from flask import Blueprint, jsonify, request, flash
import json

from application.db.db import get_db
from application.utils.utils import request_token
from application.profile import utils as profile_utils
from application.helpers.helpers import auth_token


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
    username = request.form['username']
    email = request.form['email']
    about = request.form['about']

    db = get_db()
    error = profile_utils.check_edit_properties(username, email, about)

    if error is None:
        token = request_token()
        profile = profile_utils.get_profile_by_token(token)

        try:
            profile_utils.update_user(username, email, about, profile)
            return f"User information changed successfully"

        except db.IntegrityError:
            error = f'Email "{email}" is already taken.'

    flash(error)
    return json.dumps({
        'error': error
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
