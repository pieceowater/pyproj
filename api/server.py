# api/server.py
from flask import Flask, request
from cfg import ConfigVars as conf_var

from .db import db, models
from .tools import get_token, stdout

app: Flask = Flask(conf_var.service_name)

db.connect()

# db.drop_tables([models.User, models.Post])
# db.create_tables([models.User, models.Post])


@app.route('/health')
@stdout(unprotected=True)
def health():
    return f'{conf_var.service_name} app is running!', 200


@app.route('/user/<username>')
@stdout
def user_profile(username):
    return f'User Profile: {username}', 200


@app.route('/hello')
@stdout
def hello():
    name = request.args.get('name')
    return f'Hello, {name}!', 200


@app.route('/greet', methods=['POST'])
@stdout
def greet():
    data = request.get_json()
    name = data['name']
    return f'Greetings, {name}!', 200


@app.route('/protected')
@stdout
def protected():
    return {'message': 'This is a protected route!'}, 200


@app.route('/login')
@stdout(unprotected=True)
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = get_token(identity=auth.username)

        print("Generated token:", token)
        return {'token': token}, 200

    return {'message': 'Could not verify!'}, 401
