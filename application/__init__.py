import os

from flask import Flask

from application import db, auth, userpage, users


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

    db.init_app(app)

    app.register_blueprint(auth.bp)

    app.register_blueprint(userpage.bp)

    app.register_blueprint(users.bp)
    # app.add_url_rule('/', endpoint='index')

    return app
