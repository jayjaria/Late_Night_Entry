from server import app, request, jsonify, db
from server.models import EntryLogs
from server.models import Students
from server.utils import token_required


@app.route("/entry-log", methods=["POST"])
@token_required
def createEntryLog(user):
    try:
        print("user", user)
        data = request.json
        roll_no = data.get("rollNo")

        if not roll_no:
            return jsonify({"message": "Invalid request "}), 400

        student = Students.query.filter_by(roll_no=roll_no).first()

        if not student:
            return jsonify({"message": "Invalid roll number"}), 404

        entry_log = EntryLogs(student=student.id, user=user.get("id"))
        db.session.add(entry_log)
        db.session.commit()

        return jsonify(
            {"message": "Success", "log": entry_log.to_dict(only=("id",))}
        )
    except Exception as error:
        return (
            jsonify({"message": "Internal server error", "error": str(error)}),
            500,
        )
