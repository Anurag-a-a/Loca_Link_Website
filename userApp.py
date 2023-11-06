from flask import Flask, render_template, Blueprint, session
from flask import redirect
from flask import url_for
from flask import request
from model.comment import *
from model.post import *
from model.user import *
from flask import jsonify
import re  # Import regular expression module

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
            session['username'] = username

            return render_template('refresh_and_redirect.html')
        else:
            login_message = "Please input correctly. "
            return render_template('login.html', message=login_message)
    return render_template('login.html')




@user_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        session.pop('user_id', None)
        session.clear()
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')

        if not all([username, password, confirm_password, email]):
            login_message = "Please fill in all fields."
            return render_template('signup.html', message=login_message)

        # Username validation
        if not re.match("^[a-zA-Z0-9]+$", username) or username.isdigit() or not username[0].isalpha():
            login_message = "Invalid username. Username should only contain letters and numbers, and should start with a letter."
            return render_template('signup.html', message=login_message)

        # Email validation
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            login_message = "Invalid email format."
            return render_template('signup.html', message=login_message)

        # Password validation
        if len(password) < 8 or not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            login_message = "Invalid password. Password should be at least 8 characters long and include numbers, alphabets, and special characters."
            return render_template('signup.html', message=login_message)

        if password != confirm_password:
            login_message = "Passwords do not match."
            return render_template('signup.html', message=login_message)

        if exist_user(username):
            login_message = "Username has been used."
            return render_template('signup.html', message=login_message)
        else:
            # Implement secure password storage (hashing) before storing in the database
            # Add the user to the database with hashed password
            add_user(username, password, email)  # Replace this with your secure database storage function

            return render_template('home.html', username=username)
    
    return render_template('signup.html')


@user_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    session.clear()
    return redirect(url_for('user.user_login'))

# @user_blueprint.route('/about-us')
# def about_us_page():
#     return render_template('about_page.html')


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

@user_blueprint.route("/profile")
def profile():
    username = session.get("username")
    if not username:
        return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    return render_template('EditProfile.html',username=username)

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