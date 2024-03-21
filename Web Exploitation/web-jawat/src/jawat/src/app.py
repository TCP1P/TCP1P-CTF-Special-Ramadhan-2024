import flask
from flask import Flask, render_template, request, url_for
import jwt
import os
import re

app = Flask(__name__)


# I'm not in any wordlist hehehe
JWT_SECRET = os.environ.get('JWT_SECRET') or 'secret'

JWT_ALG = 'HS256'
JWT_COOKIE = 'appdata'


@app.route('/')
def root():
    return render_template("index.html")


@app.route('/welcome', methods=['GET'])
def welcome():
    cookie = request.cookies.get(JWT_COOKIE)

    if not cookie:
        return f'Error: missing {JWT_COOKIE} cookie value'

    try:
        jwtData = jwt.decode(cookie, JWT_SECRET, algorithms=[JWT_ALG])
    except:
        return 'Error: unable to decode JWT cookie', 400

    user = jwtData['user']
    if not user:
        return 'Error: missing data field from decoded JWT', 400
    
    if user == "admin":
        user = os.environ.get('FLAG') or 'TCP1P{fake_flag}'
    
    return render_template("welcome.html", username=user)


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')

    if not username:
        return 'Error: username is required', 400

    username = str(username)

    if not re.match('^[a-z]+$', username):
        return 'Error: username must be only lowercase letters', 400

    if len(username) < 3:
        return 'Error: username must be at least 3 letters', 400

    if len(username) > 20:
        return 'Error: username must be no longer than 20 letters', 400
    if username == "admin":
        return 'Error: heem you are not real'
    
    jwtData = { 
        "user": username 
    }

    cookie = jwt.encode(jwtData, JWT_SECRET, algorithm=JWT_ALG)

    response = flask.make_response(f'hello {username}')
    response.set_cookie(JWT_COOKIE, cookie)

    response.headers['location'] = url_for('welcome')
    return response, 302

if __name__ == "__main__":
    app.run(debug=False)
