from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from gevent import monkey
monkey.patch_all()
from flask import session
from flask_socketio import SocketIO, emit, join_room, leave_room
socketio = SocketIO()
from pmsapp import myredis
import json

socketio = Blueprint('chat', __name__)

socketio.route("/chat",methods=['GET'])
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

# socket chat
@socketio.on('connect', namespace='/chats')
def test_connect():
    print('Client connected')


@socketio.on('disconnect', namespace='/chats')
def test_disconnect():
    print('Client disconnected')


@socketio.on('join', namespace='/chats')
def on_join(data):
    username = session.get('username')
    room = session.get('room')
    join_room(room)
    myredis.sadd(room,username)# add to redis - online people
    parlist = list(myredis.smembers(room)) # get online people
    parlist = [str(p, encoding = "utf8") for p in parlist]
    rdata = {'username':username,'parlist':parlist}
    emit('join', rdata, room=room)

@socketio.on('leave', namespace='/chats')
def on_leave(data):
    username = session.get('username')
    room = session.get('room')
    leave_room(room)
    myredis.srem(room, username)# remove people
    parlist = list(myredis.smembers(room)) # get online people
    parlist = [str(p, encoding = "utf8") for p in parlist]
    rdata = {'username':username,'parlist':parlist}
    emit('leave', rdata, room=room)


@socketio.on('send', namespace='/chats')
def on_send(data):
    username = session.get('username')
    room = session.get('room')
    rdata = {'username':username,'message':data['data']['message'],'time':data['data']['time']}
    print(json.dumps(rdata))
    # use rpush , Insert from left to right
    myredis.rpush(room+"-record",json.dumps(rdata))#storage chat record to redis
    emit('message', rdata, room=room)


# create chatroom
@socketio.on('create', namespace='/chats')
def on_create(data):
    myredis.lpush('chatroom',data)#storage chat room to redis
    chatroom = myredis.lrange('chatroom',0,myredis.llen('chatroom'))
    chatroom = [str(chatr, encoding = "utf8") for chatr in chatroom]
    emit('create', chatroom, broadcast=True) #broadcast=True 