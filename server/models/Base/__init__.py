from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from server import db, String
import uuid
from sqlalchemy_serializer import SerializerMixin


class BaseModel(db.Model, SerializerMixin):
    __abstract__ = True
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    created_on: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated_on: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
