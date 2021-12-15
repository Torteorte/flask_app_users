from flask_httpauth import HTTPTokenAuth

from application.utils.utils import get_table_tokens, check_token_expiration


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    tokens = get_table_tokens()

    for token_table in tokens:
        if {token} == {*token_table}:
            return check_token_expiration(token)
