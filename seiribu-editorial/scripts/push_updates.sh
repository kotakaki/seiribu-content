#!/usr/bin/env bash
set -euo pipefail

message="${1:-Update editorial files}"

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

git diff --check
git status --short

git add .
git commit -m "$message"
git push origin main
