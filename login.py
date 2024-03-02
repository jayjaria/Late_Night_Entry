from flask import Flask, request
from server import jsonify
from Users import Users


app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("usernamae")
    password = data.get("password")

    if not username or password:
        return jsonify({"message": "Username and Password are required"}), 400

    user = Users.query.filter_by(username=username, password=password).first()
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return (
            jsonify({"message", "Invalid email or password"}),
            400,
        )  # or create a new user/account


if __name__ == "__main__":
    app.run(debug=True)
