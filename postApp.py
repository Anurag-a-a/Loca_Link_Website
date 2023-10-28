from flask import Flask, render_template, Blueprint, session
from flask import redirect
from flask import url_for
from flask import request
from model.community import *
from model.post import *
from model.user import *
from flask import jsonify

app = Flask(__name__)
post_blueprint = Blueprint('post', __name__)


@post_blueprint.route("/create", methods=["GET", 'POST'])
def createPost():
    if request.method == 'POST':
        username = request.form.get('username')
        user_id = get_user_id_by_username(username)
        communityName = request.form.get('communityName')
        community_id = get_community_id_by_communityName(communityName)
        title = request.form.get('title')
        content = request.form.get('content')

        if exist_post(title):
            createPost_message = "Title has been used. "
            return render_template('home.html', message=createPost_message)
        else:
            add_post(user_id, community_id, title, content)
            return render_template('home.html', username=username)
    return render_template('createPost.html')