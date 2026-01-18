# Boutique ADO (local dev)

This repo is set up for an older dependency stack (Django 3.0.1), so it is expected to run on **Python 3.8.x**.

## Quickstart

### 1) Python + venv

This project uses `pyenv` and a checked-in `.python-version`.

```bash
pyenv install 3.8.18
pyenv local 3.8.18

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

(Optional) Load fixtures:

```bash
python manage.py loaddata categories
python manage.py loaddata products
```

### 2) Environment variables

Checkout requires Stripe keys.

- Copy `.env.example` to `.env` and fill in values.
- `scripts/dev.sh` will automatically load `.env` if present.

### 3) Run the server

```bash
./scripts/dev.sh
```

(Equivalent):

```bash
export DEVELOPMENT=1
python manage.py runserver
```

## Common tasks

- Run any `manage.py` command with env + venv loaded:

```bash
./scripts/manage.sh check
./scripts/manage.sh createsuperuser
```

- Clear corrupted sessions (rare, but fixes 500s caused by bad session data):

```bash
./scripts/clear_sessions.sh
```

## Notes

- If `/checkout/` errors with “You did not provide an API key”, ensure `STRIPE_SECRET_KEY` is set.
- If port 8000 is busy: `lsof -nP -iTCP:8000 -sTCP:LISTEN` then `kill <PID>`.
