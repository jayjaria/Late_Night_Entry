from server.models import Users
from flask import request, jsonify
from server.utils import token_required
import jwt
from server import app, flask_bcrypt
from flask_jwt_extended import get_jwt


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

    if user:
        token = jwt.encode(
            user.to_dict(rules=("-password", "-created_on", "-updated_on")),
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
    return jsonify(user.to_dict(rules=("-password",)))


@app.route("/logout", methods=["DELETE"])
@token_required(verify_type=False)
def logout():
    token = get_jwt()

    jti = token["jti"]
    ttype = token["type"]
    jwt.redis_blocklist.set(jti, "", ex=3600)  # expiration time in seconds
    return jsonify(msg=f"{ttype.capitalize()} token successfully revoked")
