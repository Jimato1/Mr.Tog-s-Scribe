.PHONY: build up down logs shell clean

# Build the Docker image
build:
	docker compose build

# Start the bot in detached mode
up:
	docker compose up -d

# Stop the bot
down:
	docker compose down

# View logs
logs:
	docker compose logs -f

# Open a shell in the container
shell:
	docker compose exec discord-bot /bin/bash

# Remove containers, volumes, and built images
clean:
	docker compose down -v
	docker rmi discord-bot_discord-bot

# Local development setup
setup-dev:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "Development environment set up. Activate with 'source venv/bin/activate'"

# Update requirements.txt file
freeze:
	pip freeze > requirements.txt