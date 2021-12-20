from flask import Blueprint, jsonify

from application.profile import utils as profile_utils
from application.application_config.project_auth import project_auth
from application.shared.utils import get_token_from_request, json_message, get_request_form_property

profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile_bp.route('/', methods=['GET'])
@project_auth.login_required
def get_profile():
    token = get_token_from_request()
    profile = profile_utils.get_profile_by_token(token)

    return jsonify(
        id=profile['userId'],
        username=profile['username'],
        email=profile['email'],
        about=profile['about'],
        token=profile['token']
    )


@profile_bp.route('/edit', methods=['PUT'])
@project_auth.login_required
def edit_profile():
    [username, email, about] = get_request_form_property('username', 'email', 'about')

    profile_utils.validate_edit_properties(username, email, about)

    token = get_token_from_request()
    profile = profile_utils.get_profile_by_token(token)

    profile_utils.update_user(username, email, about, profile)

    return json_message("User information changed successfully")


@profile_bp.route('/delete', methods=['DELETE'])
@project_auth.login_required
def delete_profile():
    token = get_token_from_request()
    profile = profile_utils.get_profile_by_token(token)

    profile_utils.delete_user(profile)

    return json_message(f"User {profile['username']} success deleted.")
