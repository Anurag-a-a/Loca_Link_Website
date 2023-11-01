from flask import Flask, render_template, Blueprint, session
from flask import redirect
from flask import url_for
from flask import request

from model.comment import *
from model.post import *
from model.user import *
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'team20'
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if is_null_login(username, password):
            login_message = "Please input username and password. "
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
        if is_null_signup(username, password, email):
            login_message = "Please input username, password and email. "
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


@user_blueprint.route('/like/<int:postId>')
def like(postId):
    username = session.get("username")
    if not username:
        return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    user_id = get_user_id_by_username(username)
    try:
        add_like(user_id, postId)
        add_likeNum(postId)
        return jsonify({'status': 'success', 'message': 'Post liked successfully'}), 200
    except:
        return jsonify({'status': 'failed', 'message': 'An error occurred while liking the post'}), 500



@user_blueprint.route('/createComment/<int:postId>', methods=["GET", 'POST'])
def createComment(postId):
    if request.method == "POST":
        username = session.get("username")
        if not username:
            return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

        user_id = get_user_id_by_username(username)
        content = request.form.get('content')
        try:
            add_comment(content, user_id, postId)
            return jsonify({'status': 'success', 'message': 'Comment successfully'}), 200
        except:
            return jsonify({'status': 'failed', 'message': 'An error occurred while commenting'}), 500


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