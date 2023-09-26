import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope='module')
def client():
    with TestClient(app) as client:
        yield client

def test_endpoint_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200

def test_endpoint_users_user_id(client):
    response = client.get(f"/users/{1}")
    assert response.status_code == 200
    assert response.json()['id'] == 1, ["username"] == "string"

# def test_endpoint_create_users(client):
#     data = {"id":3, "username": "jane_doe"}
#     response = client.post("/create_users/", json=data)
#     assert response.status_code == 201
#     assert response.json() == {"id": 3, "username": "jane_doe"}


# def test_update_user():
#     data = {"username": "updated_user"}
#     response = client.patch("/users/1", json=data)
#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "username": "updated_user"}
#
# def test_delete_user():
#     response = client.delete("/users/1")
#     assert response.status_code == 200
#     assert response.json() == {"message": "User deleted"}


