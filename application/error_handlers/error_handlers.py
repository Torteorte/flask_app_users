from flask import request
from application.profile.profile import profile_bp
from application.auth.auth import auth_bp


def page_not_found(e):
    return f'Error 404! "URL: {request.base_url}, Method: {request.method}" Not Found! ' \
           f'Try another one URL or method.', 404


def invalid_method(e):
    return f'Error 405! "Method: {request.method}" for "URL: {request.base_url}" Not Allowed! ' \
           f'Try another method', 405


@auth_bp.errorhandler(400)
def bad_request_auth(e):
    if request.path.startswith('/api/auth/register'):
        return f'Error 400 BAD REQUEST! Check username, email and password in form-data of request', 400
    elif request.path.startswith('/api/auth/login'):
        return f'Error 400 BAD REQUEST! Check email and password in form-data of request', 400


@profile_bp.errorhandler(400)
def bad_request_edit(e):
    if request.path.startswith('/api/profile/edit'):
        return f'Error 400 BAD REQUEST! Check username, email and about in form-data of request', 400
