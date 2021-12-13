import os

from flask import Flask, request

from application import db
from application.auth import auth
from application.profile import profile
from application.users import users


def page_not_found(e):
    return f'Error 404! "URL: {request.base_url}, Method: {request.method}" Not Found! Try another one URL or method.', 404


def invalid_method(e):
    return f'Error 405! "Method: {request.method}" for "URL: {request.base_url}" Not Allowed! Try another method', 405


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True
    )

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'application.sqlite'),
    )

    if test_config is None:
        app.config['JSON_AS_ASCII'] = False
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, invalid_method)

    db.init_app(app)

    app.register_blueprint(auth.auth_bp)

    app.register_blueprint(profile.profile_bp)

    app.register_blueprint(users.users_bp)

    return app
