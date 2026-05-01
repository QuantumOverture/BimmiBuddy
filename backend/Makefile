migrate:
	uv run alembic -c './database/alembic.ini' revision --autogenerate -m '$(message)' 
	uv run alembic -c './database/alembic.ini' upgrade head

server:
	uv run fastapi dev

.PHONY: migrate