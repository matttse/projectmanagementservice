from service_application_package import create_app
from service_application_package.chat.chatroute import socketio
application = create_app()
socketio.init_app(application)

if __name__ == '__main__':
    socketio.run(application)
