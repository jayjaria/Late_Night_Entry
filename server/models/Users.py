from .Base import BaseModel
from server import mapped_column, Mapped, String, Column, SQLEnum, TEXT
from enum import Enum


class Roles(Enum):
    USER = "user"
    ADMIN = "admin"


class Users(BaseModel):
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )
    password: Mapped[str] = mapped_column(TEXT)
    role = Column(SQLEnum(Roles), default=Roles.USER)
