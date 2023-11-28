from flask import Flask, render_template, Blueprint, session
from flask import request
from model.community import *
from model.post import *
from model.user import *
from flask import jsonify
from collections import defaultdict
app = Flask(__name__)
community_blueprint = Blueprint('community', __name__)


#Create Community Route 
@community_blueprint.route("/create", methods=["GET", 'POST'])
def createCommunity():
    if request.method == 'POST':
        communityName = request.form.get('name')
        username = request.form.get('username')
        user_id = get_user_id_by_username(username)
        # print(type(communityName), type(username), type(user_id))
        if exist_community(communityName):
            createCommunity_message = "Community name has been used. "
            return render_template('createCommunity.html', message=createCommunity_message)
        else:
            add_community(communityName, user_id)
            return render_template('home.html', username=username)
    return render_template('createCommunity.html')

def check_session():
    username = session.get("username")
    communityName = session.get("location")
    
    if not username:
        return False, jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    return True, (username, communityName)

#Route for loading community Page
@community_blueprint.route("/<int:id>")
def community(id):
    user_check, user_data = check_session()
    
    if not user_check:
        return user_data
    username, communityName = user_data
    communityList = get_communityList()[:]
    community = get_community_by_id(id)
    posts = get_postList_in_community(id)[:]

    return render_template('CommunityPage.html',communityList=communityList,
                           username=username,community=community,posts=posts)


#Route for loading all posts from the database from all communities
@community_blueprint.route("/topPosts")
def topPosts():
    user_check, user_data = check_session()
    
    if not user_check:
        return user_data
    username, communityName = user_data
    
    communityList = get_communityList()[:]
    all_posts = []
    for community in communityList:
        posts = get_postList_in_community(community['id'])[:]
        all_posts.extend(posts)

    return render_template('topPosts.html', communityList=communityList,
                           username=username, posts=all_posts)

@community_blueprint.route("/createEvent")
def createEvent():
    user_check, user_data = check_session()
    
    if not user_check:
        return user_data
    username, communityName = user_data
    return render_template('createEvent.html',username=username,communityName = communityName )
