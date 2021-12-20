from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from application.db.helpers import get_db
from application.application_config.exceptions import InvalidAPIUsage
from application.shared.utils import generate_token, create_token_expiration, run_sql


def get_user_property():
    return request.form.get('email'), request.form.get('password'), request.form.get('username')


def create_user(user_id, email, password, username):
    db = get_db()

    try:
        insert_into_users(user_id, email, password, username)
    except db.IntegrityError:
        raise InvalidAPIUsage(f"Email '{email}' is already registered.")


def insert_into_users(user_id, email, password, username):
    run_sql(
        "INSERT INTO users (id, username, password, email) VALUES (?, ?, ?, ?)",
        [user_id, username, generate_password_hash(password), email]
    )


def insert_into_tokens(user_id):
    token = generate_token()
    token_expiration = create_token_expiration()

    run_sql(
        "INSERT INTO tokens (userId, token, tokenExpiration) VALUES (?, ?, ?)",
        [user_id, token, token_expiration]
    )

    return token


def get_user_by_email(email):
    db = get_db()

    return db.execute(
        'SELECT * FROM users WHERE email = ?',
        [email]
    ).fetchone()


def validate_register_properties(email, password, username):
    fields = {'Email': email, 'Password': password, 'Username': username}

    for field in fields.keys():

        if not fields[field]:
            raise InvalidAPIUsage(f"{field} can`t be empty.", status_code=400)


def validate_login_properties(user, email, password):

    if user is None:
        raise InvalidAPIUsage(f"No user with email: '{email}'.")

    elif not check_password_hash(user['password'], password):
        raise InvalidAPIUsage("Incorrect email or password.")
