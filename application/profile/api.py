from flask import Blueprint, jsonify
import json

from application.profile import utils as profile_utils
from application.shared.utils import request_token
from application.application_config.verify_token import auth_token

profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile_bp.route('/', methods=['GET'])
@auth_token.login_required
def get_profile():
    token = request_token()
    profile = profile_utils.get_profile_by_token(token)

    return jsonify(
        id=profile['userId'],
        username=profile['username'],
        email=profile['email'],
        about=profile['about'],
        token=profile['token']
    )


@profile_bp.route('/edit', methods=['PUT'])
@auth_token.login_required
def edit_profile():
    username, email, about = profile_utils.get_profile_property()

    profile_utils.check_edit_properties(username, email, about)

    token = request_token()
    profile = profile_utils.get_profile_by_token(token)

    profile_utils.update_user(username, email, about, profile)

    return json.dumps({
        'text': "User information changed successfully"
    })


@profile_bp.route('/delete', methods=['DELETE'])
@auth_token.login_required
def delete_profile():
    token = request_token()
    profile = profile_utils.get_profile_by_token(token)

    profile_utils.delete_user(profile)

    return json.dumps({
        'text': f"User {profile['username']} success deleted."
    })
