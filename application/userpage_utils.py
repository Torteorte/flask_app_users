from flask import g, redirect, request, flash, url_for
from application.db import get_db


def get_user():
    user_id = g.user['id']
    user = get_db().execute(
        'SELECT id, username, about, email'
        ' FROM users'
        ' WHERE id = ?',
        (user_id,)
    ).fetchone()

    return user


def post_edit_userpage(id_user):
    username = request.form['username']
    email = request.form['email']
    about = request.form['about']
    error = None

    if not username:
        error = 'User name is required.'

    if not email:
        error = 'Email name is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            'UPDATE users SET username = ?, email = ?, about = ?'
            ' WHERE id = ?',
            (username, email, about, id_user)
        )
        db.commit()
        return f"User data changed successfully"


def delete_user(id_user):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (id_user,))
    db.commit()
