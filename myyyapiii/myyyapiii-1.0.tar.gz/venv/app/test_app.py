from email import header
from urllib import response
from .app import app

from fastapi.testclient import TestClient
import pytest  

client = TestClient(app)

@pytest.fixture
def get_create_data():
    create_user_data = {
    "email": "oo9iiiy675@gmail.com",
    "password": "test5",
    "org_name": "oioo"
    }
    return  create_user_data 

@pytest.fixture
def get_login_data():
    login_data = {
        "username": "test1@gmail.com",
        "password": "test1"
    }
    return login_data

@pytest.fixture
def authorize(get_login_data):
    token = client.post("/auth/jwt/login", data = get_login_data)
    return token

@pytest.fixture
def get_token(authorize):
    token_data = {
        "Authorization": "Bearer"+" "+authorize.json()["access_token"]
    }
    return token_data

#REGISTER
def test_create_user(get_create_data):
    response = client.post("/auth/register", json=get_create_data)
    assert response.status_code == 201
    assert response.json()["org_id"] == response.json()["id"]

# def test_create_user_empty():
#     response = client.post("/auth/register", json={})
#     assert response.status_code == 422

# def test_create_user_twice(get_create_data):
#     response = client.post("/auth/register", json=get_create_data)
#     assert response.status_code == 400
#     assert response.json() == {
#         "detail": "REGISTER_USER_ALREADY_EXISTS"
#     }

# #LOGIN
# def test_login(get_login_data):                                                         #failed
#     response = client.post("/auth/jwt/login", data = get_login_data)
#     assert response.status_code == 200
#     assert response.json()["token_type"] == "bearer"

# def test_login_wrong_email():
#     login_data = {
#         "username": "sumdus@gmail.com",
#         "password": "password"
#     }

#     response = client.post("/auth/jwt/login", data = login_data)
#     assert response.json() == {
#         "detail": "LOGIN_BAD_CREDENTIALS"
#     }

# def test_login_wrong_password():
#     login_data = {
#         "username": "sundus@gmail.com",
#         "password": "sundusss"
#     }
#     response = client.post("/auth/jwt/login", data = login_data)
#     assert response.json() == {
#         "detail": "LOGIN_BAD_CREDENTIALS"
#     }

# #LOGOUT
# def test_logout(get_token):
#     response = client.post("/auth/jwt/logout", headers = get_token)
#     assert response.status_code == 200

# #FORGOT-PASSWORD
# def test_forgot_password():             #failed
#     data = {
#         "email": "user@example.com"
#     }
#     response = client.post("/auth/forgot-password", data = data)
#     assert response.status_code == 202


# #GET-CURRENT-USER
# def test_get_current_user(get_token):
#     response = client.get("/users/me", headers=get_token)
#     response.json()["email"] == "test1@gmail.com"

# #PATCH-CURRENT-USER
# def test_patch_current_user(get_token):
#     update_data = {
#         "password": "user1234",
#         "email": "user1234@example.com"
#     }
#     response = client.patch("/users/me", headers = get_token, data=update_data)

#     assert response.status_code == 200
#     assert response.json()["email"] ==  "user1234@example.com"