from server import app, request, jsonify, db
from server.utils import token_required
from server.models import EntryLogs
from server.models import Students
from server.models import Users
from server.utils import token_required
from datetime import datetime, timedelta


@app.route("/entry-log", methods=["POST"])
@token_required
def createEntryLog(user):
    try:
        # print("user", user)
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


@app.route("/entry-log", methods=["GET"])
@token_required
def getEntryLog(user):
    try:
        today = datetime.now()
        yesterday = datetime(
            today.year, today.month, today.day, 22, 0, 0
        ) - timedelta(days=1)

        start_date = request.args.get("startDate", yesterday)
        end_date = request.args.get("endDate", today)
        batch_no = request.args.get("batchNo")
        date_format = "%Y-%m-%d"

        formatted_start_date = (
            start_date
            if isinstance(start_date, datetime)
            else datetime.strptime(start_date, date_format)
        )
        formatted_end_date = (
            end_date
            if isinstance(end_date, datetime)
            else datetime.strptime(end_date, date_format)
        )

        if not batch_no:
            entry_logs = EntryLogs.query.filter(
                EntryLogs.created_on.between(
                    formatted_start_date, formatted_end_date
                )
            )
        else:
            entry_logs = EntryLogs.query.join(Students).filter(
                Students.roll_no.like(f"{batch_no}%"),
                EntryLogs.created_on.between(
                    formatted_start_date, formatted_end_date
                ),
            )

        response_entry_logs = []
        for entry in entry_logs:
            response = {}
            response["rollNo"] = entry.student.roll_no
            response["studentName"] = entry.student.name
            response["createdBy"] = entry.user.username
            response["createdAt"] = entry.created_on
            response_entry_logs.append(response)

        return jsonify({"log": response_entry_logs})

    except ValueError as error:
        return (
            jsonify({"message": "Invalid input", "error": str(error)}),
            400,
        )

    except Exception as error:
        print(error)
        return (
            jsonify({"message": "Internal server error", "error": str(error)}),
            500,
        )
