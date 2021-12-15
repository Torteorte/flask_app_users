from flask import Blueprint, flash, request
import secrets

from application.db.db import get_db
from application.utils.utils import out_token, get_token
from .utils import insert_into_users, insert_into_tokens, check_register_properties, get_user_by_email, \
    check_login_properties

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user_id = str(secrets.token_hex(16))

    db = get_db()
    error = check_register_properties(username, password, email)

    if error is None:
        try:
            insert_into_users(user_id, username, password, email)
            insert_into_tokens(user_id)
            return f"User success added"

        except db.IntegrityError:
            error = f"Email '{email}' is already registered."

    flash(error)
    return f"Error: {error}"


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = get_user_by_email(email)
    error = check_login_properties(user, email, password)

    if error is None:
        token = get_token(user['id'])
        return f"Login success." \
               f" Token: {token}"

    flash(error)
    return f"Error: {error}"


@auth_bp.route('/logout/<token>', methods=['POST'])
def logout(token):
    return out_token(token)
