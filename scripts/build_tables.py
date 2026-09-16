#!/usr/bin/env python3
"""Parse chronology.md and geography.md into machine-readable tables.

The markdown files are the source of truth. This script derives everything that
can be derived — astronomical years, spans, polity durations — so that the
arithmetic has exactly one home and cannot drift from the prose.

  uv run --no-project scripts/build_tables.py

Writes results/{chronology,places,polities,durations}.csv.gz.

Date notation is specified in chronology.md §2 and is deliberately a closed
vocabulary so that it stays parseable:

  1048 CE | c. 375 CE | [30-375 CE] | t.p.q. 1048 CE | t.a.q. 1028 CE
  fl. 1010-1028 CE | C6 CE | [C1-C3 CE] | [c. 500 BCE-c. 1000 CE] | 762 CE-present

Arithmetic uses astronomical year numbering (1 BCE = 0, 2 BCE = -1) because
historians' BCE/CE has no year zero, so naive subtraction overstates every span
crossing the epoch by one year.
"""

from __future__ import annotations

import csv
import datetime as dt
import gzip
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

# An en-dash, a hyphen and a minus sign all appear in hand-written tables.
DASH = r"[-‐‑‒–—−]"
PRESENT_YEAR = dt.date.today().year


def astronomical(year: int, era: str) -> int:
    """Convert a historians' year to astronomical numbering.

    CE years are unchanged; 1 BCE becomes 0, 2 BCE becomes -1. Without this,
    200 BCE to 10 CE computes as 210 years instead of the correct 209.
    """
    return year if era == "CE" else 1 - year


def century_bounds(n: int, era: str) -> tuple[int, int]:
    """Inclusive astronomical bounds of the nth century."""
    if era == "CE":
        return (n - 1) * 100 + 1, n * 100
    return astronomical(n * 100, "BCE"), astronomical((n - 1) * 100 + 1, "BCE")


_ENDPOINT = re.compile(
    r"^\s*(?P<circa>c\.\s*)?(?:(?P<cent>C(?P<cn>\d{1,2}))|(?P<yr>\d{1,4}))"
    r"(?:\s*(?P<era>BCE|CE))?\s*$",
    re.I,
)


def _endpoint(text: str, default_era: str | None) -> tuple[int, int, bool, bool] | None:
    """Parse one endpoint -> (lo, hi, circa, is_century) in astronomical years."""
    if text.strip().lower() == "present":
        return PRESENT_YEAR, PRESENT_YEAR, False, False
    m = _ENDPOINT.match(text)
    if not m:
        return None
    era = (m.group("era") or default_era or "CE").upper()
    circa = bool(m.group("circa"))
    if m.group("cent"):
        n = int(m.group("cn"))
        # There is no zeroth century. Without this, "C0 CE" silently yields the
        # span -99 to 0 — a typo becomes a date a century off and in the wrong
        # era, which is worse than the row being reported as unreadable.
        if n == 0:
            return None
        lo, hi = century_bounds(n, era)
        return lo, hi, circa, True
    year = int(m.group("yr"))
    # Likewise no year zero: the notation is historians', not astronomical.
    if year == 0:
        return None
    y = astronomical(year, era)
    return y, y, circa, False


def parse_date(raw: str) -> dict:
    """Parse a chronology/geography date cell into structured fields."""
    out = {
        "date_display": raw.strip(),
        "qualifier": "exact",
        "year_start": None,
        "year_end": None,
        "circa": False,
        "parsed": False,
    }
    s = raw.strip()
    if not s or s == "—":
        return out

    if s.startswith("[") and s.endswith("]"):
        out["qualifier"] = "range"
        s = s[1:-1].strip()
    elif s.lower().startswith("t.p.q."):
        out["qualifier"] = "tpq"
        s = s[6:].strip()
    elif s.lower().startswith("t.a.q."):
        out["qualifier"] = "taq"
        s = s[6:].strip()
    elif s.lower().startswith("fl."):
        out["qualifier"] = "floruit"
        s = s[3:].strip()

    # The era often appears only on the final endpoint: "[30-375 CE]".
    tail = re.search(r"(BCE|CE)\s*$", s, re.I)
    default_era = tail.group(1).upper() if tail else "CE"

    parts = re.split(DASH, s)
    if len(parts) == 2:
        a = _endpoint(parts[0], default_era)
        b = _endpoint(parts[1], default_era)
        if a and b:
            out.update(
                year_start=a[0], year_end=b[1], circa=a[2] or b[2], parsed=True
            )
            if out["qualifier"] == "exact":
                out["qualifier"] = "range"
            return out
        return out

    one = _endpoint(s, default_era)
    if one:
        out.update(year_start=one[0], year_end=one[1], circa=one[2], parsed=True)
        # A century is a 100-year span. Reporting it as "exact" would assert a
        # precision the source never gave — the false precision geography.md §3
        # flags for region coordinates, in the time axis.
        if one[3] and out["qualifier"] == "exact":
            out["qualifier"] = "century"
    return out


def read_table(path: Path, header_key: str) -> list[dict]:
    """Read the first markdown table whose header row contains header_key."""
    rows, header, in_table = [], None, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        if header is None:
            if header_key in cells:
                header, in_table = cells, True
            continue
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    if header is None:
        sys.exit(f"no table with column {header_key!r} in {path.name}")
    return rows


def strip_tag(v: str) -> str:
    """Normalise a markdown tag cell to bare text.

    The cell is backtick-quoted but `[unverified]` sits *outside* the quotes, as
    in "`#e/secondary` [unverified]". Stripping only the outer pair therefore
    left the closing backtick embedded in the value.
    """
    return " ".join(v.replace("`", " ").split())


