from flask import Blueprint
import json

from application.auth import utils as auth_utils
from application.shared.utils import set_token_expired, get_or_create_token, request_token, generate_user_id

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    email, password, username = auth_utils.get_user_property()
    user_id = generate_user_id()

    auth_utils.check_register_properties(email, password, username)

    auth_utils.create_user(user_id, email, password, username)
    token = auth_utils.insert_into_tokens(user_id)

    return json.dumps({
        'text': 'User success added',
        'token': token
    })


@auth_bp.route('/login', methods=['POST'])
def login():
    email, password, username = auth_utils.get_user_property()

    user = auth_utils.get_user_by_email(email)
    auth_utils.check_login_properties(user, email, password)

    token = get_or_create_token(user['id'])

    return json.dumps({
        'token': token
    })


@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request_token()

    set_token_expired(token)

    return json.dumps({
        'text': 'Success logout'
    })
