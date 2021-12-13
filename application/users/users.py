from flask import (
    Blueprint, jsonify
)

from application.utils.utils import get_user, get_users

users_bp = Blueprint('users', __name__, url_prefix='/api/users')


@users_bp.route('/', methods=['GET'])
def get_all_users():
    data_all = []
    users = get_users()

    for user in users:
        data_all.append({**user})

    return jsonify(users=data_all)


@users_bp.route('/<int:userid>', methods=['GET'])
def get_user_by_id(userid):
    user = get_user(userid)

    if user:
        return jsonify({**user})
    else:
        return f"User with id '{userid}' is not found"
