from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from application.auth import login_required
# from application.db import get_db
from application.userpage_utils import get_user, post_edit_userpage, delete_user

bp = Blueprint('userpage', __name__)


@bp.route('/')
@login_required
def redirect_empty_url():
    return redirect(url_for('userpage.index'))


@bp.route('/userpage', methods=('GET',))
@login_required
def index():
    user = get_user()
    return render_template('userpage/index.html', user=user)


@bp.route('/userpage/test')
@login_required
def test_test():
    user = get_user
    print(user)
    return render_template('userpage/index.html', user=user)


@bp.route('/userpage/edit', methods=('GET', 'POST'))
@login_required
def edit():
    user = get_user()
    id_user = user['id']

    if request.method == 'POST':
        post_edit_userpage(id_user)

    return render_template('userpage/edit.html', user=user)


@bp.route('/userpage/delete', methods=('POST',))
@login_required
def delete():
    user = get_user()
    id_user = user['id']

    if request.method == 'POST':
        delete_user(id_user)

    return redirect(url_for('auth.login'))
