from application.db.helpers import get_db


def get_user_by_id(userid):
    user = get_db().execute(
        'SELECT id, username, about, email FROM users WHERE id = ?',
        [userid]
    ).fetchone()

    return user


def get_users():
    users = get_db().execute(
        'SELECT id, username, email, about FROM users'
    ).fetchall()

    return users


def get_tokens():
    tokens = get_db().execute(
        'SELECT * FROM tokens'
    ).fetchall()

    return tokens
