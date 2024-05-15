import os
from flask import Flask, abort, session, request, redirect, current_app
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, String, Enum as SQLEnum, TEXT, Boolean
from dotenv import load_dotenv
from urllib.parse import quote_plus
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import logging

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

flask_bcrypt = Bcrypt(app)
db.init_app(app)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

from server.models import (
    Users as UserModel,
    Students as StudentModel,
    Entry_Logs as EntryLogModel,
)
from server.routes import *

CORS(app)


def create_root_user():
    print("________initiating server root user____________")
    root_user = os.getenv("ROOT_USER")
    root_password = os.getenv("ROOT_PASSWORD")
    if root_password and root_user:
        root_user = UserModel(root_user, root_password, True)
        db.session.add(root_user)
        db.session.commit()
    else:
        print("There is no default user set")


with app.app_context():
    db.create_all()

    count = UserModel.query.count()
    if count == 0:
        create_root_user()
