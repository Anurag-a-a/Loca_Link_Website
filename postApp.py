from flask import Blueprint, jsonify, Flask, request, render_template, session, redirect
from model.community import *
from model.post import *
from model.user import *

app = Flask(__name__)
post_blueprint = Blueprint('post', __name__)


@post_blueprint.route("/create/<int:communityId>", methods=["GET", 'POST'])
def createPost(communityId):
    if request.method == 'POST':
        username = session.get("username")
        user_id = get_user_id_by_username(username)
        title=request.form.get("title")
        content=request.form.get("content")

        if exist_post(title):
            createPost_message = "Title has been used. "
            return render_template('createPost.html', message=createPost_message)
        else:
            add_post(user_id, communityId, title, content)
            return redirect("/community/{}/posts".format(communityId))
    return render_template('createPost.html',communityId=communityId)


# post list of community
@post_blueprint.route('/community/<int:community_id>/posts', methods=['GET'])
def get_posts_by_community(community_id):
    posts = get_postList_in_community(community_id)
    return render_template('PostList.html',posts=posts,community_id=community_id)



# @post_blueprint.route('/delete_post/<int:post_id>', methods=['POST'])
# def delete_post(post_id):
#     # Get the post by its ID
#     post = next((p for p in posts if p['id'] == post_id), None)
#     if post:
#         # Delete the post if the user_id matches (you may need to add authentication)
#         if post['user_id'] == 1:  # Replace 1 with the user's ID who can delete posts
#             posts.remove(post)
#
#     return 'Post deleted successfully'  # You might redirect to another page after deletion
