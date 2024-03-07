from server.models import Users
from flask import request, jsonify
from server.utils import token_required
import jwt
from server import app, flask_bcrypt, db
from datetime import datetime, timedelta, timezone
import os


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and Password are required"}), 400

    user = Users.query.filter_by(username=username).one()
    if user and not flask_bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Invalid password"}), 400

    payload = user.to_dict(rules=("-password", "-created_on", "-updated_on"))
    payload["exp"] = datetime.now(tz=timezone.utc) + timedelta(
        minutes=int(os.getenv("JWT_EXPIRY", 30))
    )
    if user:
        token = jwt.encode(
            payload,
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return (
            jsonify({"message": "Invalid email or password"}),
            400,
        )


@app.route("/", methods=["GET"])
@token_required
def dashboard(user):
    return jsonify(user)


@app.route("/logout", methods=["DELETE"])
@token_required
def logout():
    return jsonify({"message": "Logout"})


def validate_pass(password):
    special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    c = 0
    for char in password:
        if char in special_characters:
            c = 1
            break
    if c == 1 and len(password) > 8:
        return True
    else:
        return False


@app.route("/register", methods=["POST"])
@token_required
def register_user(user):
    register_user = {}

    # user should be admin
    if user.get("is_admin"):

        # request body=>{usernmae->string,password->string,is_admin->True/False}

        data = request.json
        username = data.get("username")
        password = data.get("password")
        is_admin = data.get("is_admin", False)

        if validate_pass(password):
            if Users.query.filter_by(username=username).count() > 0:
                print(Users.query.filter_by(username=username))
                return jsonify({"message": "This user already exists"}), 400

            register_user[username] = password
            # Adding it to Users table
            me = Users(username, password, is_admin)
            db.session.add(me)
            db.session.commit()

            return register_user
            # store in user table

            # return register_user
        else:
            return jsonify({"message": "Enter a Strong Password"})

    else:
        return jsonify({"message": "Unauthorized access"}), 401
