from flask import Blueprint, jsonify, Flask, request, render_template, session, redirect,send_from_directory
from werkzeug.utils import secure_filename

import os
from model.community import *
from model.post import *
from model.user import *
from model.comment import *

app = Flask(__name__)
post_blueprint = Blueprint('post', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_session():
    username = session.get("username")
    communityName = session.get("location")
   
    if not username:
        return False, jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    return True, (username, communityName)

#Route for Creating the posts
@post_blueprint.route("/createPost", methods=["GET", 'POST'])
def createPost():
    if request.method == 'POST':
        user_check, user_data = check_session()
   
        if not user_check:
            return user_data
        username, communityName = user_data
        user_id = get_user_id_by_username(username)['id']
       
        communityId = get_community_id_by_communityName(communityName)['id']
       
        file_path = 'en.txt'  # Path to the curse word dictionary
       
        title = request.form.get("title")
        #checking if curse words are present in the Title
        result_title = auto_moderator(file_path, title)
        if result_title:
            return """
            <script>
                alert("Title contains a curse word. Please choose another title.");
                window.location.href = '/post/createPost';  // Redirect back to the createPost page
            </script>
            """

        content = request.form.get("content")
        #checking if curse words are present in the string
        result_content = auto_moderator(file_path, content)
        if result_content:
            return """
            <script>
                alert("Content contains a curse word. Please enter different content.");
                window.location.href = '/post/createPost';  // Redirect back to the createPost page
            </script>
            """
        # Check if an image file is provided
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '' and allowed_file(image.filename):
                # Securely save the uploaded image

                filename = secure_filename(image.filename)
                image.save(os.path.join('uploads/', filename))
                image_path = os.path.join('../uploads/', filename)
            else:
                # Handle the case where the file is not allowed or not provided
                image_path = None
        else:
            image_path = None
       
        if exist_post(title):
            createPost_message = "Title has been used. "
            return """
            <script>
                alert("Title has been used.");
                window.location.href = '/post/createPost';  // Redirect back to the createPost page
            </script>
            """
        else:
            add_post(user_id, communityId, title, content, image_path)
            return redirect("/community/{}".format(communityId))
   
    username = session.get("username")
    communityName = session.get("location")

    if not username:
        return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    return render_template('/createPost.html',communityName = communityName)

#Getting a specific posts from all posts
@post_blueprint.route('/community/<int:community_id>/posts', methods=['GET'])
def get_posts_by_community(community_id):
    user_check, user_data = check_session()
   
    if not user_check:
        return user_data
    username, communityName = user_data
   
    posts = get_postList_in_community(community_id)
    return render_template('PostList.html',posts=posts,community_id=community_id)

#Curse word logic
def auto_moderator(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            words = [word.strip().lower() for word in file.read().split(',')]
            search_string_lower = search_string.lower()
            for word in words:
           
                if word in search_string_lower:
                    return True
        return False

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

@post_blueprint.route("/deletePost/<int:id>", methods=["POST"])
def deletePost(id):
    if request.method == 'POST':
        user_check, user_data = check_session()
        if not user_check:
            return user_data
        username, communityName = user_data
   
        post = delete_post_by_id(id)
        if post:
            return jsonify({'success': True, 'message': 'Post deleted successfully'})
        else:
            return jsonify({'success': False, 'message': 'Failed to delete post'})

@post_blueprint.route("/<int:id>", methods=["GET"])
def show_post(id):
    if request.method == 'GET':
        user_check, user_data = check_session()
   
        if not user_check:
            return user_data
        username, communityName = user_data
   
        post = get_post_by_id(id)
        communityList = get_communityList()[:]
        comments = get_comments_by_postId(id)

        return render_template('singlePost.html', post=post, communityList=communityList,
                               comments=comments)
   
@post_blueprint.route("/usersPosts", methods=["GET"])
def usersPosts():
    if request.method == 'GET':
        user_check, user_data = check_session()
   
        if not user_check:
            return user_data
        username, communityName = user_data
        id = session.get("user_id")

        post = get_usersPosts(id)

        return render_template('usersPosts.html', posts=post)


