from server import Users, request, jsonify, app
from server.utils import token_required
import jwt


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and Password are required"}), 400

    user = Users.query.filter_by(username=username, password=password).first()

    if user:
        token = jwt.encode(
            {"user_id": user.id, "role": user.role.value},
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return (
            jsonify({"message", "Invalid email or password"}),
            400,
        )  # or create a new user/account


@app.route("/", methods=["GET"])
@token_required
def dashboard(user):
    print(user)
    return jsonify({"hello": " "})
