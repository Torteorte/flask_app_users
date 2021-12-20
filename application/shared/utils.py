import json
import secrets
from flask import request
from datetime import datetime, timedelta

from application.db.helpers import get_db


def generate_random_string():
    return str(secrets.token_hex(16))


def generate_user_id():
    return generate_random_string()


def generate_token():
    return generate_random_string()


def create_token_expiration():
    now_time = datetime.utcnow()
    return now_time + timedelta(minutes=30)


def get_or_create_token(user_id):
    token = get_not_expired_token_by_user_id(user_id)

    if token:
        return token['token']
    else:
        return create_user_token(user_id)


def get_not_expired_token_by_user_id(user_id):
    db = get_db()
    expiration_time = datetime.utcnow() + timedelta(seconds=60)

    return db.execute(
        'SELECT token, tokenExpiration FROM tokens WHERE userId = ? and tokenExpiration > ?',
        [user_id, expiration_time]
    ).fetchone()


def create_user_token(user_id):
    token = generate_token()
    token_expiration = create_token_expiration()

    run_sql(
        "UPDATE tokens SET token = ?, tokenExpiration = ? WHERE userId = ?",
        [token, token_expiration, user_id],
    )

    return token


def set_token_expired(token):
    token_expiration = datetime.utcnow() - timedelta(seconds=1)

    run_sql(
        "UPDATE tokens SET tokenExpiration = ? WHERE token = ?",
        [token_expiration, token]
    )


def check_token_expiration(token):
    token_expiration = get_token_expiration(token)

    if date_type(*token_expiration) < datetime.utcnow():
        return None
    return token


def get_token(token):
    db = get_db()

    return db.execute(
        'SELECT token FROM tokens WHERE token = ?', [token]
    ).fetchone()


def get_token_expiration(token):
    db = get_db()

    return db.execute(
        'SELECT tokenExpiration FROM tokens WHERE token = ?',
        [token],
    ).fetchone()


def date_type(item):
    return datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f')


def get_token_from_request():
    return request.headers['Authorization'].split(' ')[1]


def json_message(text):
    return json.dumps({
        'text': text
    })


def json_token(token):
    return json.dumps({
        'token': token
    })


def json_message_with_token(text, token):
    return json.dumps({
        'text': text,
        'token': token
    })


def get_request_form_property(*args):
    return [request.form.get(arg) for arg in args]


def run_sql(command, args, get_item=None, db=None):
    if db is None:
        db = get_db()

    action = db.execute(
        command,
        args
    )

    if get_item:
        return action.fetchone()

    return db.commit()
