from werkzeug.security import generate_password_hash, check_password_hash
from flask import request

from application.application_config.errors_raiser import InvalidAPIUsage
from application.db.helpers import get_db
from application.shared.utils import generate_token, create_token_expiration


def get_user_property():
    return request.form.get('email'), request.form.get('password'), request.form.get('username')


def create_user(user_id, email, password, username):
    db = get_db()
    try:
        insert_into_users(user_id, email, password, username)

    except db.IntegrityError:
        raise InvalidAPIUsage(f"Email '{email}' is already registered.")


def insert_into_users(user_id, email, password, username):
    db = get_db()

    db.execute(
        "INSERT INTO users (id, username, password, email) VALUES (?, ?, ?, ?)",
        [user_id, username, generate_password_hash(password), email]
    )
    db.commit()


def insert_into_tokens(user_id):
    db = get_db()
    token = generate_token()
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


def check_register_properties(email, password, username):
    fields = {'Email': email, 'Password': password, 'Username': username}

    for field in fields.keys():

        if not fields[field]:
            raise InvalidAPIUsage(f"{field} can`t be empty.", status_code=400)


def check_login_properties(user, email, password):

    if user is None:
        raise InvalidAPIUsage(f"No user with email: '{email}''.")

    elif not check_password_hash(user['password'], password):
        raise InvalidAPIUsage("Incorrect email or password.")
