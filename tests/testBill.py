import unittest
from models.bill import Bill

class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill("2024-10-10", 500)

    def test_receipt_attributes(self):  # Corrige "recipt" a "receipt"
        self.assertEqual(self.bill.date, "2024-10-10")  # Cambia self.recipt a self.bill
        self.assertEqual(self.bill.price, 500)
