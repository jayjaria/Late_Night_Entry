from .Base import BaseModel
from server import mapped_column, db


class EntryLogs(BaseModel):
    student_id = db.Column(
        db.String(255), db.ForeignKey("students.id"), nullable=False
    )

    created_by = db.Column(
        db.String(255), db.ForeignKey("users.id"), nullable=False
    )

    def __init__(self, student, user) -> None:
        self.student_id = student
        self.created_by = user
