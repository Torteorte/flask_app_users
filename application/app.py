from flask import Flask

from application.application_config import config as config
from application.application_config.commands import app_register_commands
from application.application_config.blueprints import app_register_blueprints
from application.application_config.error_handlers import app_register_error_handler


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=config.DATABASE,
        FLASK_ENV=config.FLASK_ENV,
        SECRET_KEY=config.SECRET_KEY
    )

    app_register_blueprints(app)
    app_register_error_handler(app)
    app_register_commands(app)

    return app
