import pytest
from application.db.helpers import get_db


def test_successful_register(client, app):
    response = client.post(
        '/api/auth/register', data={'email': 'abc@email.com', 'password': 'abc', 'username': 'abc'}
    )
    assert response.status_code == 200

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM users WHERE email = 'abc@email.com'",
        ).fetchone() is not None

    assert 'User success added' in response.get_data(as_text=True)


@pytest.mark.parametrize(('email', 'password', 'username', 'message'), (
    ('abc', 'abc', '', 'Username can`t be empty.'),
    ('abc', '', 'abc', 'Password can`t be empty.'),
    ('test_email@email.com', 'abc', 'abc', "Email 'test_email@email.com' is already registered."),
))
def test_failed_register(client, email, password, username, message):
    response_empty = client.post(
        '/api/auth/register', data={'email': email, 'password': password, 'username': username}
    )

    assert message in response_empty.get_data(as_text=True)


def test_register_with_miss_form(client):
    response_none = client.post(
        '/api/auth/register', data={'email': 'abc@email.com', 'password': 'abc'}
    )
    assert response_none.status_code == 400


def test_successful_login(client, app):
    response = client.post(
        '/api/auth/login', data={'email': 'test_email@email.com', 'password': 'test'}
    )
    assert response.status_code == 200

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM users WHERE email = 'test_email@email.com'",
        ).fetchone() is not None

    assert '"token": "test_token"' in response.get_data(as_text=True)


@pytest.mark.parametrize(('email', 'password', 'message'), (
    ('test@email.com', 'test', f"No user with email: 'test@email.com'."),
    ('test_email@email.com', '123', 'Incorrect email or password.')
))
def test_failed_login(client, email, password, message):
    response_empty = client.post(
        '/api/auth/login', data={'email': email, 'password': password}
    )

    assert message in response_empty.get_data(as_text=True)


def test_login_with_miss_form(client, app):
    response = client.post(
        '/api/auth/register', data={'email': 'abc@email.com'}
    )
    assert response.status_code == 400


def test_successful_logout(client, app):
    response = client.post(
        '/api/auth/logout', headers={'Authorization': 'Bearer test_token'}
    )

    assert response.status_code == 200
    assert 'Success logout' in response.get_data(as_text=True)
