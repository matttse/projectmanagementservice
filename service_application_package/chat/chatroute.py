from flask import session
from flask_socketio import SocketIO, emit, join_room, leave_room
from service_application_package.chat import myredis
socketio = SocketIO()

import json
# socket chat
@socketio.on('connect', namespace='/chats')
def test_connect():
    print('Client connected')

@socketio.on('connect_event', namespace='/chats')
def refresh_message(message):
    """ 服务端接受客户端发送的通信请求 """
    emit('server_response', {'data': message['data']})

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
