import unittest

from models.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("John Doe", "123456")

    def test_client_attributes(self):
        self.assertEqual(self.client.name, "John Doe")
        self.assertEqual(self.client.id, "123456")

    def test_purchase_history_method(self):
        self.assertTrue(callable(getattr(self.client, 'purchaseHistory', None)))
        self.assertEqual(self.client.purchaseHistory(), [])