import os

from flask import Flask

from application import db
from application.auth import auth
from application.profile import profile
from application.users import users


def page_not_found(error):
    return f'Error 404! Bad request! Try another one URL or method.', 404


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='templates'
    )
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'application.sqlite'),
    )

    if test_config is None:
        app.config['JSON_AS_ASCII'] = False
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_error_handler(404, page_not_found)

    db.init_app(app)

    app.register_blueprint(auth.auth_bp)

    app.register_blueprint(profile.profile_bp)

    app.register_blueprint(users.users_bp)

    return app
