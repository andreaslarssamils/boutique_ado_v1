#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

./scripts/manage.sh shell -c "from django.contrib.sessions.models import Session; Session.objects.all().delete(); print('Deleted sessions')"
