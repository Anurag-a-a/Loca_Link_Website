from flask import Blueprint, jsonify, Flask, request, render_template, session, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename

import os
from model.community import *
from model.post import *
from model.user import *
from model.comment import *
from model.like import *
from model.event import *
from model.interested import *

app = Flask(__name__)
event_blueprint = Blueprint('event', __name__)


def check_session():
    username = session.get("username")
    communityName = session.get("location")

    if not username:
        return False, jsonify({'status': 'failed', 'message': 'Please log in firstly'}), 401

    return True, (username, communityName)


@event_blueprint.route("/<int:id>", methods=["POST", "GET"])
def show_event(id):
    user_check, user_data = check_session()

    if not user_check:
        return user_data
    username, communityName = user_data

    event = get_event_by_id(id)
    communityList = get_communityList()[:]
    userId = get_user_id_by_username(username)['id']
    ifInterested = if_interested(userId, id)

    if request.method == "POST":
        action = request.form.get('action')

        # if action == 'comment':
        #     content = request.form.get('content')
        #     add_comment(content, id, username)

        if action == 'interested':
            if ifInterested:
                interestedId = get_interested(userId, id)['id']
                delete_interested(interestedId)
                delete_interestedNum(id)
            else:
                add_interested(userId, id)
                add_interestedNum(id)

        return redirect(url_for('event.show_event', id=id))

    return render_template('singleEvent.html', event=event, communityList=communityList,
                           ifInterested=ifInterested, eventId=id)