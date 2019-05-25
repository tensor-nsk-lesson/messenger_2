# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, abort
import psycopg2
app = Flask(__name__)
'''
EXAMPLE
users = [
    {
        'name': 'A',
        'age': 19
    },
    {
        'name': 'B',
        'age': 21
    },
    {
        'name': 'C',
        'age': 31
    }
]

messages = [
    {
        'send': 'M',
        'to': 'B',
        'text': 'Привет!'
    },
    {
        'send': 'A',
        'to': 'C',
        'text': 'Как твои дела?'
    },
    {
        'send': 'C',
        'to': 'A',
        'text': 'Ого, спасибо.'
    },
]


@app.route("/")
@app.route("/index")
def hello():
    return "Hello World!"


@app.route("/users")
def get_users():
    return jsonify(users)


@app.route("/users", methods=['POST'])
def create_users():
    if not request.json or not 'age' in request.json or not 'name' in request.json:
        abort(400)
    users.append({
        'name': request.json['name'],
        'age': request.json['age']
    })
    return jsonify(users)


@app.route("/message")
def get_messages():
    return jsonify(messages)


@app.route("/message/<int:index>")
def get_message(index):
    return jsonify(messages[index])


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Такого наше API не умеет:)'}), 404


app.run(port=80)
'''

connect = psycopg2.connect("dbname=messenger_2 user=messneger_2 host=90.189.168.29 password=messenger_2")
cursor = connect.cursor()
cursor.execute()

@app.route("/signup", methods=['POST'])
def signup():

    return jsonify(messages)