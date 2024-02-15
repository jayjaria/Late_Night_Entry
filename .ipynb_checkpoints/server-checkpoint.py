from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jay@9352*Mysql@localhost/late_entries'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress Flask-SQLAlchemy modification tracking

db = SQLAlchemy(app)
