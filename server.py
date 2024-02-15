from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

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

# 1. Gets the count of student in all time
@app.route('/late_count/<roll_number>', methods=['GET'])
def late_count(roll_number):  #We'll fetch roll number from the URL
    count = LateEntry.query.filter(LateEntry.roll_number==roll_number).count()

    return jsonify({'roll_number':roll_number, 'late_count':count})


# 2. Checks if a Student was late on last night
@app.route('/check_late_last_night/<roll_number>', methods=['GET'])
def check_late_last_night(roll_number):
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)

    late_last_night = LateEntry.query.filter(LateEntry.roll_number==roll_number, LateEntry.entry_time__date==yesterday).count()

    was_late = late_last_night>0

    return jsonify({'roll_number':roll_number,'was_late':was_late})

# 3. Finds all late enrties in last night
@app.route('/late_entries_last_night', methods=['GET'])
def late_entries_last_night():
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)

    late_entries = LateEntry.query.filter(LateEntry.entry_time__date==yesterday).all()

    late_students = [{'roll_number':entry.roll_number,'entry_time':entry.entry_time} for entry in late_entries]
    return jsonify({'late_entries_last_night':late_students})



