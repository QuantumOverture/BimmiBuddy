from dotenv import load_dotenv

load_dotenv(override=True)

import os
import logging
from fastapi import FastAPI, Depends
from fastapi_clerk_auth import ClerkConfig, ClerkHTTPBearer

from controllers.user_controller import user_router

logging.basicConfig(level=logging.INFO)

# Setup auth
# clerk_config = ClerkConfig(jwks_url=f"https://{os.getenv('CLERK_API_URL')}/.well-known/jwks.json", leeway=5.0)
# clerk_auth_guard = ClerkHTTPBearer(config=clerk_config, add_state=True)

# app = FastAPI(dependencies=[Depends(clerk_auth_guard)])
app = FastAPI()

app.include_router(user_router)
