import unittest

from fastapi.testclient import TestClient

from app.main import app

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
