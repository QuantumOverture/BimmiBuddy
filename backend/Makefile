migrate:
	alembic -c './database/alembic.ini' revision --autogenerate -m '$(message)' 
	alembic -c './database/alembic.ini' upgrade head


.PHONY: migrate