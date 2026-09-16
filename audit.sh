#!/bin/bash
# Survey resources.md against the tags.md scheme. Run from the project root.
# Only multi-tag item lines are real entries; single-tag prose mentions are skipped.
#
# THIS SCRIPT REPORTS AND DOES NOT GATE. It always exits 0.
#
# Its output is written to be read by a model reviewing the register, not skimmed
# by a person. That is why it prints every section every run, unfiltered and
# without summarising: reading the whole report is cheap for the intended reader
# and is the point. A person filtering it down to the sections they just edited is
# how a repeated-facet violation survived two commits.
#
# Most of what it prints is an observation rather than a violation — the census and
# counts are state, and the CJK check surfaces every instance so the reader can
# judge which are intentional. Deciding which findings block is preflight.sh's job,
# and it names them explicitly rather than inferring them from an exit code here.
echo "=== tag-cap or repeated-facet violations ==="
# Cap applies to the descriptive facets only (tags.md rule 7): at most three of
# #d #c #r #f, exactly one #e, at most one each of #v and #s.
grep -o '`#[dcrefvs]/[a-z-]*\( #[dcrefvs]/[a-z-]*\)\+`' resources.md | while read -r l; do
  desc=$(printf '%s' "$l" | grep -o '#[dcrf]/' | wc -l)
  dup=$(printf '%s' "$l" | grep -o '#[dcrefvs]/' | sort | uniq -d)
  ne=$(printf '%s' "$l" | grep -o '#e/' | wc -l)
  if [ "$desc" -gt 3 ] || [ -n "$dup" ] || [ "$ne" -ne 1 ]; then echo "  VIOLATION: $l"; fi
done
echo "=== entries missing the mandatory #e/ ==="
grep -o '`#[dcrefvs]/[a-z-]*\( #[dcrefvs]/[a-z-]*\)\+`' resources.md | grep -v '#e/' | sed 's/^/  VIOLATION: /'
echo "=== retired vocabulary still in use ==="
# Values removed by the 2026-09-14 facet split. They must not reappear.
# Scanned everywhere, not just the tagged files: README.md and tags.md *describe*
# the scheme, and stale descriptions there outlived the migration precisely because
# this check did not look at them.
#
# Some mentions are legitimate — the history of the split, and grep recipes that
# deliberately hunt for the old values. Those opt out with the token 'retired-ok'
# on the line (an HTML comment in prose, a shell comment inside a code fence).
# Opting out by marker rather than by matching the surrounding phrasing means the
# exemption survives an edit to the sentence around it.
grep -n '#e/attested\|#e/devotional\|#e/contested\|#e/fringe\|#e/speculative\|#e/unverified' \
  *.md lit/*.md lit/*/*.md 2>/dev/null \
  | grep -v 'retired-ok' \
  | sed 's/^/  RETIRED: /'
echo "=== tags used but not defined in tags.md ==="
comm -23 <(grep -oh '#[dcrefvs]/[a-z-]*' resources.md methods.md background.md | sort -u) \
         <(grep -o '#[dcrefvs]/[a-z-]*' tags.md | sort -u) | sed 's/^/  UNDEFINED: /'
echo "=== census (resources.md) ==="
grep -o '#[dcrefvs]/[a-z-]*' resources.md | sort | uniq -c | sort -rn | head -10
echo "=== counts ==="
# A register entry is a '- ' line whose indented continuation block carries the
# mandatory #e/ tag. Counting bare '- ' lines conflates entries with ordinary
# prose bullets; looking only at the next line misses multi-line entries.
printf '  entries: %s\n' "$(awk '
  /^- / { if (inblk && hit) n++; inblk=1; hit=0; next }
  /^[ \t]/ { if (inblk && /#e\//) hit=1; next }
  { if (inblk && hit) n++; inblk=0; hit=0 }
  END { if (inblk && hit) n++; print n+0 }' resources.md)"
printf '  open questions: %s\n' "$(grep -ch '^?' resources.md background.md | paste -sd+ | bc)"
printf '  unverified: %s\n' "$(grep -c '\[unverified\]' resources.md)"
echo "=== leftover draft markers ==="
grep -n 'superseded\|see corrected entry\|— \*see note\*\|invalid, two' resources.md | sed 's/^/  STALE: /'
echo "=== subsection headers out of sync with parent ==="
uv run --no-project python3 - <<'PY'
import re
cur=None; bad=0
for i,l in enumerate(open("resources.md"),1):
    m=re.match(r"^## (\d+)\. ",l)
    if m: cur=m.group(1)
    m2=re.match(r"^### (\d+)\.(\d+)",l)
    if m2 and cur and m2.group(1)!=cur:
        print(f"  MISMATCH line {i}: {l.strip()[:56]} (parent is §{cur})"); bad+=1
PY
echo "=== encoding: invalid UTF-8 ==="
for f in *.md lit/*.md lit/*/*.md; do
  [ -f "$f" ] || continue
  iconv -f UTF-8 -t UTF-8 "$f" >/dev/null 2>&1 || echo "  INVALID UTF-8: $f"
done
echo "=== encoding: mojibake signatures (UTF-8 read as Latin-1) ==="
grep -n 'â€\|Ã[©¨¤¶±]\|Â[ §°]\|ï»¿' *.md lit/*.md lit/*/*.md 2>/dev/null | sed 's/^/  MOJIBAKE: /'
echo "=== stray CJK (review: 景教 in terms.md is intentional) ==="
grep -nP '[\x{3000}-\x{9FFF}]' *.md lit/*.md lit/*/*.md 2>/dev/null | cut -c1-88 | sed 's/^/  CJK: /'
echo "=== dangling subsection references ==="
for s in $(grep -oh '§[0-9]\+\.[0-9]' *.md | sort -u); do
  n=${s#§}
  grep -q "^### ${n}" resources.md || grep -q "^### ${n}" methods.md || grep -q "^## ${n%%.*}" methods.md || echo "  DANGLING: $s"
done

echo "=== build_tables.py unit tests ==="
# Quiet when they pass, full output when they do not — a summary line is no use
# when something broke.
if out=$(uv run --no-project python3 scripts/test_build_tables.py 2>&1); then
  printf '  %s\n' "$(printf '%s' "$out" | tail -n1)"
else
  printf '%s\n' "$out" | sed 's/^/  /'
fi

echo "=== derived tables out of sync with their sources ==="
# results/*.csv.gz are committed, so they can go stale silently — as they did
# through the facet split, still carrying retired values two weeks later.
out=$(uv run --no-project scripts/build_tables.py --check 2>&1)
printf '%s\n' "$out" | sed 's/^/  /' 

echo "=== duplicate section numbers ==="
for f in background.md methods.md resources.md tags.md terms.md chronology.md geography.md; do
  [ -f "$f" ] || continue
  grep -oE '^#+ [0-9]+(\.[0-9a-z]+)* ' "$f" | sed 's/^#* //; s/ $//' | sort | uniq -d \
    | while read -r n; do printf '  %s: section %s declared more than once\n' "$f" "$n"; done
done
