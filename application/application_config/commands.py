from application.application_config.db import app_register_command_init_db


def app_register_commands(app):
    app_register_command_init_db(app)
