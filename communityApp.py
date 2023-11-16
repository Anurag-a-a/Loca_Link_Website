from flask import Flask, render_template, Blueprint, session
from flask import redirect
from flask import url_for
from flask import request
from model.community import *
from model.post import *
from model.user import *
from flask import jsonify
from collections import defaultdict
app = Flask(__name__)
community_blueprint = Blueprint('community', __name__)


@community_blueprint.route("/create", methods=["GET", 'POST'])
def createCommunity():
    if request.method == 'POST':
        communityName = request.form.get('name')
        username = request.form.get('username')
        user_id = get_user_id_by_username(username)
        print(type(communityName), type(username), type(user_id))
        if exist_community(communityName):
            createCommunity_message = "Community name has been used. "
            return render_template('createCommunity.html', message=createCommunity_message)
        else:
            add_community(communityName, user_id)
            return render_template('home.html', username=username)
    return render_template('createCommunity.html')


@community_blueprint.route("/<int:id>")
def community(id):
    username = session.get("username")
    if not username:
        return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    communityList = get_communityList()[:]
    community = get_community_by_id(id)
    posts = get_postList_in_community(id)[:]

    return render_template('CommunityPage.html',communityList=communityList,
                           username=username,community=community,posts=posts)

# @community_blueprint.route("/music")
# def music():
#     username = session.get("username")
#     if not username:
#         return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401
#
#     return render_template('MusicPage.html',username=username)
#
#
#
# @community_blueprint.route("/dance")
# def dance():
#     username = session.get("username")
#     if not username:
#         return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401
#
#     return render_template('DancePage.html',username=username)
#
# @community_blueprint.route("/sports")
# def sports():
#     username = session.get("username")
#     if not username:
#         return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401
#
#     return render_template('Sports.html',username=username)
# @community_blueprint.route("/arts")
# def arts():
#     username = session.get("username")
#     if not username:
#         return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401
#
#     return render_template('ArtsPage.html',username=username)

@community_blueprint.route("/topPosts")
def topPosts():
    username = session.get("username")
    if not username:
        return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    communityList = get_communityList()[:]
    all_posts = []
    print(communityList)
    # Fetch posts from all communities
    for community in communityList:
        print(community)
        posts = get_postList_in_community(community['id'])[:]
        all_posts.extend(posts)

    # Sort the combined posts based on a specific criterion (for example, by the number of likes)
    #all_posts.sort(key=lambda post: post['likes'], reverse=True)

    return render_template('topPosts.html', communityList=communityList,
                           username=username, posts=all_posts)

@community_blueprint.route("/post/<int:id>", methods=["GET"])
def show_post(id):
    if request.method == 'GET':
        username = session.get("username")
        if not username:
            return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401
        
        post = get_post_by_id(id)
        print(post)

        return render_template('post_template.html', post=post)