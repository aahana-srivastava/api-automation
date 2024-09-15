import pytest
import requests
from utils.api_helper import get, post, put, delete

def test_get_all_posts():
    posts = get('/posts')
    assert isinstance(posts, list)
    assert len(posts) > 0

def test_get_specific_post():
    post = get('/posts/1')
    assert isinstance(post, dict)
    assert post['id'] == 1

def test_create_new_post():
    new_post = {
        'title': 'Test Post',
        'body': 'This is a test post',
        'userId': 1
    }
    created_post = post('/posts', new_post)
    assert created_post['title'] == new_post['title']
    assert created_post['body'] == new_post['body']

def test_update_post():
    updated_post = {
        'id': 1,
        'title': 'Updated Post',
        'body': 'This post has been updated',
        'userId': 1
    }
    response = put('/posts/1', updated_post)
    assert response['title'] == updated_post['title']
    assert response['body'] == updated_post['body']

def test_delete_post():
    response = delete('/posts/1')
    assert response == {}

def test_nonexistent_post():
    with pytest.raises(requests.exceptions.HTTPError):
        get('/posts/999999')