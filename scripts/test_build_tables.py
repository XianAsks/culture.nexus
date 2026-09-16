#!/usr/bin/env python3
"""Tests for build_tables.py.

  uv run --no-project scripts/test_build_tables.py

Standard library only, so it runs wherever the generator does and needs no
project metadata. audit.sh runs it.

The date notation these tests exercise is specified in chronology.md §2 and is
deliberately a closed vocabulary. Each form there should have a case here: an
unparseable date is reported rather than raised, so a silent regression shows up
as rows quietly dropping out of the tables rather than as a crash.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_tables as bt


class TestAstronomical(unittest.TestCase):
    """Astronomical year numbering — the off-by-one the whole file exists for."""

    def test_ce_unchanged(self):
        self.assertEqual(bt.astronomical(1048, "CE"), 1048)
        self.assertEqual(bt.astronomical(1, "CE"), 1)

    def test_bce_has_a_year_zero(self):
        self.assertEqual(bt.astronomical(1, "BCE"), 0)
        self.assertEqual(bt.astronomical(2, "BCE"), -1)
        self.assertEqual(bt.astronomical(200, "BCE"), -199)

    def test_the_documented_span(self):
        """Indo-Greek, 200 BCE to 10 CE, is 209 years and not 210."""
        lo = bt.astronomical(200, "BCE")
        hi = bt.astronomical(10, "CE")
        self.assertEqual(hi - lo, 209)


class TestCenturyBounds(unittest.TestCase):
    def test_ce(self):
        self.assertEqual(bt.century_bounds(1, "CE"), (1, 100))
        self.assertEqual(bt.century_bounds(6, "CE"), (501, 600))
        self.assertEqual(bt.century_bounds(20, "CE"), (1901, 2000))

    def test_bce_runs_backwards(self):
        # C1 BCE is 100 BCE to 1 BCE, i.e. astronomical -99 to 0.
        self.assertEqual(bt.century_bounds(1, "BCE"), (-99, 0))
        self.assertEqual(bt.century_bounds(5, "BCE"), (-499, -400))

    def test_bounds_are_ordered(self):
        for era in ("CE", "BCE"):
            for n in range(1, 21):
                lo, hi = bt.century_bounds(n, era)
                self.assertLess(lo, hi, f"C{n} {era}")


class TestParseDate(unittest.TestCase):
    """One case per form in chronology.md §2.2's closed vocabulary."""

    def assertDate(self, raw, qualifier, start, end, circa=False):
        got = bt.parse_date(raw)
        self.assertTrue(got["parsed"], f"{raw!r} did not parse")
        self.assertEqual(got["qualifier"], qualifier, raw)
        self.assertEqual(got["year_start"], start, raw)
        self.assertEqual(got["year_end"], end, raw)
        self.assertEqual(got["circa"], circa, raw)

    def test_exact(self):
        self.assertDate("1048 CE", "exact", 1048, 1048)

    def test_circa(self):
        self.assertDate("c. 375 CE", "exact", 375, 375, circa=True)

    def test_range(self):
        self.assertDate("[30–375 CE]", "range", 30, 375)

    def test_range_both_bce(self):
        """The era appears only on the final endpoint and governs both."""
        self.assertDate("[500–300 BCE]", "range", -499, -299)

    def test_range_crossing_the_epoch(self):
        self.assertDate("[200 BCE–10 CE]", "range", -199, 10)

    def test_terminus_post_quem(self):
        self.assertDate("t.p.q. 1048 CE", "tpq", 1048, 1048)

    def test_terminus_ante_quem(self):
        self.assertDate("t.a.q. 1028 CE", "taq", 1028, 1028)

    def test_floruit(self):
        self.assertDate("fl. 1010–1028 CE", "floruit", 1010, 1028)

    def test_century(self):
        self.assertDate("C6 CE", "century", 501, 600)

    def test_century_range(self):
        self.assertDate("[C1–C3 CE]", "range", 1, 300)

    def test_century_range_bce(self):
        self.assertDate("[C5–C3 BCE]", "range", -499, -200)

    def test_circa_century(self):
        self.assertDate("c. C10 CE", "century", 901, 1000, circa=True)

    def test_mixed_circa_range(self):
        self.assertDate("[c. 500 BCE–c. 1000 CE]", "range", -499, 1000, circa=True)

    def test_present(self):
        got = bt.parse_date("762 CE–present")
        self.assertTrue(got["parsed"])
        self.assertEqual(got["year_start"], 762)
        self.assertEqual(got["year_end"], bt.PRESENT_YEAR)

    def test_all_dash_characters_split(self):
        """Hand-written tables carry several dashes; all must behave alike."""
        for dash in ("-", "‐", "‑", "‒", "–", "—", "−"):
            with self.subTest(dash=dash):
                self.assertDate(f"[30{dash}375 CE]", "range", 30, 375)

    def test_lowercase_era(self):
        self.assertDate("1048 ce", "exact", 1048, 1048)


