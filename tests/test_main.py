import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def test_create_item(self):
        response = client.post("/items", json={"name": "Test Item", "description": "A test item", "price": 10.0})
        self.assertEqual(response.status_code, 200)

    def test_read_items(self):
        response = client.get("/items")
        self.assertEqual(response.status_code, 200)
