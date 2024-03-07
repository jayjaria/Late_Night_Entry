from .Base import BaseModel
from server import mapped_column, db
from server.models import Students, Users


class EntryLogs(BaseModel):
    student_id = db.column(
        db.String(255),
        db.ForeignKey("Students.id", nullable=False, unique=True),
    )

    # roll_no: Mapped[str] = mapped_column(String(10), unique=True)
    # created_by: Mapped[str] = mapped_column(String(30), unique=True)
