from flask_socketio import SocketIO, send
from app import app

socketio = SocketIO(app)

@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)
