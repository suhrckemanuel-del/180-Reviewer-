#!/usr/bin/env bash
# PROTOTYPE -- throwaway. Ticket 12.
# Runs each arm N times through Codex. Clean CODEX_HOME so the machine's
# config.toml (service_tier=default, rejected by this build) is bypassed.
set -u
CX="/c/Users/User/AppData/Local/OpenAI/Codex/bin/codex.exe"
export CODEX_HOME="C:\Users\User\AppData\Local\Temp\proto12-codexhome"
HERE="$(cd "$(dirname "$0")" && pwd)"
NEUTRAL="/c/Users/User/AppData/Local/Temp/proto12-neutral"
mkdir -p "$NEUTRAL" "$HERE/runs"
cd "$NEUTRAL" || exit 1

run() {   # run <arm> <n>
  local arm="$1" n="$2" i
  for ((i=1;i<=n;i++)); do
    local src="$HERE/bundles/$arm.txt" out="$HERE/runs/codex--$arm--r$i.md"
    [ -f "$src" ] || { echo "MISSING $src"; return; }
    [ -s "$out" ] && { echo "skip $arm r$i"; continue; }
    local s=$(date +%s)
    timeout 900 "$CX" exec --sandbox read-only --skip-git-repo-check - \
        < "$src" > "$out" 2> "$HERE/runs/codex--$arm--r$i.err.txt"
    echo "$arm r$i exit=$? $(( $(date +%s)-s ))s out=$(wc -c <"$out")b"
  done
}

run B-full 5
run B-headdrop 3
run B-tail97 3
run A-probe-full 5
run A-probe-headdrop 2
run B-tail85 2
run B-tail65 1
echo ALLDONE
