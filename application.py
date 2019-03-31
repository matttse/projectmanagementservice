from service_application_package import create_app
from service_application_package.chatroute import socketio
application = create_app()

if __name__ == '__main__':
	socketio.init_app(application)
	application.run(debug=True)