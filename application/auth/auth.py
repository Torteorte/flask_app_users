import functools
from flask import Blueprint, flash, g, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from application.db import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'

        elif not password:
            error = 'Password is required.'

        elif not email:
            error = 'Email is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                    (username, generate_password_hash(password), email),
                )
                db.commit()
                return f"User success added"

            except db.IntegrityError:
                error = f"Email '{email}' is already registered."

        flash(error)
        return f"Error: {error}"


@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()

        if email is None:
            error = f'Incorrect email.'

        elif not check_password_hash(user['password'], password):
            error = f'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return f"Login success"

        flash(error)
        return f"Error: {error}"


@auth_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return f"User logout"


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None

    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return f"No authorized user. Please, authorize first"

        return view(**kwargs)

    return wrapped_view
