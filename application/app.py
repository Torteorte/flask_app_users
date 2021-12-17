import os
from flask import Flask

from application.db import db
from application import config as config
from .error_handlers.error_handlers import app_register_error_handler
from application.helpers.blueprints import app_register_blueprints
from application.helpers.make_dirs import app_make_dirs


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=config.SECRET_KEY,
        DATABASE=config.DATABASE,
        FLASK_ENV=config.FLASK_ENV
    )

    app_make_dirs()

    app_register_error_handler(app)
    db.init_app(app)
    app_register_blueprints(app)

    return app
