from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send
from db import *
from auth import *
from contact import *
from chat import *
from profile import *
import redis
import secrets

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mod=None)

@app.route('/profile/<int:id_user>', methods=['GET'])
def profile(id_user):
    return jsonify(get_profile(id_user))

@app.route('/login', methods=['POST'])
def auth():
    user_number = request.json.get('user_number')
    password = request.json.get('password')
    result = authorization(user_number, password)
    if result.get(''):
        return jsonify(result)
    else:
        key = secrets.token_hex(10)
        print(key.__str__())
        r.set(key.__str__(), result.get('Id_user').__str__(), 7200)
    return jsonify({'session':key})

@app.route('/signup', methods=['POST'])
def register():
    user_number = request.json.get('user_number')
    user_name = request.json.get('user_name')
    password = request.json.get('password')
    return jsonify(signup(user_number, user_name, password))

@app.route("/contacts/<string:id_session>", methods=['POST'])
def create_contact(id_session):
    Id_user = r.get(id_session)
    id_user_cont = request.json.get('id_user_cont')
    return jsonify(create_cont(Id_user, id_user_cont))

@app.route('/contacts/<string:id_session>', methods=['GET'])
def get_cont(id_session):
    Id_user = r.get(id_session)
    return jsonify(get_cont(Id_user))

@app.route('/chat/<int:id_chat>/message/<int:id_message>', methods=['PUT'])
def delete_message(id_chat, id_message):
    id_user = r.get(request.json.get('id_session'))
    return jsonify(del_mes(id_chat, id_message, id_user, del_mes))

@app.route('/chat/<int:id_chat>', methods=['GET'])
def get_messages(id_chat):
    return jsonify(get_all_mes(id_chat))

#чат, который работает некорректно, но с использованием socketIO
@app.route('/chat_test/')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def show_mes(message):
    send(message, broadcast=True)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, threaded=True)
    socketio.run(app)
