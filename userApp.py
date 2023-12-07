from flask import Flask, render_template, Blueprint, session
from flask import redirect
from werkzeug.utils import secure_filename
from flask import url_for
from flask_bcrypt import Bcrypt
from flask import request
from model.comment import *
from model.community import *
from model.post import *
from model.user import *
from flask import jsonify
import re  # Import regular expression module
import os
import sys
app = Flask(__name__)
app.secret_key = 'team20'
user_blueprint = Blueprint('user', __name__)
bcrypt = Bcrypt(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#Route for Login Page
@user_blueprint.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if is_null_login(username, password):
            login_message = "Please input username and password."
            return render_template('login.html', message=login_message)
        print(username)
        user = is_existed(username)

        if user and bcrypt.check_password_hash(user['password'], password):
            # Passwords match, user is authenticated
            session['user_id'] = user['id']
            session['username'] = username
            session['location'] = user['location']

            return render_template('refresh_and_redirect.html')
        else:
            login_message = "Invalid username or password."
            return render_template('login.html', message=login_message)

    username = session.get("username")

    if username:
        return render_template('refresh_and_redirect.html')

    return render_template('login.html')



#Route for Signup Page
@user_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        session.pop('user_id', None)
        session.clear()
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        location = request.form.get("communityName")

        if not all([username, password, confirm_password, email,location]):
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
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')


        if exist_user(username):
            login_message = "Username has been used."
            return render_template('signup.html', message=login_message)
        else:
            # Implement secure password storage (hashing) before storing in the database
            # Add the user to the database with hashed password
            add_user(username, hashed_password, email,location)
            user = is_existed(username)
            session['user_id'] = user['id']
            session['username'] = username
            session['location'] = user['location']

            return render_template('refresh_and_redirect.html')
    
    communities =  get_communityList()
    community_names = [community['name'] for community in communities]

    return render_template('signup.html',communities=community_names)


#Route for logging out of the system
@user_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    session.clear()
    return redirect(url_for('user.user_login'))

def check_session():
    username = session.get("username")
    communityName = session.get("location")
    
    if not username:
        return False, jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    return True, (username, communityName)



#Route for fetching users details 
@user_blueprint.route("/profile")
def profile():
    user_check, user_data = check_session()
    
    if not user_check:
        return user_data
    username, communityName = user_data
    
    communityList = get_communityList()[:]
    profile = get_profile(username)
    return render_template('Profile.html', username=username, communityList=communityList,
                           email=profile['email'], location = profile['location'], desc = profile['description'],avatar = profile['avatar'],address = profile['address'],phone = profile['phone'])


@user_blueprint.route("/changePass", methods=["GET","POST"])
def changePass():
    user_check, user_data = check_session()
    
    if not user_check:
        return user_data
    username, communityName = user_data
    
    communityList = get_communityList()[:]
    profile = get_profile(username)

    if request.method == 'POST':
        ogPass = request.form.get('og-password')
        edit_password = request.form.get('edit-password')
        conf_password = request.form.get('conf-password')

        user = is_existed(username)

        if user and bcrypt.check_password_hash(user['password'], ogPass):
            # Passwords match, user is authenticated
            session['user_id'] = user['id']
            session['username'] = username
            session['location'] = user['location']

        if ogPass == edit_password:
            error_message = "New password must be different from the old password."
            return render_template('changePass.html', username=username, communityList=communityList, error_message=error_message)
        
        if edit_password != conf_password:
            error_message = "Password and confirm password must be same."
            return render_template('changePass.html', username=username, communityList=communityList, error_message=error_message)
        
        hashed_password = bcrypt.generate_password_hash(conf_password).decode('utf-8')
        edit_password = hashed_password

        updatePass(username, edit_password)
            
        return render_template('Profile.html',username=username,communityList=communityList,
                           email=profile['email'], location = profile['location'], desc = profile['description'],avatar = profile['avatar'],address = profile['address'],phone = profile['phone'])
    return render_template('changePass.html', username=username, communityList=communityList)

#Route for editing User Profile
@user_blueprint.route("/editProfile", methods=["GET","POST"])
def editProfile():
    user_check, user_data = check_session()
    
    if not user_check:
        return user_data
    username, communityName = user_data
    
    communityList = get_communityList()[:]
    profile = get_profile(username)

    if request.method == 'POST':
        email = request.form.get('edit-email')
        desc = request.form.get('edit-description')
        address = request.form.get('edit-address')
        phone = request.form.get('edit-phone')
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '' and allowed_file(image.filename):
                # Securely save the uploaded image

                filename = secure_filename(image.filename)
                image.save(os.path.join('uploads/', filename))
                image_path = os.path.join('../uploads/', filename)
            else:
                # Handle the case where the file is not allowed or not provided
                image_path = ''
        else:
            image_path = ''

        if email != profile['email'] or desc != profile['description'] or address != profile['address'] or phone != profile['phone']:
            updateDetails(username, email, desc, address, phone, image_path)
            profile = get_profile(username)
            return render_template('Profile.html', username=username, communityList=communityList,
                                   email=profile['email'], location=profile['location'],
                                   desc=desc, avatar=profile['avatar'], address=address, phone=phone)

        # If no field has changed, display a message or redirect to the profile page
        return render_template('EditProfile.html', username=username, communityList=communityList,
                               email=profile['email'], location=profile['location'],
                               desc=profile['description'], avatar=profile['avatar'],
                               address=profile['address'], phone=profile['phone'],
                               error_message="No changes were made.")
    
    return render_template('EditProfile.html', username=username, communityList=communityList,
                           email=profile['email'], location = profile['location'], desc = profile['description'],avatar = profile['avatar'],address = profile['address'],phone = profile['phone'])