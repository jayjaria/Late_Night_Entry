from server import app, jsonify


@app.route("/")
def hello_route():
    return jsonify({"hello": "late_night_app"})
