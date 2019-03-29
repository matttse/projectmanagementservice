from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from service_application_package.chat.forms import ChatForm

chat = Blueprint('chat', __name__)

@chat.route("/chat")
def chat():
    return render_template('chat.html', title='Chat')