class TestParseDateRejects(unittest.TestCase):
    """Bad input must be reported as unparsed, never raise and never guess."""

    def test_unparsed_cases(self):
        for raw in ("", "   ", "—", "sometime later", "the ninth century",
                    # No zeroth century and no year zero: the notation is
                    # historians', so both are typos rather than dates.
                    "C0 CE", "0 CE", "0 BCE", "[C0–C3 CE]"):
            with self.subTest(raw=raw):
                got = bt.parse_date(raw)
                self.assertFalse(got["parsed"], f"{raw!r} should not parse")
                self.assertIsNone(got["year_start"])
                self.assertIsNone(got["year_end"])

    def test_display_is_always_preserved(self):
        self.assertEqual(bt.parse_date("  sometime later ")["date_display"],
                         "sometime later")


class TestStripTag(unittest.TestCase):
    def test_unverified_sits_outside_the_backticks(self):
        """Regression: the closing backtick was carried into the value."""
        self.assertEqual(bt.strip_tag("`#e/secondary` [unverified]"),
                         "#e/secondary [unverified]")

    def test_plain(self):
        self.assertEqual(bt.strip_tag("`#e/secondary`"), "#e/secondary")

    def test_multiple_facets(self):
        self.assertEqual(bt.strip_tag("`#e/secondary #s/contested`"),
                         "#e/secondary #s/contested")

    def test_no_backticks_left_anywhere(self):
        for cell in ("`#e/primary` [unverified]", "`a` `b`", "#e/inferred"):
            self.assertNotIn("`", bt.strip_tag(cell), cell)


class TestRenderAndCheck(unittest.TestCase):
    ROWS = [{"id": "a", "n": 1}, {"id": "b", "n": 2}]
    FIELDS = ["id", "n"]

    def test_render_is_deterministic(self):
        first = bt.render_csv(self.FIELDS, self.ROWS)
        self.assertEqual(first, bt.render_csv(self.FIELDS, self.ROWS))

    def test_render_uses_unix_line_endings(self):
        """CRLF once blocked a commit; the tables are text in git."""
        self.assertNotIn("\r", bt.render_csv(self.FIELDS, self.ROWS))

    def test_check_reports_a_missing_table(self):
        self.assertIn("missing", bt.check_csv("no-such-table", self.FIELDS, self.ROWS))


class TestTablesInSync(unittest.TestCase):
    """The committed tables must match what the sources produce.

    This is the check that was absent while results/ described the retired
    evidential scheme for two weeks.
    """

    def test_in_sync(self):
        chron = bt.build_chronology()
        places = bt.build_places()
        polities = bt.build_polities()
        for name, rows in (("chronology", chron), ("places", places),
                           ("polities", polities), ("durations", polities)):
            with self.subTest(table=name):
                self.assertIsNone(bt.check_csv(name, list(rows[0]), rows))

    def test_every_date_parses(self):
        unparsed = [r["id"] for r in bt.build_chronology() if not r["parsed"]]
        self.assertEqual(unparsed, [], "chronology rows with unreadable dates")


if __name__ == "__main__":
    unittest.main(verbosity=2)
