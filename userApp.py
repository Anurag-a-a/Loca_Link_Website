from flask import Flask, render_template, Blueprint, session
from flask import redirect
from flask import url_for
from flask import request
from model.user import *
from flask import jsonify

app = Flask(__name__)
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if is_null(username, password):
            login_message = "Wrong username or password. "
            return render_template('login.html', message=login_message)
        elif is_existed(username, password):

            user_id = get_user_id_by_username(username)
            session['user_id'] = user_id

            return render_template('home.html', username=username)
        else:
            login_message = "Please input correctly. "
            return render_template('login.html', message=login_message)
    return render_template('login.html')


@user_blueprint.route("/signup", methods=["GET", 'POST'])
def signup():
    if request.method == 'POST':
        session.pop('user_id', None)
        session.clear()
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if is_null(username, password, email):
            login_message = "Wrong username or password or email. "
            return render_template('signup.html', message=login_message)
        if exist_user(username):
            login_message = "Username has been used. "
            return render_template('signup.html', message=login_message)
        else:
            add_user(request.form['username'], request.form['password'], request.form['email'])
            return render_template('home.html', username=username)
    return render_template('signup.html')



@user_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    session.clear()
    return redirect(url_for('user.user_login'))



# @user_blueprint.route('/')
# def index():
#     return render_template('login0.html')
#
# @user_blueprint.route('/login', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = {
#             'username': username,
#             'password': password
#         }
#         return jsonify(user), 200