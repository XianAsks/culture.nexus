#!/bin/bash
# Gate the register before staging. Run from the project root.
#
#   ./preflight.sh        exits 0 when clean, 1 when an assertion fails
#
# The companion to audit.sh, which surveys and always exits 0. The split is
# deliberate: most of what audit.sh prints is an observation rather than a
# violation, so an exit code derived from "did anything print" would be wrong in
# both directions. This script names the sections that are assertions, and treats
# every other section as advisory.
#
# The two have different readers. audit.sh is read and judged by a model, which can
# weigh an observation in context. This one answers a mechanical yes/no that must
# hold whether or not anything read the report at all.
#
# It runs audit.sh rather than reimplementing its checks, so the check logic
# has one home and the two scripts cannot drift apart. What lives here is the
# judgement about which findings block, which is the thing that was never decided.

set -uo pipefail

# Sections whose findings are violations. A finding here means the register
# contradicts its own scheme, or a derived artefact disagrees with its source.
ASSERTIONS=(
  "tag-cap or repeated-facet violations"
  "entries missing the mandatory #e/"
  "retired vocabulary still in use"
  "tags used but not defined in tags.md"
  "leftover draft markers"
  "subsection headers out of sync with parent"
  "encoding: invalid UTF-8"
  "encoding: mojibake signatures (UTF-8 read as Latin-1)"
  "dangling subsection references"
  "duplicate section numbers"
)

# Sections that always print, or that exist to put something in front of a human.
# Listed rather than inferred so that adding a section to audit.sh without
# classifying it here is caught below, instead of silently defaulting to one side.
ADVISORY=(
  "census (resources.md)"
  "counts"
  "stray CJK (review: 景教 in terms.md is intentional)"
  "build_tables.py unit tests"
  "derived tables out of sync with their sources"
)

report=$(./audit.sh 2>&1) || true

section() {
  # Body lines of one "=== name ===" section, up to the next header.
  printf '%s\n' "$report" \
    | awk -v want="=== $1 ===" '
        $0 == want { on = 1; next }
        /^=== / { on = 0 }
        on { print }
      '
}

has_section() {
  printf '%s\n' "$report" | grep -qxF "=== $1 ==="
}

status=0

# The two checks that are assertions but report through their own exit status
# rather than by printing findings: an empty section means nothing ran, not that
# all is well, so they are gated on the command rather than on the output.
if ! uv run --no-project python3 scripts/test_build_tables.py >/dev/null 2>&1; then
  echo "BLOCKED  unit tests failing — scripts/test_build_tables.py"
  status=1
fi
if ! uv run --no-project scripts/build_tables.py --check >/dev/null 2>&1; then
  echo "BLOCKED  results/ out of sync — run scripts/build_tables.py"
  status=1
fi

for name in "${ASSERTIONS[@]}"; do
  if ! has_section "$name"; then
    echo "BLOCKED  no section '$name' in audit.sh output — renamed or removed?"
    status=1
    continue
  fi
  findings=$(section "$name" | grep -c '[^[:space:]]')
  if [ "$findings" -gt 0 ]; then
    echo "BLOCKED  $name ($findings)"
    section "$name" | sed 's/^/         /'
    status=1
  fi
done

# Every section audit.sh prints must be classified one way or the other. A new
# check that nobody triaged is itself a finding: silence would let it default to
# advisory, which is how a gate quietly stops gating.
while IFS= read -r name; do
  for known in "${ASSERTIONS[@]}" "${ADVISORY[@]}"; do
    [ "$name" = "$known" ] && continue 2
  done
  echo "BLOCKED  unclassified section '$name' — add it to ASSERTIONS or ADVISORY"
  status=1
done < <(printf '%s\n' "$report" | sed -n 's/^=== \(.*\) ===$/\1/p')

if [ "$status" -eq 0 ]; then
  echo "preflight clean — ${#ASSERTIONS[@]} assertions, ${#ADVISORY[@]} advisory"
  echo "run ./audit.sh for the full report, including the advisory sections"
fi
exit "$status"
