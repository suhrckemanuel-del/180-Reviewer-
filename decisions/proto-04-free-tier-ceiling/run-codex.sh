#!/usr/bin/env bash
# PROTOTYPE -- throwaway. Ticket 04.
#
# Runs every arm in ./bundles through Codex (gpt-5.6-sol) and saves the reply.
# Uses the binary the Codex desktop app ships, because the npm-installed CLI on
# this machine is too old for the account's model. Nothing is installed and no
# config is edited: the only override is service_tier, which the old config.toml
# sets to a value this build rejects.
#
# Run from a neutral cwd so no AGENTS.md is picked up.

set -u

CX="/c/Users/User/AppData/Local/OpenAI/Codex/bin/eab8377aebac6c07/codex.exe"
HERE="$(cd "$(dirname "$0")" && pwd)"
NEUTRAL="/c/Users/User/AppData/Local/Temp/proto04-neutral"
mkdir -p "$NEUTRAL" "$HERE/runs"

ARMS="${*:-full-prose full-html tail85-prose tail65-prose tail40-prose tail65-html headdrop-prose}"

cd "$NEUTRAL" || exit 1

for arm in $ARMS; do
  src="$HERE/bundles/$arm.txt"
  out="$HERE/runs/codex--$arm.md"
  err="$HERE/runs/codex--$arm.stderr.txt"
  [ -f "$src" ] || { echo "MISSING $src"; continue; }

  echo "=== $arm  ($(wc -c <"$src") chars) ==="
  start=$(date +%s)
  timeout 900 "$CX" exec --sandbox read-only --skip-git-repo-check - \
      < "$src" > "$out" 2> "$err"
  code=$?
  end=$(date +%s)
  echo "    exit=$code  $((end-start))s  out=$(wc -c <"$out") bytes"
done
