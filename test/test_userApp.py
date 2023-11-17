import pytest
from flask import Flask
from flask.testing import FlaskClient
from userApp import app, user_blueprint
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_successful_login(client):
    # Simulate a POST request to the login endpoint with valid credentials
    data = {'username': 'Username', 'password': 'Password123@'}
    response =  client.post('/user/user_login/', json =data) 
    assert response.status_code == 302  # Redirect to refresh_and_redirect.html
    assert response.headers['Location'] == '/refresh_and_redirect.html'

def test_invalid_credentials(client):
    # Simulate a POST request to the login endpoint with invalid credentials
    with client.post('/user/user_login', data={'username': 'invalid', 'password': 'password'}) as response:
        assert response.status_code == 200  # Remains on login.html
        assert b'Please input correctly' in response.data  # Error message displayed

def test_missing_login_fields(client):
    # Simulate a POST request to the login endpoint with missing fields
    with client.post('/user/user_login', data={'username': ''}) as response:
        assert response.status_code == 200  # Remains on login.html
        assert b'Please input username and password' in response.data  # Error message displayed

def test_get_login_page(client):
    # Simulate a GET request to the login page
    with client.get('/user/user_login') as response:
        assert response.status_code == 200  # Login page rendered
        assert b'Login' in response.data  # Login page content verified

if __name__ == '__main__':
    pytest.main()