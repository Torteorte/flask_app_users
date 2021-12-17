import click
from flask.cli import with_appcontext

from application.db.helpers import init_db


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
