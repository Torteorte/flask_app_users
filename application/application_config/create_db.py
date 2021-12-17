from application.db.command import init_db_command
from application.db.helpers import close_db


def create_db(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
