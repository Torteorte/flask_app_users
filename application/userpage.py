from flask import Blueprint, flash, g, redirect, render_template, request, url_for

# from application.auth import login_required
from application.userpage_utils import get_user, post_edit_userpage, delete_user

bp = Blueprint('userpage', __name__, url_prefix='/api/userpage')


# @bp.route('/')
# # @login_required
# def render_user_page():
#     user = get_user()
#     return render_template('userpage/index.html', user=user)


@bp.route('/edit', methods=['GET', 'POST'])
# @login_required
def edit_user():
    user = get_user()
    id_user = user['id']

    if request.method == 'POST':
        return post_edit_userpage(id_user)


@bp.route('/delete', methods=['POST'])
# @login_required
def delete_user():
    user = get_user()
    id_user = user['id']

    if request.method == 'POST':
        delete_user(id_user)

    return redirect(url_for('auth.login'))
