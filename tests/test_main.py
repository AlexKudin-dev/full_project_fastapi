import docker as docker
from main import app
from httpx import AsyncClient
import unittest


class TestApp(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.app = app
    async def test_endpoint_get_users(self):
        async with AsyncClient(app=self.app, base_url="http://0.0.0.0:8000") as client:
            response = await client.get("/get-users/")
            self.assertEqual(response.status_code, 200, "Expected status code 200")

    async def test_endpoint_get_user(self):
        async with AsyncClient(app=self.app, base_url="http://0.0.0.0:8000") as client:
            response = await client.get("/get-user/1")
            user = response.json()
            self.assertEqual(response.status_code, 200, "Expected status code 200")
            self.assertEqual(user["id"], 1, "Expected id == 1")

    # async def test_endpoint_create_users(self):
    #     async with AsyncClient(app=self.app,base_url="http://0.0.0.0:8000") as client:
    #         data = {"id": 3, "username": "jaijo"}
    #         response = await client.post("/post-create-users/", json=data)
    #         self.assertEqual(response.status_code, 422, "Expected status code 422")
    #         self.assertEqual(response.json(), {"username": "jaijo"})

    async def test_endpoint_patch_user(self):
        async with AsyncClient(app=self.app, base_url="http://0.0.0.0:8000") as client:
           data = {"id": 1, "username": "upd_user"}
           response = await client.patch("/patch-user/", json=data)
           self.assertEqual(response.status_code, 200, "Expected status code 200")
           self.assertEqual(response.json(), 'UPDATE 1')

    async def test_endpoint_delete_users(self):
        async with AsyncClient(app=self.app, base_url="http://0.0.0.0:8000") as client:
          response = await client.delete("/delete-users/2")
          self.assertEqual(response.status_code, 200, "Expected status code 200")
          self.assertEqual(response.json(), {"detail": "User value2 deleted"})




if __name__ == "__main__":
    # Создаем тестовый суит
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApp)

    # Запускаем тесты
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Проверяем результаты тестов
    if result.failures or result.errors:
        # Если есть неуспешные тесты, выключаем контейнер FastAPI
        client = docker.from_env()
        container = client.containers.get("fastapi_app")  # Название контейнера FastAPI
        container.stop()
        print("Контейнер FastAPI выключен.")
















