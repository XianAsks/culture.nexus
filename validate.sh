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
printf '  entries: %s\n' "$(grep -c '^- ' resources.md)"
printf '  open questions: %s\n' "$(grep -ch '^?' resources.md background.md | paste -sd+ | bc)"
printf '  unverified: %s\n' "$(grep -c '\[unverified\]' resources.md)"
exit 0
