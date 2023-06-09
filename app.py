from bottle import run, post, request, route, abort,  template, static_file, BaseTemplate
import bottle
import secrets
from enum import Enum
import string
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
from typing import List
app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url

server = WSGIServer(("0.0.0.0", 9988), app)


@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@route('/static/js/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root='static/js')

@route('/static/fonts/<filename:re:.*\.ttc>')
def send_ttc_font(filename):
    return static_file(filename, root='static/fonts')

@route('/static/fonts/<filename:re:.*\.otf>')
def send_otf_font(filename):
    return static_file(filename, root='static/fonts')


class CharacterType(Enum):
    ALPHANUMERIC = ''.join(string.ascii_letters + string.digits)
    DIGITS =  string.digits
    LETTERS = string.ascii_letters
    MIXED = string.ascii_letters + string.punctuation + string.digits

class PasswordGenerator:
    def password(password_length, character_type):
        return f'{"".join([secrets.choice(character_type.value)  for _ in range(password_length) ])}'

@route('/')
def index():
    return template('index.tpl')

@post('/send')
def send_password():
    data = request.forms
    data_items = list(data.values())
   #list(data)[0]
    print(data[0])


server.serve_forever()

