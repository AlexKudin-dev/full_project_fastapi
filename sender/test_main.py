from fastapi.testclient import TestClient
from main import app
from fastapi import status






async def test_endpoint_get_users(client : TestClient(app)):
    response = await client.get("/users/")
    assert response.status_code == status.HTTP_200_OK


async def test_endpoint_users_user_id(client : TestClient(app)):
    response = await client.get(f"/user/{1}/")
    assert response.status_code == status.HTTP_200_OK
    #assert response.json()['id'] == 1, ["username"] == "string"



# def test_endpoint_create_users(client):
#     data = {"username": "jane_doe"}
#     response = client.post("/create_users/", json=data)
#     assert response.status_code == 422
#     assert response.json() == {"username": "jane_doe"}
#
#
#
#  def test_update_user():
#      data = {"username": "updated_user"}
#      response = client.patch("/users/1", json=data)
#      assert response.status_code == 200
#      assert response.json() == {"id": 1, "username": "updated_user"}
#

#  def test_endpoint_delete_user():
#      response = client.delete("/users/3")
#      assert response.status_code == 200
#     assert response.json() == {"message": "User deleted"}


