import secrets
from datetime import datetime, timedelta


def get_token(token, token_expiration):
    now_time = datetime.utcnow()
    if token and token_expiration and token_expiration > now_time + timedelta(seconds=60):
        return token
    else:
        token = secrets.token_hex(16)
        token_expiration = now_time + timedelta(seconds=1800)
        return [token, token_expiration]


def out_token():
    token_expiration = datetime.utcnow() - timedelta(seconds=1)
    return token_expiration


def check_token_authentication(user, token_expiration):
    if user is None and token_expiration < datetime.utcnow():
        return None
    return user