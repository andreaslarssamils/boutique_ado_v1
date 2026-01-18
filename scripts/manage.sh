#!/usr/bin/env bash
set -euo pipefail

# Ensure we run from repo root
cd "$(dirname "${BASH_SOURCE[0]}")/.."

# pyenv (if available)
if command -v pyenv >/dev/null 2>&1; then
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"
fi

# venv
if [[ -f "venv/bin/activate" ]]; then
  # shellcheck disable=SC1091
  source venv/bin/activate
fi

# Load .env (KEY=VALUE lines)
if [[ -f ".env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

python manage.py "$@"
