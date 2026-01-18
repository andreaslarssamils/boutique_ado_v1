.PHONY: dev run migrate loaddata check shell clear-sessions

# Convenience wrapper around scripts/manage.sh

dev:
	./scripts/dev.sh

run:
	./scripts/manage.sh runserver

migrate:
	./scripts/manage.sh migrate

loaddata:
	./scripts/manage.sh loaddata categories && ./scripts/manage.sh loaddata products

check:
	./scripts/manage.sh check

shell:
	./scripts/manage.sh shell

clear-sessions:
	./scripts/clear_sessions.sh
