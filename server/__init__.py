import os
import sys
import threading

from flask import (
    Flask, render_template
)
from flask_socketio import SocketIO, send

sys.path.insert(0, './ecosystem')

from ecosystem import Ecosystem

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )
    socketio = SocketIO(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    ecosystem = Ecosystem(number_organisms=5, food_amount=3, step_size=0.01)
    t1 = threading.Thread(target=ecosystem.run)

    t1.start()

    @app.route('/')
    def root():
        return render_template('base.html')

    @socketio.on('message')
    def handle_message(data):
        send(str(ecosystem.json()))

    return app
