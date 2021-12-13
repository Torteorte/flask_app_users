from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)

from application.db import get_db

bp = Blueprint('users', __name__)


@bp.route('/api/users', methods=['GET'])
def get_all_users():
    data_all = []
    db = get_db()

    users = db.execute(
        'SELECT id, username, email, about'
        ' FROM users'
    ).fetchall()

    for user in users:
        data_all.append({**user})

    return jsonify(users=data_all)


@bp.route('/api/users/auth-user', methods=['GET'])
def get_current_user():
    if g.user:
        return jsonify(
            id=g.user['id'],
            username=g.user['username'],
            email=g.user['email'],
            about=g.user['about']
        )
    else:
        return f"No authorized user. Please, authorize first"


@bp.route('/api/users/user:<int:userid>', methods=['GET'])
def get_user_by_id(userid):
    user = get_db().execute(
        'SELECT id, username, email, about'
        ' FROM users'
        ' WHERE id = ?', [userid]
    ).fetchone()
    if user:
        return jsonify({**user})
    else:
        return f"There is no such user"
