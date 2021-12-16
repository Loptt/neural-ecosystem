import os

from flask import (
    Flask, render_template
)
from ..ecosystem import Ecosystem


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    ecosystem = Ecosystem()

    @app.route('/')
    def root():
        return render_template('base.html')

    return app
