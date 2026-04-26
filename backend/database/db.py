from dotenv import load_dotenv
load_dotenv(override=True)
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Uuid, DateTime, func
from datetime import datetime
import uuid

engine = create_async_engine(
    f"postgresql+asyncpg://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?ssl=require",
    echo=True,
    future=True,
)


class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def to_dict(self) -> dict:
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }