.PHONY: all start stop


all: start

start:
	mkdir -p postgres_data
	docker compose up -d

restart_force:
	docker compose down -v
	docker compose up -d --force-recreate

stop:
	docker compose down