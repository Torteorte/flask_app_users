def test_successful_get_all_users(client):
    response = client.get(
        '/api/users', headers={'Authorization': 'Bearer test_token'}
    )

    assert response.status_code == 200


def test_successful_get_current_user(client):
    response = client.get(
        '/api/users/test_id', headers={'Authorization': 'Bearer test_token'}
    )

    assert response.status_code == 200


def test_failed_get_current_user(client):
    response = client.get(
        '/api/users/te', headers={'Authorization': 'Bearer test_token'}
    )

    assert response.status_code == 404
    assert "User with id 'te' is not found" in response.get_data(as_text=True)
