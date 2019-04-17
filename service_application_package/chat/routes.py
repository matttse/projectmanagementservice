from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, session)
from flask_login import current_user, login_required
from service_application_package.chat import myredis


chatroombp = Blueprint('chatroombp', __name__)


@chatroombp.route("/chat",methods=['GET'])
@login_required
def chat():
    if not request.args.get("room") is None:
        room = request.args.get("room")
    else:
        room = 'Public' # default public room
    session['room'] = room
    
    # search chat record
    record = myredis.lrange(room+'-record',0,myredis.llen(room+'-record'))
    record = [str(rec, encoding = "utf8") for rec in record]
    # search channel
    chatroom = myredis.lrange('chatroom',0,myredis.llen('chatroom'))
    chatroom = [str(chatr, encoding = "utf8") for chatr in chatroom]
    return render_template('chat.html', title='Chat', record=record, room=room, username=current_user.username, channel=chatroom)
