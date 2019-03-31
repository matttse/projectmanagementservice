from pmsapp import application
from pmsapp.websocket_route import socketio
if __name__ == '__main__':
    # init socketio
    socketio.init_app(application)
    socketio.run(application,host='127.0.0.1', port=5000)
