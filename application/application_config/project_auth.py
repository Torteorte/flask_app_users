from flask_httpauth import HTTPTokenAuth

from application.shared.utils import get_token, check_token_expiration

project_auth = HTTPTokenAuth(scheme='Bearer')


@project_auth.verify_token
def verify_token(token):
    token_for_check = get_token(token)

    if token_for_check:
        return check_token_expiration(token_for_check[0])
