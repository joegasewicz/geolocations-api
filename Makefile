DB_NAME=admin
DB_USERNAME=admin
DB_PASSWORD=admin

locations-api-server:
	pipenv run uvicorn main:app --reload


mongo-import-towns:
	mongoimport -d bn_database -c towns --file ./towns.json --authenticationDatabase $(DB_NAME) --username $(DB_USERNAME) --password $(DB_PASSWORD) --host localhost --port 27017
