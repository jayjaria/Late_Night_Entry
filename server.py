from flask import Flask, request, render_template, redirect, url_for, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.get("/hello")
def hello_world():
    # /hello?para1=2
    para1=request.args.get("para1")
    if(para1):
        print({"para1":para1})
    return "<ul><li>JAI</li><li>JITEND</li><li>ABC</li></ul>"

# request params
@app.get("/hello/<name>")
def hello_world_from_query(name):
    return {"name":name}

#request body
# Request query params
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:jay@9352*Mysql@localhost/late_entries'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress Flask-SQLAlchemy modification tracking
#
# db = SQLAlchemy(app)
#
# # Defining LateEntry Model
# class LateEntry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     roll_number = db.Column(db.String(20), nullable=True)
#     entry_time = db.Column(db.DateTime, default=datetime.utcnow)
#
# @app.route('/')
# def index():
#     return "Late Entry System"
#
# @app.route('/late_entries', methods=['POST'])  #This is a route decorator that tells Flask that the function immediately followiing it should be called(here late_entry()) when a Post request is made to the '/late_entry' URL
# def late_entry():
#     data = request.get_json()   #This line retrieves JSON data from the body of the incoming HTTP request and store it in the variable 'data' as a Python Dictionary.
#
#     roll_number = data.get('roll_number')
#
#     if not roll_number:
#         return jsonify({'error':'Roll number is required'}),400  #Jsonify returns data from Flask routes in a JSON-formatted string that can be easily consumed by a Javascript applications.
#
#     late_entry = LateEntry(roll_number = roll_number)  #This creates a new instance of the LateEntry model
#     db.session.add(late_entry)
#     db.session.commit()
#
#     return jsonify({'message':'Late Entry recorded successfully'}), 201
#
# # 1. Gets the count of student in all time
# @app.route('/late_count/<roll_number>', methods=['GET'])
# def late_count(roll_number):  #We'll fetch roll number from the URL
#     count = LateEntry.query.filter(LateEntry.roll_number==roll_number).count()
#
#     return jsonify({'roll_number':roll_number, 'late_count':count})
#
#
# # 2. Checks if a Student was late on last night
# @app.route('/check_late_last_night/<roll_number>', methods=['GET'])
# def check_late_last_night(roll_number):
#     today = datetime.utcnow().date()
#     yesterday = today - timedelta(days=1)
#
#     late_last_night = LateEntry.query.filter(LateEntry.roll_number==roll_number, LateEntry.entry_time__date==yesterday).count()
#
#     was_late = late_last_night>0
#
#     return jsonify({'roll_number':roll_number,'was_late':was_late})
#
# # 3. Finds all late enrties in last night
# @app.route('/late_entries_last_night', methods=['GET'])
# def late_entries_last_night():
#     today = datetime.utcnow().date()
#     yesterday = today - timedelta(days=1)
#
#     late_entries = LateEntry.query.filter(LateEntry.entry_time__date==yesterday).all()
#
#     late_students = [{'roll_number':entry.roll_number,'entry_time':entry.entry_time} for entry in late_entries]
#     return jsonify({'late_entries_last_night':late_students})
#
#
# # We made 4 fields Roll number, Start Date, End Date, Late Count. There are 4 different variations of user searches
# @app.route('/find late students', methods=['GET'])
# def find_late_students():
#     start_date = request.args.get("Start_date")
#     end_date = request.args.ger("End_date")
#     roll_number = request.args.get("Roll_number")
#     late_count_threshold = int(request.args.get("Late_count", 0))
#
#     date_format = "%d-%m-%Y"
#     if not start_date:
#         return jsonify({'error':"Please enter a start date"}), 400
#
#     start_date = datetime.strptime(start_date, date_format)
#
#     # Roll Number given
#     if roll_number:
#         # Both start and end dates are given
#         if end_date:
#             end_date = datetime.strptime(end_date, date_format).date()
#             late_count = LateEntry.query.filter(LateEntry.roll_number == roll_number, LateEntry.entry_time.date().between(start_date, end_date)).count()
#             return jsonify({"roll_number": roll_number, "late_count":late_count})
#
#         # Only start date is given
#         else:
#             late_count = LateEntry.query.filter(LateEntry.roll_number == roll_number, LateEntry.entry_time.date() == start_date).count()
#             was_late = late_count>0
#
#             return jsonify({"roll_number":roll_number, "was_late":was_late})
#
#     # Roll Number is not given
#     else:
#         # Both start and end dates are given
#         if end_date:
#             end_date = datetime.strptime(end_date, date_format)
#
#             late_entries = LateEntry.query.filter(LateEntry.entry_time.date().between(start_date, end_date)).all()
#             late_count = {}
#             for entry in late_entries:
#                 if entry.roll_number not in late_count:
#                     late_count[entry.roll_number] = 1
#                 else:
#                     late_count[entry.roll_number]+=1
#
#             result = [roll_number for roll_number, count in late_count.items() if count > late_count_threshold]
#             return jsonify({"Late_students_list": result})
#
#         # Only start date is given
#         # Here Student is the record of all the Students
#         else:
#             late_entries = LateEntry.query.filter(LateEntry.entry_time.date() == start_date).all()
#
#             all_students = Student.query.all()
#             all_students_roll_number = [student.roll_number for student in all_students]
#
#             result=[]
#
#             was_late = any(entry.roll_number == roll_number for entry in late_entries)
#
#             result.append({'roll_number':roll_number, 'was_late':was_late})
#
#             return jsonify({"Late_status_of_all_students": result})
#
#
#
