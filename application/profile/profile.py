from flask import Blueprint, g, jsonify

from .utils import post_edit_profile, delete_user
from application.db.db import get_db
# from application.auth.auth import login_required

profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')


@profile_bp.route('/', methods=['GET'])
def test_user_from_tokens():
    db = get_db()

    test_user_id = 'cd8197ece12c04a7aa77f5f87cd44eee'
    test_token = '55cf87724f665f4c907516fe11b9c056'
    token_table = db.execute(
        'SELECT * FROM tokens JOIN users WHERE tokens.userId = ?, token = ?', [test_user_id, test_token]
    ).fetchone()
    token_table = db.execute(
        'SELECT * FROM tokens WHERE token = ?', [test_user_id, test_token]
    ).fetchone()

    return f"{token_table['id']}"


# @profile_bp.route('/', methods=['GET'])
# @login_required
# def get_profile():
#     return jsonify(
#         id=g.user['id'],
#         username=g.user['username'],
#         email=g.user['email'],
#         about=g.user['about']
#     )


# @profile_bp.route('/edit', methods=['POST'])
# @login_required
# def edit_profile():
#     return post_edit_profile(g.user['id'])


# @profile_bp.route('/delete', methods=['POST'])
# @login_required
# def delete_profile():
#     return delete_user(g.user)
