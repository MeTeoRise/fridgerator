PROJECT_NAME := fridgerator

build:
	docker build . -t $(PROJECT_NAME)

start:
	docker compose up -d

stop:
	docker compose down