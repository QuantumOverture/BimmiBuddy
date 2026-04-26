from controllers.user_controller import user_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(user_router)