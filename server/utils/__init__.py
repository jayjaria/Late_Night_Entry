from functools import wraps
import jwt
from jwt import ExpiredSignatureError
from server.models import Users
from flask import current_app, request
from server import jsonify


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[
                1
            ]  # Bearer token_value

        if not token:
            return {
                "message": "Authentication token is missing",
                "data": None,
                "error": "Unauthorized",
            }, 401

        try:
            data = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"],
                options={"verify_exp": True},
            )

            current_user = Users.query.filter_by(id=data["id"]).first()
            if current_user is None:
                return {
                    "message": "Invalid Authetication token",
                    "data": None,
                    "error": "Unauthorized",
                }, 401

        except ExpiredSignatureError:
            return (
                jsonify(
                    {
                        "message": "Token has Expired",
                        "data": None,
                        "error": "Token Expired",
                    }
                ),
                401,
            )

        return func(
            current_user.to_dict(rules=("-password",)), *args, **kwargs
        )

    return decorated
