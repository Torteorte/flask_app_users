from flask import Blueprint, jsonify

from .utils import get_user_by_id, get_users, get_tokens
from application.helpers.helpers import auth


users_bp = Blueprint('users', __name__, url_prefix='/api/users')


# роут для удобства
@users_bp.route('/tokens', methods=['GET'])
@auth.login_required
def get_all_tokens():
    data_all = []
    tokens = get_tokens()

    for token in tokens:
        data_all.append({**token})

    return jsonify(tokens=data_all)


@users_bp.route('/', methods=['GET'])
@auth.login_required
def get_all_users():
    data_all = []
    users = get_users()

    for user in users:
        data_all.append({**user})

    return jsonify(users=data_all)


@users_bp.route('/<user_id>', methods=['GET'])
@auth.login_required
def get_user_by_id(user_id):
    user = get_user_by_id(user_id)

    if user:
        return jsonify({**user})
    else:
        return f"User with id '{user_id}' is not found"
