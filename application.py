from service_application_package import create_app
from service_application_package.chat.chatroute import socketio
application = create_app()

if __name__ == '__main__':
	socketio.init_app(application)
	socketio.run(application,host='0.0.0.0', port=49276)
