from flask_httpauth import HTTPTokenAuth

from application.utils.utils import get_token_for_check, check_token_expiration


auth_token = HTTPTokenAuth(scheme='Bearer')


@auth_token.verify_token
def verify_token(token):
    token_for_check = get_token_for_check(token)

    if token_for_check:
        return check_token_expiration(token_for_check[0])
