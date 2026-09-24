#!/usr/bin/env bash
# PROTOTYPE -- throwaway. Ticket 21. Same shape as proto-04's runner; the binary
# hash moved (the old one is gone from this machine), so it is resolved here.
set -u
CX="/c/Users/User/AppData/Local/OpenAI/Codex/bin/247581e40ee272fb/codex.exe"
HERE="$(cd "$(dirname "$0")" && pwd)"
NEUTRAL="/c/Users/User/AppData/Local/Temp/proto21-neutral"
mkdir -p "$NEUTRAL" "$HERE/runs"
ARMS="${*:-nogate-full-no both-full-no both-full-yes both-tail65-no both-tail40-no both-headdrop-no both-headdrop-yes p1-headdrop-no p2-headdrop-no both-headdrop2-no}"
cd "$NEUTRAL" || exit 1
for arm in $ARMS; do
  src="$HERE/bundles/$arm.txt"; out="$HERE/runs/codex--$arm.md"; err="$HERE/runs/codex--$arm.stderr.txt"
  [ -f "$src" ] || { echo "MISSING $src"; continue; }
  start=$(date +%s)
  timeout 900 "$CX" exec --sandbox read-only --skip-git-repo-check - < "$src" > "$out" 2> "$err"
  echo "=== $arm exit=$? $(( $(date +%s)-start ))s out=$(wc -c <"$out")B err=$(wc -c <"$err")B"
done
