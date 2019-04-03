from service_application_package import create_app
from service_application_package.chat.chatroute import socketio
application = create_app()

if __name__ == '__main__':
	socketio.init_app(application)
	socketio.run(application, host='master.projectchat.rpwclh.use1.cache.amazonaws.com', port=5000)
	application.run(debug=True)