from flask import Blueprint, jsonify, request, flash

from application.db.db import get_db
from .utils import get_profile_by_token, check_edit_properties, delete_user, update_user
from application.helpers.helpers import auth


profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile_bp.route('/', methods=['GET'])
@auth.login_required
def get_profile():
    token = request.headers['Authorization'].split(' ')[1]
    profile = get_profile_by_token(token)

    return jsonify(
        id=profile['userId'],
        username=profile['username'],
        email=profile['email'],
        about=profile['about'],
        token=profile['token']
    )


@profile_bp.route('/edit', methods=['PUT'])
@auth.login_required
def edit_profile():
    username = request.form['username']
    email = request.form['email']
    about = request.form['about']

    db = get_db()
    error = check_edit_properties(username, email, about)

    if error is None:
        token = request.headers['Authorization'].split(' ')[1]
        profile = get_profile_by_token(token)

        try:
            update_user(username, email, about, profile)
            return f"User information changed successfully"

        except db.IntegrityError:
            error = f'Email "{email}" is already taken.'

    flash(error)
    return f"{error}"


@profile_bp.route('/delete', methods=['DELETE'])
@auth.login_required
def delete_profile():
    token = request.headers['Authorization'].split(' ')[1]
    profile = get_profile_by_token(token)

    delete_user(profile)
    return f"User {profile['username']} success deleted."
