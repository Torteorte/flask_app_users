from flask import request
import json

from application.profile.profile import profile_bp
from application.auth.auth import auth_bp


def page_not_found(e):
    return json.dumps({
        'error': 'Error 404! Not Found',
        'URL': f'{request.base_url}',
        'method': f'{request.method}',
        'text': 'Try another one URL or method'
    }), 404


def invalid_method(e):
    return json.dumps({
        'error': 'Error 405! Not Allowed',
        'URL': f'{request.base_url}',
        'method': f'{request.method}',
        'text': 'Try another method'
    }), 405


@auth_bp.errorhandler(400)
def bad_request_auth(e):
    if request.path.startswith('/api/auth/register'):
        return json.dumps({
            'error': 'Error 400! BAD REQUEST',
            'text': 'Check username, email and password in form-data of request'
        }), 400

    elif request.path.startswith('/api/auth/login'):
        return json.dumps({
            'error': 'Error 400! BAD REQUEST',
            'text': 'Check email and password in form-data of request'
        }), 400


@profile_bp.errorhandler(400)
def bad_request_edit(e):
    if request.path.startswith('/api/profile/edit'):
        return json.dumps({
            'error': 'Error 400! BAD REQUEST',
            'text': 'Check username, email and about in form-data of request'
        }), 400


def app_register_error_handler(app):
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, invalid_method)
    app.register_error_handler(400, bad_request_edit)
    app.register_error_handler(400, bad_request_auth)
