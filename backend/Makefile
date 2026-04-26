migrate:
	alembic -c './database/alembic.ini' revision --autogenerate -m '$(message)' 
	alembic -c './database/alembic.ini' upgrade head

server:
	uv run fastapi dev

.PHONY: migrate