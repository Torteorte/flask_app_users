from application.db.helpers import close_db
from application.db.command import init_db_command


def app_register_command_init_db(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
