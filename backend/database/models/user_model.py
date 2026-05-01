from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import mapped_column, Mapped

from database.db import Base


class User(Base):
    __tablename__ = "users"
    clerk_id: Mapped[str] = mapped_column(String(255), unique=True)
    first_name: Mapped[str] = mapped_column(String(255))
