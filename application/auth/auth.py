import secrets
from flask import Blueprint, flash, request
import json

from application.db.db import get_db
from application.auth import utils as auth_utils
from application.utils.utils import set_token_expired, get_or_create_token, request_token

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user_id = str(secrets.token_hex(16))

    db = get_db()
    error = auth_utils.check_register_properties(username, password, email)

    if error is None:
        try:
            auth_utils.insert_into_users(user_id, username, password, email)
            token = auth_utils.insert_into_tokens(user_id)

            return json.dumps({
                'text': 'User success added',
                'token': token
            })

        except db.IntegrityError:
            error = f"Email '{email}' is already registered."

    flash(error)
    return json.dumps({
        'error': error
    })


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = auth_utils.get_user_by_email(email)
    error = auth_utils.check_login_properties(user, email, password)

    if error is None:
        token = get_or_create_token(user['id'])

        return json.dumps({
            'token': token
        })

    flash(error)
    return json.dumps({
        'error': error
    })


@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request_token()

    set_token_expired(token)
    return json.dumps({
        'text': 'Success logout'
    })
