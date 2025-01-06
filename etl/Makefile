aiflow-init:
	docker compose -f docker-compose.airflow.yaml up airflow-init

airflow:
	docker compose -f docker-compose.airflow.yaml up

airflow-down:
	docker compose -f docker-compose.airflow.yaml down -v

prune:
	docker system prune --all
