from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jay@9352*Mysql@localhost/late_entries'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress Flask-SQLAlchemy modification tracking

db = SQLAlchemy(app)

# Defining LateEntry Model
class LateEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), nullable=True)
    entry_time = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return "Late Entry System"

@app.route('/late_entries', methods=['POST'])  #This is a route decorator that tells Flask that the function immediately followiing it should be called(here late_entry()) when a Post request is made to the '/late_entry' URL
def late_entry():
    data = request.get_json()   #This line retrieves JSON data from the body of the incoming HTTP request and store it in the variable 'data' as a Python Dictionary.
    
    roll_number = data.get('roll_number')

    if not roll_number:
        return jsonify({'error':'Roll number is required'}),400  #Jsonify returns data from Flask routes in a JSON-formatted string that can be easily consumed by a Javascript applications.
    
    late_entry = LateEntry(roll_number = roll_number)  #This creates a new instance of the LateEntry model
    db.session.add(late_entry)
    db.session.commit()

    return jsonify({'message':'Late Entry recorded successfully'}), 201
