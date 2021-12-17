from flask import Flask

from application.application_config import config as config
from application.application_config.create_db import create_db
from application.application_config.error_handlers import app_register_error_handler
from application.application_config.blueprints import app_register_blueprints


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=config.SECRET_KEY,
        DATABASE=config.DATABASE,
        FLASK_ENV=config.FLASK_ENV
    )

    create_db(app)
    app_register_blueprints(app)
    app_register_error_handler(app)

    return app
