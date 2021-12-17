from application.auth import auth
from application.users import users
from application.profile import profile


def app_register_blueprints(app):
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(profile.profile_bp)
    app.register_blueprint(users.users_bp)
