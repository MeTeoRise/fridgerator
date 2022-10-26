PROJECT_NAME := fridgerator

build:
	docker build . -t $(PROJECT_NAME)

run:
	docker-compose up -d