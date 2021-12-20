from flask import Blueprint

from application.auth import utils as auth_utils
from application.application_config.project_auth import project_auth
from application.shared.utils import set_token_expired, get_or_create_token, get_token_from_request, generate_user_id, \
    json_message, json_token, json_message_with_token, get_request_form_property

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    [email, password, username] = get_request_form_property('email', 'password', 'username')
    user_id = generate_user_id()

    auth_utils.validate_register_properties(email, password, username)

    auth_utils.create_user(user_id, email, password, username)
    token = auth_utils.insert_into_tokens(user_id)

    return json_message_with_token('User success added', token)


@auth_bp.route('/login', methods=['POST'])
def login():
    [email, password] = get_request_form_property('email', 'password')

    user = auth_utils.get_user_by_email(email)
    auth_utils.validate_login_properties(user, email, password)

    token = get_or_create_token(user['id'])

    return json_token(token)


@auth_bp.route('/logout', methods=['POST'])
@project_auth.login_required
def logout():
    token = get_token_from_request()

    set_token_expired(token)

    return json_message('Success logout')
