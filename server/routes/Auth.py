from functools import wraps
import jwt
from flask import request, Flask
from flask import current_app
import models

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return {
                "message": "Authentication token is missing",
                "data": None,
                "error": "Unauthorized",
            }, 401

        try:
            data = jwt.decode(
                token, current_app.config["SECRET KEY"], algorithms=["HS256"]
            )
            current_user = models.Users().get_by_id(data["user_id"])
            if current_user is None:
                return {
                    "message": "Invalid Authetication token",
                    "data": None,
                    "error": "Unauthorized",
                }, 401

        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e),
            }, 500

        return func(current_user, *args, **kwargs)

    return decorated


# def validate_email_password(email, password):
#     if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#         return "Invalid format"
#     if not password or len(password) < 8:
#         return "Password must be atleast of 8 characters"

#     return True
