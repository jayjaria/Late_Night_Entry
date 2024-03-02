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

    def __repr__(self):
        return f"username: {self.username}, password: {self.password}, id: {self.id}, role:{self.role}"
