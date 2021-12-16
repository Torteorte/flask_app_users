import secrets
from datetime import datetime, timedelta
from application.db.db import get_db


def create_token():
    return str(secrets.token_hex(16))


def create_token_expiration():
    now_time = datetime.utcnow()
    return now_time + timedelta(seconds=1800)


def get_or_create_token(user_id):
    token = get_token_from_table(user_id)

    if token:
        return token['token']
    else:
        return create_user_token(user_id)


def get_token_from_table(user_id):
    db = get_db()
    expiration_time = datetime.utcnow() + timedelta(seconds=60)

    return db.execute(
        'SELECT token, tokenExpiration FROM tokens WHERE userId = ? and tokenExpiration > ?', [user_id, expiration_time]
    ).fetchone()


def create_user_token(user_id):
    db = get_db()
    token = create_token()
    token_expiration = create_token_expiration()

    db.execute(
        "UPDATE tokens SET token = ?, tokenExpiration = ? WHERE userId = ?",
        [token, token_expiration, user_id],
    )
    db.commit()

    return token


def set_token_expired(token):
    token_expiration = datetime.utcnow() - timedelta(seconds=1)
    db = get_db()

    db.execute(
        "UPDATE tokens SET tokenExpiration = ? WHERE token = ?",
        [token_expiration, token],
    )
    db.commit()


def check_token_expiration(token):
    token_expiration = get_table_token_expiration(token)

    if date_type(*token_expiration) < datetime.utcnow():
        return None
    return token


def get_token_for_check(token):
    db = get_db()

    return db.execute(
        'SELECT token FROM tokens WHERE token = ?', [token]
    ).fetchone()


def get_table_token_expiration(token):
    db = get_db()

    return db.execute(
        'SELECT tokenExpiration FROM tokens WHERE token = ?',
        [token],
    ).fetchone()


def date_type(item):
    return datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f')
