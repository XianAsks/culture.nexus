#!/bin/bash
# Validate resources.md against the tags.md scheme. Run from the project root.
# Only multi-tag item lines are real entries; single-tag prose mentions are skipped.
fail=0
echo "=== >3 tags, or a repeated facet ==="
while read -r l; do
  n=$(printf '%s' "$l" | grep -oF '#' | wc -l)
  dup=$(printf '%s' "$l" | grep -o '#[dcref]/' | sort | uniq -d)
  if [ "$n" -gt 3 ] || [ -n "$dup" ]; then echo "  VIOLATION: $l"; fail=1; fi
done < <(grep -o '`#[dcref]/[a-z-]*\( #[dcref]/[a-z-]*\)\+`' resources.md)
echo "=== entries missing the mandatory #e/ ==="
grep -o '`#[dcref]/[a-z-]*\( #[dcref]/[a-z-]*\)\+`' resources.md | grep -v '#e/' | sed 's/^/  VIOLATION: /' && fail=1
echo "=== tags used but not defined in tags.md ==="
comm -23 <(grep -oh '#[dcref]/[a-z-]*' resources.md methods.md background.md | sort -u) \
         <(grep -o '#[dcref]/[a-z-]*' tags.md | sort -u) | sed 's/^/  UNDEFINED: /'
echo "=== census (resources.md) ==="
grep -o '#[dcref]/[a-z-]*' resources.md | sort | uniq -c | sort -rn | head -8
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

echo "=== duplicate section numbers ==="
for f in background.md methods.md resources.md tags.md terms.md chronology.md geography.md; do
  [ -f "$f" ] || continue
  grep -oE '^#+ [0-9]+(\.[0-9a-z]+)* ' "$f" | sed 's/^#* //; s/ $//' | sort | uniq -d \
    | while read -r n; do printf '  %s: section %s declared more than once\n' "$f" "$n"; done
done
