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
        communityName = request.form.get("communityName")
        communityId = get_community_id_by_communityName(communityName)['id']
        title = request.form.get("title")
        content = request.form.get("content")

        if exist_post(title):
            createPost_message = "Title has been used. "
            return render_template('createPost.html', message=createPost_message)
        else:
            add_post(user_id, communityId, title, content)
            return redirect("/community/{}".format(communityId))
    return render_template('createPost.html')


#Getting a specific posts from all posts
@post_blueprint.route('/community/<int:community_id>/posts', methods=['GET'])
def get_posts_by_community(community_id):
    posts = get_postList_in_community(community_id)
    return render_template('PostList.html',posts=posts,community_id=community_id)


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