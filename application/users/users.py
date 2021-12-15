from flask import Blueprint, jsonify

from .utils import get_user, get_users, get_tokens
from application.helpers.helpers import auth


users_bp = Blueprint('users', __name__, url_prefix='/api/users')


# Не ругай, это для моего удобства. Такое нельзя оставлять в обычном проекте.
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


@users_bp.route('/<int:userid>', methods=['GET'])
@auth.login_required
def get_user_by_id(userid):
    user = get_user(userid)

    if user:
        return jsonify({**user})
    else:
        return f"User with id '{userid}' is not found"
