import pytest
from jose import jwt

from app.config import settings
#from test.database import client, session
from app import schemas


# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hello World!'
#     assert res.status_code == 200



def test_create_user(client):
    res = client.post('/users/', json={'email': 'a@ale.de', 'password': 'pass'})
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'a@ale.de'
    assert res.status_code == 201


def test_login_user(client):
    res = client.post('/login', data={'username': 'a@ale.de', 'password': 'pass'})
    print(res.json())
    assert res.status_code == 200





def test_login_user2(client, test_user):
    print(test_user)
    res = client.post('/login', data={'username': test_user['email'], 'password': test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get('user_id')
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200


@pytest.mark.parametrize('email, password, status_code', [
    ('test@test.de', 'password', 403),
    (None, 'password', 422),
    ('testdf@test.de', 'password22', 403),
])
def test_incorrect_login(client, email, password, status_code):
    res = client.post('/login', data={'username': email, 'password': password})

    assert res.status_code == status_code
    print(res.json().get('detail'))
    #assert res.json().get('detail') == 'Invalid credentials'



















