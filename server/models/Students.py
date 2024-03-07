from .Base import BaseModel
from server import mapped_column, Mapped, String, db


class Students(BaseModel):
    roll_no: Mapped[str] = mapped_column(String(10), unique=True)
    name: Mapped[str] = mapped_column(
        String(50),
    )
    entry_log = db.relationship("EntryLogs", backref="student")
