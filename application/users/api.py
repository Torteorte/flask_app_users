from flask import Blueprint, jsonify
import json

from .utils import get_user_by_id, get_users, get_tokens
from application.application_config.verify_token import auth_token


users_bp = Blueprint('users', __name__, url_prefix='/api/users')


# роут для удобства разработки
@users_bp.route('/tokens', methods=['GET'])
@auth_token.login_required
def get_all_tokens():
    list_of_tokens = [{**token} for token in get_tokens()]

    return jsonify(tokens=list_of_tokens)


@users_bp.route('/', methods=['GET'])
@auth_token.login_required
def get_all_users():
    list_of_users = [{**user} for user in get_users()]

    return jsonify(users=list_of_users)


@users_bp.route('/<user_id>', methods=['GET'])
@auth_token.login_required
def get_user_by_id(user_id):
    user = get_user_by_id(user_id)

    if user:
        return jsonify({**user})
    else:
        return json.dumps({
            'text': f"User with id '{user_id}' is not found"
        })
