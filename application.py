import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = []
channels = []
messages = {}


@app.route('/')
def index():
    return render_template('index.html', channels=channels)

def message_received():
    print('Message received')

@socketio.on('submit display')
def new_display(data):
    name = data['display_name']
    old_name = data['old_display']
    channel = data['current_chan']
    print('Display name ' + name + ' submitted')
    if name in users:
        print('Display name ' + name + ' rejected')
        emit('display taken', {'error': 'This display name is already in use'}, callback=message_received())
    else:
        print('Display name ' + name + ' accepted')
        users.append(name)
        emit('display set', name, callback=message_received())
        emit('name changed', {'name': name, 'old_name': old_name}, room=channel, include_self=False)

@socketio.on('submit channel')
def new_channel(data):
    name = data['channel_name']
    print('Channel name ' + name + ' submitted')
    if name in channels:
        print('Channel name ' + name + ' rejected')
        emit('channel exists', {'error': 'This channel name already exists'}, callback=message_received())
    else:
        print('Channel name ' + name + ' accepted')
        channels.append(name)
        messages[name] = []
        emit('channel created', name, callback=message_received(), broadcast=True)

@socketio.on('join channel')
def join_channel(data):
    channel = data['channel']
    user = data['user']
    join_room(channel)
    if channel in channels:
        message_data = messages[channel]
        emit('get messages', message_data, callback=message_received())
    emit('user joined', {'user': user}, room=channel, include_self=False)

@socketio.on('leave channel')
def leave_channel(data):
    channel = data['channel']
    user = data['user']
    leave_room(channel)
    emit('user left', {'user': user}, room=channel)

@socketio.on('send message')
def send_message(data):
    message = data['message']
    channel = data['channel']
    user = data['user']
    timestamp = time.localtime()
    timestamp = time.strftime("%H:%M, %d %B", timestamp)  
    new_message = {
        'message': message,
        'user': user,
        'timestamp': timestamp
    }
    messages[channel].append(new_message)
    if len(messages[channel]) > 100:
        messages[channel].pop(0)
    emit('new message', new_message, room=channel)

@socketio.on('file upload')
def file_upload(data):
    emit('file received', data, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
