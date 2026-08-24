#!/usr/bin/env python3
"""Normalize lit/ after a retrieval run. Idempotent.

1. Renames PDFs to  YYYY-short-title-ID.pdf  in both sources.
2. Regenerates each MANIFEST.md from the saved query responses.

Does not touch QUERIES.md (records queries actually issued) or WANTED.md (hand-maintained).
"""
import datetime
import glob
import json
import os
import re

TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.abspath(__file__))


def slug(text, n=46):
    return re.sub(r"[^A-Za-z0-9]+", "-", text)[:n].strip("-").lower()


def collect(pattern, key):
    """Index every result across saved responses by an id function."""
    found = {}
    for path in glob.glob(os.path.join(ROOT, pattern)):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path) as fh:
            for rec in json.load(fh).get("results", []):
                k = key(rec)
                if k and k not in found:
                    found[k] = rec
    return found


def rename(source, pdf_id_re, meta, year_of, title_of):
    """Rename each PDF to the canonical scheme; return rows for the manifest."""
    pdf_dir = os.path.join(ROOT, source, "pdf")
    rows = []
    for name in sorted(os.listdir(pdf_dir)):
        if not name.endswith(".pdf"):
            continue
        m = re.search(pdf_id_re, name)
        ident = m.group(1) if m else name[:-4]
        rec = meta.get(ident, {})
        want = "%s-%s-%s.pdf" % (year_of(rec), slug(title_of(rec) or ident), ident)
        if name != want:
            os.rename(os.path.join(pdf_dir, name), os.path.join(pdf_dir, want))
        rows.append((rec, ident, want, os.path.getsize(os.path.join(pdf_dir, want))))
    rows.sort(key=lambda r: str(year_of(r[0])))
    return rows


NOT_RETRIEVED = (
    "\n## Not retrieved\n\n"
    "See [`../WANTED.md`](../WANTED.md) — items verified to exist but not held.\n"
)

# ----------------------------------------------------------------- OpenAlex
oa = collect("openalex/queries/*.json", lambda r: r["id"].rsplit("/", 1)[-1])
records = os.path.join(ROOT, "openalex/meta/records.json")
if os.path.exists(records):
    with open(records) as fh:
        for rec in json.load(fh)["results"]:
            oa[rec["id"].rsplit("/", 1)[-1]] = rec

rows = rename("openalex", r"(W\d+)\.pdf$", oa,
              lambda r: r.get("publication_year", "n-d"),
              lambda r: r.get("display_name"))

with open(os.path.join(ROOT, "openalex/MANIFEST.md"), "w") as fh:
    fh.write("# OpenAlex — retrieved sources\n\n")
    fh.write("Normalized %s. Queries: `QUERIES.md`. Raw responses: `queries/`.\n\n" % TODAY)
    fh.write("**Licenses are as reported by OpenAlex and are NOT verified.** `unspecified` means\n"
             "none was declared — assume all rights reserved. `submitted` versions are preprints,\n"
             "not the version of record; do not quote them as published text. See `../../.licenses/`.\n\n")
    fh.write("| Year | Title | Venue | License | Ver | DOI | File | MB |\n")
    fh.write("|---|---|---|---|---|---|---|---|\n")
    for rec, ident, fname, size in rows:
        best = rec.get("best_oa_location") or {}
        prim = (rec.get("primary_location") or {}).get("source") or {}
        fh.write("| %s | %s | %s | `%s` | %s | %s | `%s` | %.1f |\n" % (
            rec.get("publication_year", "n-d"),
            (rec.get("display_name") or "(no metadata)")[:58],
            (prim.get("display_name") or "—")[:24],
            best.get("license") or "unspecified",
            (best.get("version") or "—")[:9],
            (rec.get("doi") or "—").replace("https://doi.org/", ""),
            fname, size / 1048576))
    fh.write(NOT_RETRIEVED)

# ---------------------------------------------------------------- Europe PMC
ep = collect("epmc/queries/*.json", lambda r: r.get("pmcid"))
rows = rename("epmc", r"(PMC\d+)\.pdf$", ep,
              lambda r: r.get("pubYear", "n-d"),
              lambda r: r.get("title"))

with open(os.path.join(ROOT, "epmc/MANIFEST.md"), "w") as fh:
    fh.write("# Europe PMC — retrieved sources\n\n")
    fh.write("Normalized %s. Queries: `QUERIES.md`. Raw responses: `queries/`.\n\n" % TODAY)
    fh.write("Europe PMC returns open-access content only, but **open access is not one license** —\n"
             "terms vary per paper. `unspecified` means none declared. See `../../.licenses/`.\n\n")
    fh.write("| Year | PMCID | Title | Journal | License | DOI | File | MB |\n")
    fh.write("|---|---|---|---|---|---|---|---|\n")
    for rec, ident, fname, size in rows:
        journal = ((rec.get("journalInfo") or {}).get("journal") or {}).get("title") or "—"
        fh.write("| %s | %s | %s | %s | `%s` | %s | `%s` | %.1f |\n" % (
            rec.get("pubYear", "n-d"), ident,
            (rec.get("title") or "(no metadata)").rstrip(".")[:52],
            journal[:22], rec.get("license") or "unspecified",
            rec.get("doi") or "—", fname, size / 1048576))
    fh.write(NOT_RETRIEVED)

# ------------------------------------------------- OpenAlex query log
# Regenerable because the OpenAlex API echoes the query as meta.x_query.oql.
# The Europe PMC log is NOT regenerated: that API does not echo, so epmc/QUERIES.md
# is hand-maintained from the invoking commands.
rows = []
for path in sorted(glob.glob(os.path.join(ROOT, "openalex/queries/*.json"))):
    with open(path) as fh:
        d = json.load(fh)
    oql = (d["meta"].get("x_query") or {}).get("oql", "(not echoed)")
    rows.append((os.path.basename(path)[:-5],
                 "full-text" if "full text has" in oql else "title/abstract",
                 oql.replace("works where ", ""),
                 d["meta"]["count"]))
with open(os.path.join(ROOT, "openalex/QUERIES.md"), "w") as fh:
    fh.write("# OpenAlex \u2014 query log\n\nRegenerated %s from the API's own `x_query.oql` echo,\n" % TODAY)
    fh.write("not a reconstruction. Raw responses in `queries/`.\n\n")
    fh.write("| # | Mode | Query | Hits |\n|---|---|---|---|\n")
    for slug, mode, q, count in rows:
        fh.write("| `%s` | %s | %s | %s |\n" % (slug, mode, q, "**0**" if count == 0 else count))
    zero = [r[0] for r in rows if r[3] == 0]
    fh.write("\n## Zero-hit queries \u2014 negative results\n\n")
    fh.write("Recorded per `methods.md` \u00a77. Absence from an index is not absence of literature;\n")
    fh.write("see `../../resources.md` \u00a717.1 on what this database does and does not reach.\n\n")
    for z in zero:
        fh.write("- `%s`\n" % z)

print("normalized: %d openalex + %d epmc PDFs" % (
    len(os.listdir(os.path.join(ROOT, "openalex/pdf"))),
    len(os.listdir(os.path.join(ROOT, "epmc/pdf")))))
