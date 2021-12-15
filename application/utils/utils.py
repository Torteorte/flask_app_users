import secrets
from datetime import datetime, timedelta
from application.db.db import get_db


def get_token(user_id):
    db = get_db()
    now_time = datetime.utcnow()

    token_table = db.execute(
        'SELECT token, tokenExpiration FROM tokens WHERE userId = ?', [user_id]
    ).fetchone()

    if token_table['token'] and token_table['tokenExpiration'] and \
            convert_to_date(token_table['tokenExpiration']) > now_time + timedelta(seconds=60):
        return token_table['token']
    else:
        token = str(secrets.token_hex(16))
        token_expiration = now_time + timedelta(seconds=1800)
        db.execute(
            "UPDATE tokens SET token = ?, tokenExpiration = ? WHERE userId = ?",
            [token, token_expiration, user_id],
        )
        db.commit()
        return get_token(user_id)


def out_token(token):
    token_expiration = datetime.utcnow() - timedelta(seconds=1)
    db = get_db()

    db.execute(
        "UPDATE tokens SET tokenExpiration = ? WHERE token = ?",
        [token_expiration, token],
    )
    db.commit()
    return f'Success logout'


def check_token_expiration(token):
    token_expiration = get_table_token_expiration(token)

    if convert_to_date(*token_expiration) < datetime.utcnow():
        return None
    return token


def get_table_tokens():
    db = get_db()

    return db.execute(
        'SELECT token FROM tokens',
    ).fetchall()


def get_table_token_expiration(token):
    db = get_db()

    return db.execute(
        'SELECT tokenExpiration FROM tokens WHERE token = ?',
        [token],
    ).fetchone()


def convert_to_date(item):
    return datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f')
