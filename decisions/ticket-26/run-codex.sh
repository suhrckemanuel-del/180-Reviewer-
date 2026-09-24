#!/usr/bin/env bash
# PROTOTYPE -- throwaway. Ticket 26 register run, Codex family. Blocked until 2026-09-21 01:13 (usage limit).
# Same shape as ticket 21's runner, same binary hash (the top-level codex.exe still fails
# at config load on service_tier; 247581e40ee272fb works). Nothing installed or edited.
set -u
# 2026-09-24: the pinned 247581e40ee272fb binary no longer exists -- Codex self-updated.
# Round 1 ran on that binary, round 2 runs on this one. NOT the same instrument.
CX="/c/Users/User/AppData/Local/OpenAI/Codex/bin/80f78947ad880e6e/codex.exe"  # codex-cli 0.155.0-alpha.16.3
HERE="$(cd "$(dirname "$0")" && pwd)"
NEUTRAL="/c/Users/User/AppData/Local/Temp/proto20-neutral"
mkdir -p "$NEUTRAL" "$HERE/runs"
ARMS="${*:-student-attempt-r1 student-attempt-r2}"
cd "$NEUTRAL" || exit 1
for arm in $ARMS; do
  src="$HERE/bundles/$arm.txt"; out="$HERE/runs/codex--$arm.md"; err="$HERE/runs/codex--$arm.stderr.txt"
  [ -f "$src" ] || { echo "MISSING $src"; continue; }
  start=$(date +%s)
  timeout 900 "$CX" exec --sandbox read-only --skip-git-repo-check - < "$src" > "$out" 2> "$err"
  echo "=== $arm exit=$? $(( $(date +%s)-start ))s out=$(wc -c <"$out")B err=$(wc -c <"$err")B"
done
