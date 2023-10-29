from flask import Flask, render_template, Blueprint, session
from flask import redirect
from flask import url_for
from flask import request
from model.community import *
from model.user import *
from flask import jsonify

app = Flask(__name__)
community_blueprint = Blueprint('community', __name__)


@community_blueprint.route("/create", methods=["GET", 'POST'])
def createCommunity():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        user_id = get_user_id_by_username(username)
        if exist_community(name):
            createCommunity_message = "Community name has been used. "
            return render_template('home.html', message=createCommunity_message)
        else:
            add_community(request.form['username'], user_id)
            return render_template('home.html', username=username)
    return render_template('createCommunity.html')