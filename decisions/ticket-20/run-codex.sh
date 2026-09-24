#!/usr/bin/env bash
# PROTOTYPE -- throwaway. Ticket 20's verification run, Codex family.
# Same shape as ticket 21's runner, same binary hash (the top-level codex.exe still fails
# at config load on service_tier; 247581e40ee272fb works). Nothing installed or edited.
set -u
CX="/c/Users/User/AppData/Local/OpenAI/Codex/bin/247581e40ee272fb/codex.exe"
HERE="$(cd "$(dirname "$0")" && pwd)"
NEUTRAL="/c/Users/User/AppData/Local/Temp/proto20-neutral"
mkdir -p "$NEUTRAL" "$HERE/runs"
ARMS="${*:-student-nothing student-attempt lead-nothing student-cut student-argue}"
cd "$NEUTRAL" || exit 1
for arm in $ARMS; do
  src="$HERE/bundles/$arm.txt"; out="$HERE/runs/codex--$arm.md"; err="$HERE/runs/codex--$arm.stderr.txt"
  [ -f "$src" ] || { echo "MISSING $src"; continue; }
  start=$(date +%s)
  timeout 900 "$CX" exec --sandbox read-only --skip-git-repo-check - < "$src" > "$out" 2> "$err"
  echo "=== $arm exit=$? $(( $(date +%s)-start ))s out=$(wc -c <"$out")B err=$(wc -c <"$err")B"
done
