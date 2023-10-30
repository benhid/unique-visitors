import unittest

from fastapi.testclient import TestClient

from app.main import app, get_db


class MockDatabase:
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def fetch_val(self, _):
        return 1

    async def execute(self, stmt, values):
        pass


def override_get_db():
    return MockDatabase()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class TestMain(unittest.TestCase):
    def test_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "1")

    def test_get_site_view(self):
        response = client.post("/site_view")
        self.assertEqual(response.status_code, 200)

    def test_get_version(self):
        response = client.get("/version")
        self.assertEqual(response.status_code, 200)

    def test_get_healthz(self):
        response = client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})


if __name__ == "__main__":
    unittest.main()
