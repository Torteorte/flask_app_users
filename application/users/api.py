from flask import Blueprint, jsonify

from application.shared.utils import json_message
from .utils import get_user_by_id, get_users, get_tokens
from application.application_config.auth import project_auth

users_bp = Blueprint('users', __name__, url_prefix='/api/users')


# ONLY FOR DEVELOPMENT
@users_bp.route('/tokens', methods=['GET'])
@project_auth.login_required
def get_all_tokens():
    list_of_tokens = [{**token} for token in get_tokens()]

    return jsonify(tokens=list_of_tokens)


@users_bp.route('/', methods=['GET'])
@project_auth.login_required
def get_all_users():
    list_of_users = [{**user} for user in get_users()]

    return jsonify(users=list_of_users)


@users_bp.route('/<user_id>', methods=['GET'])
@project_auth.login_required
def get_current_user(user_id):
    user = get_user_by_id(user_id)

    if user:
        return jsonify({**user})
    else:
        return json_message(f"User with id '{user_id}' is not found")
