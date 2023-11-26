from flask import Blueprint, jsonify, Flask, request, render_template, session, redirect
from model.community import *
from model.post import *
from model.user import *
from model.comment import *

app = Flask(__name__)
post_blueprint = Blueprint('post', __name__)

#Route for Creating the posts
@post_blueprint.route("/createPost", methods=["GET", 'POST'])
def createPost():
    if request.method == 'POST':
        username = session.get("username")
        user_id = get_user_id_by_username(username)['id']
        print(user_id)
        communityName = request.form.get("communityName")
        print(communityName)
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

        if exist_post(title):
            createPost_message = "Title has been used. "
            return """
            <script>
                alert("Title has been used.");
                window.location.href = '/post/createPost';  // Redirect back to the createPost page
            </script>
            """
        else:
            add_post(user_id, communityId, title, content)
            return redirect("/community/{}".format(communityId))
    
    return render_template('/createPost.html')


#Getting a specific posts from all posts
@post_blueprint.route('/community/<int:community_id>/posts', methods=['GET'])
def get_posts_by_community(community_id):
    posts = get_postList_in_community(community_id)
    return render_template('PostList.html',posts=posts,community_id=community_id)

#Curse word logic
def auto_moderator(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split('\n')
            if any(word in search_string for word in words):
                return True
            else:
                return False

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

@post_blueprint.route("/<int:id>", methods=["GET"])
def show_post(id):
    if request.method == 'GET':
        username = session.get("username")
        if not username:
            return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

        post = get_post_by_id(id)
        communityList = get_communityList()[:]
        comments = get_comments_by_postId(id)

        return render_template('singlePost.html', post=post, communityList=communityList,
                               comments=comments)