import os
import logging
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi_clerk_auth import HTTPAuthorizationCredentials
from svix.webhooks import Webhook, WebhookVerificationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import User
from database.db import get_session

LOGGER = logging.getLogger(__name__)
user_router = APIRouter()
CLERK_WEBHOOK_CREATE = os.getenv("CLERK_SIGNING_SECRET_CREATE")
CLERK_WEBHOOK_DELETE = os.getenv("CLERK_SIGNING_SECRET_DELETE")


@user_router.post("/user/create", tags=["users"])
async def read_users(request: Request, session: AsyncSession = Depends(get_session)):
    payload = await request.body()
    headers = {
        "svix-id": request.headers.get("svix-id"),
        "svix-timestamp": request.headers.get("svix-timestamp"),
        "svix-signature": request.headers.get("svix-signature"),
    }

    try:
        webhook = Webhook(CLERK_WEBHOOK_CREATE)
        event = webhook.verify(payload, headers)
    except WebhookVerificationError:
        raise HTTPException("Invalid webhook verification payload.")

    LOGGER.info(event["type"])
    if "user.created" != event["type"]:
        raise HTTPException(f"Unsupported in user creation: {event["type"]}")

    data = event["data"]
    async with session:
        async with session.begin():
            new_user = User(clerk_id=data["id"], first_name=data["first_name"])
            session.add(new_user)
        await session.refresh(new_user)

    return {"successful": True, "data": new_user.to_dict()}


@user_router.post("/user/delete", tags=["users"])
async def read_users(request: Request, session: AsyncSession = Depends(get_session)):
    payload = await request.body()
    headers = {
        "svix-id": request.headers.get("svix-id"),
        "svix-timestamp": request.headers.get("svix-timestamp"),
        "svix-signature": request.headers.get("svix-signature"),
    }

    try:
        webhook = Webhook(CLERK_WEBHOOK_DELETE)
        event = webhook.verify(payload, headers)
    except WebhookVerificationError:
        raise HTTPException("Invalid webhook verification payload.")

    LOGGER.info(event["type"])
    if "user.deleted" != event["type"]:
        raise HTTPException(f"Unsupported in user deletion: {event["type"]}")

    data = event["data"]
    user_dict = None
    async with session:
        async with session.begin():
            statment = select(User).where(User.clerk_id == data["id"])
            user = (await session.execute(statment)).scalar_one_or_none()
            if user:
                user_dict = user.to_dict()
                await session.delete(user)
            else:
                LOGGER.error(f"Failed to find user: {data['id']}")
                
    return {"successful": user_dict != None, "data": user_dict}
