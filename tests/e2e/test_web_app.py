import pytest

from flask import session

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_register(client):
    # Check that we retrieve the register page.
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    # Check that we can register a user successfully, supplying a valid user name and password.
    response = client.post(
        '/authentication/register',
        data={'user_name': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert response.headers['Location'] == '/authentication/login'

    # Check that we can't register a user with an invalid user name.
    response = client.post(
        '/authentication/register',
        data={'user_name': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert b'User name not unique - please choose another name' in response.data

    # Check that we can't register a user with an invalid password.
    response = client.post(
        '/authentication/register',
        data={'user_name': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert b'User name not unique - please choose another name' in response.data

@pytest.fixture
def auth(client):
    def login():
        return client.post(
            '/authentication/login',
            data={'user_name': 'thorke', 'password': 'Abcdef123!'}
        )

    def logout():
        return client.get('/authentication/logout')

    return type('Auth', (), {'login': login, 'logout': logout})

def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session

def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

