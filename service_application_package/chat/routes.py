from flask import render_template, request, Blueprint
from service_application_package.models import Project

chat = Blueprint('chat', __name__)


@chat.route("/")
def chat():
    if not current_user.is_authenticated:
        return redirect(url_for('/login'))
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
