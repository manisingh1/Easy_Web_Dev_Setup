.PHONY: up down prod debug

prod:
	docker-compose down --volumes || true
	docker-compose -f docker-compose-prod.yml build
	docker-compose -f docker-compose-prod.yml up

debug:
	docker-compose down --volumes || true
	docker-compose -f docker-compose-debug.yml build
	docker-compose -f docker-compose-debug.yml up

test:
	docker-compose down --volumes || true
	docker-compose -f docker-compose.test.yml up -d redis
	docker-compose -f docker-compose.test.yml build
	docker-compose -f docker-compose.test.yml run test-web pytest

test-debug:
	docker-compose down --volumes || true
	docker-compose -f docker-compose-test-debug.yml build
	docker-compose -f docker-compose-test-debug.yml up

down:
	docker-compose down --volumes
