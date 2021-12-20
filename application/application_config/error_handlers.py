import json
from flask import request, jsonify

from .exceptions import InvalidAPIUsage
from application.auth.api import auth_bp
from application.profile.api import profile_bp
from application.users.api import users_bp


@auth_bp.errorhandler(InvalidAPIUsage)
@profile_bp.errorhandler(InvalidAPIUsage)
def invalid_request(e):
    return jsonify(e.to_dict()), 400


@users_bp.errorhandler(InvalidAPIUsage)
def no_user_request(e):
    return jsonify(e.to_dict()), 404


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


def app_register_error_handler(app):
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, invalid_method)
    app.register_error_handler(400, invalid_request)
    app.register_error_handler(404, no_user_request)
