from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import mapped_column, Mapped

from database.db import Base

class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(255))