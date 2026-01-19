#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def _load_dotenv_if_present() -> None:
    """Load KEY=VALUE pairs from a local .env file into os.environ.

    Keeps existing environment variables intact and ignores comments/blank lines.
    This mirrors the local dev workflow used by scripts/manage.sh, but also
    supports running plain `python manage.py ...`.
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(base_dir, ".env")
    if not os.path.isfile(dotenv_path):
        return

    try:
        with open(dotenv_path, encoding="utf-8") as handle:
            for raw_line in handle:
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if not key:
                    continue
                os.environ.setdefault(key, value)
    except OSError:
        # If the .env file can't be read, fail silently so manage.py still works.
        return


def main():
    """Run administrative tasks."""
    _load_dotenv_if_present()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boutiqe_ado.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
