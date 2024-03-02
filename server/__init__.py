import os
from flask import Flask, abort, session, request, redirect, current_app
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, String, Enum as SQLEnum, TEXT
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

db_uri = (
    f"{os.getenv('DB_DIALECT')}://"
    f"{os.getenv('DB_USERNAME')}:{quote_plus(os.getenv('DB_PASSWORD'))}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SECRET_KEY"] = os.getenv("JWT_TOKEN", "default_secret")


db.init_app(app)

from server.models import *
from server.routes import *

with app.app_context():
    db.create_all()