def render_csv(fieldnames: list[str], rows: list[dict]) -> str:
    """Render the table to CSV text, separately from how it is stored.

    Splitting render from write is what lets --check compare *content*: gzip
    embeds a timestamp, so comparing compressed bytes reports drift on every run.
    """
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore",
                       lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def write_csv(name: str, fieldnames: list[str], rows: list[dict]) -> Path:
    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / f"{name}.csv.gz"
    # mtime=0 keeps the output byte-identical for identical content, so the file
    # only shows up in git when the table actually changed.
    with open(out, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as gz:
        gz.write(render_csv(fieldnames, rows).encode("utf-8"))
    return out


def check_csv(name: str, fieldnames: list[str], rows: list[dict]) -> str | None:
    """Return a one-line description of the drift, or None when in sync."""
    out = RESULTS / f"{name}.csv.gz"
    if not out.exists():
        return f"{out.relative_to(ROOT)}: missing"
    want = render_csv(fieldnames, rows)
    with gzip.open(out, "rt", encoding="utf-8", newline="") as fh:
        have = fh.read()
    if have == want:
        return None
    w_lines, h_lines = want.splitlines(), have.splitlines()
    delta = len(w_lines) - len(h_lines)
    changed = sum(1 for a, b in zip(w_lines, h_lines) if a != b)
    parts = []
    if delta:
        parts.append(f"{delta:+d} rows")
    if changed:
        parts.append(f"{changed} changed")
    return f"{out.relative_to(ROOT)}: {', '.join(parts) or 'differs'}"


def build_chronology() -> list[dict]:
    rows = []
    for r in read_table(ROOT / "chronology.md", "kind"):
        d = parse_date(r["date"])
        rows.append(
            {
                "id": r["id"],
                "date_display": d["date_display"],
                "qualifier": d["qualifier"],
                "year_start": d["year_start"],
                "year_end": d["year_end"],
                "circa": d["circa"],
                "parsed": d["parsed"],
                "kind": r["kind"],
                "entity": r["entity"],
                "bears_on": r["bears-on"],
                "tag": strip_tag(r["tag"]),
                "rung": r["rung"] if r["rung"] != "—" else "",
            }
        )
    rows.sort(key=lambda x: (x["year_start"] is None, x["year_start"] or 0))
    return rows


def build_places() -> list[dict]:
    rows = []
    for r in read_table(ROOT / "geography.md", "kind"):
        d = parse_date(r["rel"])
        rows.append(
            {
                "id": r["id"],
                "name": r["name"],
                "kind": r["kind"],
                "qid": r["qid"],
                # "~" marks a region centroid, not a location: see geography.md §3.
                "lat": r["lat"].lstrip("~") or "",
                "lon": r["lon"].lstrip("~") or "",
                "approx_coord": r["lat"].startswith("~"),
                "modern": r["modern"],
                "rel_display": d["date_display"],
                "rel_start": d["year_start"],
                "rel_end": d["year_end"],
                "tag": strip_tag(r["tag"]),
                "bears_on": r["bears-on"],
            }
        )
    return rows


def build_polities() -> list[dict]:
    rows = []
    for r in read_table(ROOT / "geography.md", "from"):
        a, b = parse_date(r["from"]), parse_date(r["to"])
        duration = None
        if a["parsed"] and b["parsed"]:
            duration = b["year_end"] - a["year_start"]
        rows.append(
            {
                "id": r["id"],
                "name": r["name"],
                "qid": r["qid"],
                "from_display": a["date_display"],
                "to_display": b["date_display"],
                "from_year": a["year_start"],
                "to_year": b["year_end"],
                "duration_years": duration,
                "approximate": a["circa"] or b["circa"],
                "tag": strip_tag(r["tag"]),
                "note": r["note"],
            }
        )
    rows.sort(key=lambda x: (x["duration_years"] is None, x["duration_years"] or 0))
    return rows


def main() -> None:
    chron = build_chronology()
    places = build_places()
    polities = build_polities()

    tables = [
        ("chronology", list(chron[0]), chron),
        ("places", list(places[0]), places),
        ("polities", list(polities[0]), polities),
        ("durations", list(polities[0]), polities),
    ]

    if "--check" in sys.argv:
        drift = [d for d in (check_csv(*t) for t in tables) if d]
        for d in drift:
            print(f"  STALE: {d}")
        if drift:
            print(f"\n{len(drift)} of {len(tables)} tables are out of date. "
                  f"Run scripts/build_tables.py to regenerate.")
            sys.exit(1)
        print(f"results/ in sync with chronology.md and geography.md "
              f"({len(tables)} tables)")
        return

    written = [write_csv(*t) for t in tables]

    unparsed = [r["id"] for r in chron if not r["parsed"]]
    nodur = [r["id"] for r in polities if r["duration_years"] is None]

    print(f"chronology : {len(chron):3d} rows, {len(chron) - len(unparsed)} dated")
    print(f"places     : {len(places):3d} rows")
    print(f"polities   : {len(polities):3d} rows, {len(polities) - len(nodur)} with duration")
    if unparsed:
        print(f"  UNPARSED dates: {', '.join(unparsed)}")
    if nodur:
        print(f"  NO duration  : {', '.join(nodur)}")
    print()
    print("durations, shortest first:")
    for r in polities:
        d = r["duration_years"]
        print(f"  {r['name']:26} {r['from_display']:>14} - {r['to_display']:<14} "
              f"{'' if d is None else str(d) + ' yr'}{' ~' if r['approximate'] else ''}")
    print()
    for p in written:
        print(f"wrote {p.relative_to(ROOT)} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
