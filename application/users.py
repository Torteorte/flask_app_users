from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from application.db import get_db

bp = Blueprint('users', __name__)


@bp.route('/api/users', methods=('GET',))
def get_all_users():
    data_all = []
    db = get_db()
    users = db.execute(
        'SELECT *'
        ' FROM users'
    ).fetchall()

    for user in users:
        user_dict = {
            'id': user['id'],
            'username': user['username'],
            'email': user['email'],
            'about': user['about']
        }
        data_all.append(user_dict)
    return jsonify(users=data_all)


@bp.route('/api/users/auth-user', methods=('GET',))
def get_current_user():
    return jsonify(
        id=g.user['id'],
        username=g.user['username'],
        email=g.user['email'],
        about=g.user['about']
    )
