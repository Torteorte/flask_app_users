from flask import request, flash

from application.db.db import get_db


def post_edit_profile(user_id):
    db = get_db()
    username = request.form['username']
    email = request.form['email']
    about = request.form['about']
    error = None

    fields = {'username': username, 'email': email, 'about': about}

    for field in fields.keys():
        if not fields[field]:
            error = f'{field} is required.'

    if error is None:
        try:
            db.execute(
                'UPDATE users SET username = ?, email = ?, about = ?'
                ' WHERE id = ?',
                [username, email, about, user_id]
            )
            db.commit()
            return f"User information changed successfully"

        except db.IntegrityError:
            error = f"Email {email} is already registered."

    flash(error)
    return f"{error}"


def delete_user(user):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', [user['id']])
    db.commit()

    return f"User {user['username']} success deleted."
