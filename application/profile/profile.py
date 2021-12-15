from flask import Blueprint, g, jsonify

from .utils import post_edit_profile, delete_user
from application.auth.auth import login_required

profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')


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
