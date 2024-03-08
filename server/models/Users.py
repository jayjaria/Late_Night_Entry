from .Base import BaseModel
from server import (
    mapped_column,
    Mapped,
    String,
    Column,
    SQLEnum,
    TEXT,
    Boolean,
    db,
)
from enum import Enum
from datetime import datetime
from server import flask_bcrypt


class Roles(Enum):
    USER = "user"
    ADMIN = "admin"


class Users(BaseModel):
    serialize_rules = ("-entry_log",)
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )
    password: Mapped[str] = mapped_column(TEXT, nullable=False)
    is_admin = mapped_column(Boolean, default=False)
    entry_log = db.relationship("EntryLogs", backref="user")

    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )
        self.is_admin = is_admin

    def __repr__(self):
        return f"username: {self.username}, password: {self.password}, id: {self.id}, role:{self.is_admin}"
