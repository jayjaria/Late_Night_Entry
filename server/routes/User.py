from server import app, jsonify, request, db
from server.utils import token_required
from server.models import Users
from server.routes import validate_pass


@app.route("/users-info", methods=["GET"])
@token_required
def getUserInfo(user):
    try:
        users_info = Users.query.all()

        response_user_info = []
        for user_info in users_info:
            response = {}
            response["username"] = user_info.username
            response["role"] = user_info.is_admin
            response_user_info.append(response)

        return jsonify({"user_log": response_user_info})

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


@app.route("/delete-user", methods=["DELETE"])
@token_required
def deleteUser(user):
    try:
        username = request.args.get("username")

        if not username:
            return jsonify({"message": "Invalid request "}), 400

        usr = Users.query.filter_by(username=username).first()

        if not usr:
            return jsonify({"message": "No such user exists"}), 400

        db.session.delete(usr)
        db.session.commit()
        return jsonify({"message": "Success"})

    except Exception as error:
        return (
            jsonify({"message": "Internal server error", "error": str(error)}),
            500,
        )


@app.route("/add-user", methods=["POST"])
@token_required
def addUser(user):
    try:
        data = request.json

        username = data.get("username")
        password = data.get("password")
        is_admin = data.get("role")

        if not username or not password or not is_admin:
            return jsonify({"message": "Provide all the fields"})

        if is_admin.lower() == "user":
            is_admin = False
        elif is_admin.lower() == "admin":
            is_admin = True
        else:
            return jsonify({"message": "Provide a valid Role"})

        if validate_pass(password):
            if Users.query.filter_by(username=username).count() > 0:

                return jsonify({"message": "This user already exists"}), 400

            add_user = Users(username, password, is_admin)
            db.session.add(add_user)
            db.session.commit()
            return jsonify({"message": "Success"})

        return jsonify({"message": "Enter a Strong Password"})
    except Exception as error:
        return (
            jsonify({"message": "Internal server error", "error": str(error)}),
            500,
        )
