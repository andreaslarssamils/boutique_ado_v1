#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

export DEVELOPMENT=1

./scripts/manage.sh runserver
