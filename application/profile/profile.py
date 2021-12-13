from flask import Blueprint, g, jsonify, request

from application.utils.utils import post_edit_profile, delete_user
from application.auth.auth import login_required

profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile_bp.errorhandler(400)
def bad_request_edit(e):
    if request.path.startswith('/api/profile/edit'):
        return f'Error 400 BAD REQUEST! Check username, email and about in form-data of request', 400


@profile_bp.route('/', methods=['GET'])
@login_required
def get_profile():
    return jsonify(
        id=g.user['id'],
        username=g.user['username'],
        email=g.user['email'],
        about=g.user['about']
    )


@profile_bp.route('/edit', methods=['POST'])
@login_required
def edit_profile():
    return post_edit_profile(g.user['id'])


@profile_bp.route('/delete', methods=['POST'])
@login_required
def delete_profile():
    return delete_user(g.user)
