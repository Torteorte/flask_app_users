import os
from flask import Flask

from application import db
from application.auth import auth
from application.config import SECRET_KEY
from application.profile import profile
from application.users import users
from .error_handlers.error_handlers import page_not_found, invalid_method, bad_request_edit, bad_request_auth


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True
    )

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
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
    app.register_error_handler(400, bad_request_edit)
    app.register_error_handler(400, bad_request_auth)

    db.init_app(app)

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(profile.profile_bp)
    app.register_blueprint(users.users_bp)

    return app


start_app = create_app()
