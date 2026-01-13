DEPLOYMENT = deployment/

DOCKER_FILE := Dockerfile
DOCKER_COMPOSE:= docker-compose.yml
IMAGE := deployment-mock-service

run-docker:
	docker compose -f $(DEPLOYMENT)$(DOCKER_COMPOSE) down
	docker rmi -f $(IMAGE) || true
	docker image prune -f
	docker compose -f $(DEPLOYMENT)$(DOCKER_COMPOSE) build --no-cache
	docker compose -f $(DEPLOYMENT)$(DOCKER_COMPOSE) up
	docker ps
