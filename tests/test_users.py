import pytest
import requests
from utils.api_helper import get, post, put

def test_get_all_users():
    users = get('/users')
    assert isinstance(users, list)
    assert len(users) > 0

def test_get_specific_user():
    user = get('/users/1')
    assert isinstance(user, dict)
    assert user['id'] == 1

def test_create_new_user():
    new_user = {
        'name': 'John Doe',
        'username': 'johndoe',
        'email': 'johndoe@example.com'
    }
    created_user = post('/users', new_user)
    assert created_user['name'] == new_user['name']
    assert created_user['username'] == new_user['username']

def test_update_user():
    updated_user = {
        'id': 1,
        'name': 'Jane Doe',
        'username': 'janedoe',
        'email': 'janedoe@example.com'
    }
    response = put('/users/1', updated_user)
    assert response['name'] == updated_user['name']
    assert response['username'] == updated_user['username']

def test_nonexistent_user():
    with pytest.raises(requests.exceptions.HTTPError):
        get('/users/999999')