from application.db.helpers import get_db
from application.shared.utils import run_sql


def get_user_by_id(userid):
    return run_sql(
        'SELECT id, username, about, email FROM users WHERE id = ?',
        [userid],
        True
    )


def get_users():
    return get_db().execute(
        'SELECT id, username, email, about FROM users'
    )


def get_tokens():
    return get_db().execute(
        'SELECT * FROM tokens'
    )
