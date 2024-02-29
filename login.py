from flask import Flask, url_for, request
from flask_login import LoginManager, UserMixin, login_user, redirect, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY']='my_secret_key'
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, user_id, username, password, is_admin=False):
        self.id = user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin

users = {
    'user1': User('1','u1','a'),
    'user2': User('2','u2','b'),
    'admin': User('3','Admin','Admin', is_admin=True)
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)  #Returns the user object

@app.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = users.get(username)
    pswd = user.password

    if user and pswd==password:
        login_user(user)
        return redirect(url_for('dashboard'))
    

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin:
        return 'You are on the Admin Dashboard'
    else:
        return 'You are on the User Dashboard'
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out Successfully'
if __name__=='__main__':
    app.run(debug=True)