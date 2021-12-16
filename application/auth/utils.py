from werkzeug.security import generate_password_hash, check_password_hash

from application.db.db import get_db
from application.utils.utils import create_token, create_token_expiration, get_token_for_check


def insert_into_users(user_id, username, password, email):
    db = get_db()

    db.execute(
        "INSERT INTO users (id, username, password, email) VALUES (?, ?, ?, ?)",
        [user_id, username, generate_password_hash(password), email]
    )
    db.commit()


def insert_into_tokens(user_id):
    db = get_db()
    token = create_token()
    token_expiration = create_token_expiration()

    db.execute(
        "INSERT INTO tokens (userId, token, tokenExpiration) VALUES (?, ?, ?)",
        [user_id, token, token_expiration]
    )
    db.commit()

    return token


def get_user_by_email(email):
    db = get_db()

    return db.execute(
        'SELECT * FROM users WHERE email = ?',
        [email]
    ).fetchone()


def check_register_properties(username, password, email):
    fields = {'Username': username, 'Email': email, 'Password': password}

    for field in fields.keys():

        if not fields[field]:
            return f'{field} can`t be empty.'

    return None


def check_login_properties(user, email, password):

    if user is None:
        return f'No user with email: "{email}".'

    elif not check_password_hash(user['password'], password):
        return f'Incorrect email or password.'

    return None


def check_logout_properties(token):

    if not token:
        return f'Token can`t be empty.'

    token_for_check = get_token_for_check(token)

    if token_for_check is None:
        return f'Invalid token.'

    return None
