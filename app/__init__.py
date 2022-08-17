from flask import Flask
from flask_bootstrap import Bootstrap5

from .config import Config
from .auth import auth


def create_app():
    app = Flask(__name__)
    Bootstrap5(app)
    app.config.from_object(Config)
    app.register_blueprint(auth)
    return app
