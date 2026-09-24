#!/usr/bin/env bash
set -u
CX="/c/Users/User/AppData/Local/OpenAI/Codex/bin/codex.exe"
export CODEX_HOME="C:\Users\User\AppData\Local\Temp\proto12-codexhome"
HERE="$(cd "$(dirname "$0")" && pwd)"
cd /c/Users/User/AppData/Local/Temp/proto12-neutral || exit 1
run() { local arm="$1" n="$2" i
  for ((i=1;i<=n;i++)); do
    local out="$HERE/runs/codex--$arm--r$i.md"
    [ -s "$out" ] && { echo "skip $arm r$i"; continue; }
    timeout 900 "$CX" exec --sandbox read-only --skip-git-repo-check - \
      < "$HERE/bundles/$arm.txt" > "$out" 2> "$HERE/runs/codex--$arm--r$i.err.txt"
    echo "$arm r$i exit=$? out=$(wc -c <"$out")b"
  done; }
run B3-headdrop 4
run B3-full 4
run B3-tail92 3
echo BATCH3DONE
