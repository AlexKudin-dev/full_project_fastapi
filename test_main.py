from main import app
from httpx import AsyncClient
import unittest


class TestApp(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.app = app
    async def test_endpoint(self):
        async with AsyncClient(app=self.app, base_url="http://0.0.0.0:8000") as client:
            response = await client.get("/get-users/")
            self.assertEqual(response.status_code, 200, "Expected status code 200")



if __name__ == "__main__":
    unittest.main()




# async def test_endpoint_users_user_id(client : TestClient(app)):
#     response = await client.get(f"/user/{1}/")
#     assert response.status_code == status.HTTP_200_OK
#     #assert response.json()['id'] == 1, ["username"] == "string"



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


