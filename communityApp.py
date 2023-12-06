from flask import Flask, render_template, Blueprint, session,redirect,url_for
from flask import request
from werkzeug.utils import secure_filename
import os
from model.community import *
from model.comment import *
from model.event import *
from model.interested import *
from model.like import *
from model.post import *
from model.user import *
from flask import jsonify
from collections import defaultdict
import datetime
import re
app = Flask(__name__)
community_blueprint = Blueprint('community', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Create Community Route
@community_blueprint.route("/create", methods=["GET", 'POST'])
def createCommunity():
    if request.method == 'POST':
        communityName = request.form.get('name')
        username = request.form.get('username')
        user_id = get_user_id_by_username(username)
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
    posts = get_extended_post_list_in_community(id, username)

    posts.reverse()

    return render_template('CommunityPage.html', communityList=communityList,
                           username=username, community=community, posts=posts, id = id)


def get_extended_post_list_in_community(community_id, username):
    posts = get_postList_in_community(community_id)[:]
    user_id = get_user_id_by_username(username)['id']

    for post in posts:
        post['ifLiked'] = if_liked(user_id, post['id'])
        post['comments'] = get_comments_by_postId(post['id'])

    return posts
        
@community_blueprint.route('/toggleLike/<int:id>', methods=['POST'])
def toggle_like(id):
    # Check if the user has already liked the post
    user_check, user_data = check_session()
   
    if not user_check:
        return user_data
    username, communityName = user_data

    comm_id = get_community_id_by_communityName(communityName)
    userId = get_user_id_by_username(username)['id']

    if_liked_status = if_liked(userId, id)
    if if_liked_status:
        # If liked, unlike the post
        like_id = get_like(userId, id)['id']
        delete_like(like_id)
        delete_likeNum(id)
    else:
        # If not liked, like the post
        add_like(userId, id)
        add_likeNum(id)

    # You can return a JSON response or any other response as needed
    return redirect(url_for('community.community', id=comm_id['id']))

@community_blueprint.route('/addComment/<int:id>/<int:post_id>', methods=['POST'])
def addComment(id, post_id):
    user_check, user_data = check_session()
    if not user_check:
        return user_data

    username, communityName = user_data

    content = request.form.get('content')
    add_comment(content, post_id, username)

    return redirect(url_for('community.community', id=id))

#Route for loading all posts from the database from all communities
@community_blueprint.route("/topPosts")
def topPosts():
    user_check, user_data = check_session()
   
    if not user_check:
        return user_data
    username, communityName = user_data
   
    communityList = get_communityList()[:]
    all_posts = []
    user_community_id = get_community_id_by_communityName(communityName)  
    user_community_posts = get_postList_in_community(user_community_id['id'])
    all_posts.extend(user_community_posts)

    # Then, get posts from other communities
    for community in communityList:
        if community['id'] != user_community_id:
            posts = get_postList_in_community(community['id'])[:]
            all_posts.extend(posts)

    all_posts.reverse()

    return render_template('topPosts.html', communityList=communityList,
                           username=username, posts=all_posts)

#Route for loading all event from the database from all communities
@community_blueprint.route("/eventExplorer",methods=["POST", "GET"])
def eventExplorer():
    user_check, user_data = check_session()
   
    if not user_check:
        return user_data
    username, communityName = user_data

    userId = get_user_id_by_username(username)['id']
   
    communityList = get_communityList()[:]
    all_events = []

    user_community_id = get_community_id_by_communityName(communityName)
    user_community_events = get_eventList_in_community(user_community_id['id'])[:]
    all_events.extend(user_community_events)

    # Then, get events from other communities
    for community in communityList:
        if community['id'] != user_community_id['id']:
            events = get_eventList_in_community(community['id'])[:]
            all_events.extend(events)

    interestDict = {}
    for event in all_events:
        eventId = event['id']
        ifInterested = if_interested(userId,eventId)
        interestDict[eventId] = ifInterested

    if request.method == "POST":
        event_id = request.form.get('eventId')
        if_Interested = if_interested(userId,event_id)
        if if_Interested:
            interestedId = get_interested(userId, event_id)['id']
            delete_interested(interestedId)
            delete_interestedNum(event_id)
        else:
            add_interested(userId, event_id)
            add_interestedNum(event_id)

        return redirect(url_for('community.eventExplorer'))

    all_events.reverse()

    return render_template('eventExplorer.html', communityList=communityList,
                           username=username,all_events=all_events,interestDict=interestDict)

@community_blueprint.route("/usersEvents", methods=["GET"])
def usersEvents():
    if request.method == 'GET':
        user_check, user_data = check_session()
   
        if not user_check:
            return user_data
        username, communityName = user_data
        id = session.get("user_id")

        events = get_usersEvents(id)

        events.reverse()

        return render_template('usersEvents.html', events=events)
#Curse word logic
def auto_moderator(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            bad_words = [word.strip().lower() for word in file.read().split(',')]
            pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in bad_words) + r')\b', flags=re.IGNORECASE)
            if pattern.search(search_string):
                return True
        return False

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False

    #Route for Creating the events
@community_blueprint.route("/createEvent", methods=["GET", 'POST'])
def createEvent():
    if request.method == 'POST':
        user_check, user_data = check_session()
   
        if not user_check:
            return user_data
        username, communityName = user_data
        user_id = get_user_id_by_username(username)['id']
       
        communityId = get_community_id_by_communityName(communityName)['id']
       
        file_path = 'en.txt'  # Path to the curse word dictionary
       
        title = request.form.get("title")
        date = request.form.get("Date")
        eventDesc = request.form.get("description")
        regURL = request.form.get("registrationUrl")
        eventType = request.form.get("etype")
        print(title,date,eventDesc,regURL,eventType)
        #checking if curse words are present in the Title
        result_title = auto_moderator(file_path, title)
        if result_title:
            return """
            <script>
                alert("Title contains a curse word. Please choose another title.");
                window.location.href = '/community/createEvent';  // Redirect back to the createPost page
            </script>
            """

        #checking if curse words are present in the string
        result_content = auto_moderator(file_path, eventDesc)
        if result_content:
            return """
            <script>
                alert("Content contains a curse word. Please enter different content.");
                window.location.href = '/community/createEvent';  // Redirect back to the createPost page
            </script>
            """
        
        image_path = ''
        # Check if an image file is provided
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '' and allowed_file(image.filename):
                # Securely save the uploaded image
                print("here")
                filename = secure_filename(image.filename)
                image.save(os.path.join('uploads/', filename))
                image_path = os.path.join('../uploads/', filename)
            
       
        if exist_event(title):
            createPost_message = "Title has been used. "
            return """
            <script>
                alert("Title has been used.");
                window.location.href = '/community/createEvent';  // Redirect back to the createPost page
            </script>
            """
        else:
            add_event(user_id, communityId, title, date, eventDesc, regURL,eventType, image_path)
            return redirect("/community/eventExplorer")
   
    username = session.get("username")
    communityName = session.get("location")

    if not username:
        return jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    user_check, user_data = check_session()
   
    if not user_check:
        return user_data
    username, communityName = user_data
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Get the current date
    
    return render_template('/createEvent.html',username=username,communityName = communityName,current_date=current_date )
