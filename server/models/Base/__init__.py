from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from server import db, String
import uuid


class BaseModel(db.Model):
    __abstract__ = True
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=str(uuid.uuid4())
    )
    created: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
