docker-compose-local:
	docker compose -f docker-compose.yaml up

aiflow-init:
	docker compose -f docker-compose.airflow.yaml up airflow-init

airflow:
	docker compose -f docker-compose.airflow.yaml up

prune:
	docker system prune --all
