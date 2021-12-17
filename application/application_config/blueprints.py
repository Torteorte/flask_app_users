from application.auth import api as auth_api
from application.users import api as users_api
from application.profile import api as profile_api


def app_register_blueprints(app):
    app.register_blueprint(auth_api.auth_bp)
    app.register_blueprint(profile_api.profile_bp)
    app.register_blueprint(users_api.users_bp)
