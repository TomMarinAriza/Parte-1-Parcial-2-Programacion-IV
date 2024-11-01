import unittest
from models.antibiotics import Antibiotics  
from models import plagueControl
from models import fertilizer
from models.client import Client
from models.bill import Bill

class TestAntibiotics(unittest.TestCase):
    def setUp(self):
        self.antibiotic = Antibiotics("Amoxicillin", 500, 100, "bovino")

    def test_antibiotic_attributes(self):
        self.assertEqual(self.antibiotic.productName, "Amoxicillin")
        self.assertEqual(self.antibiotic.dose, 500)  
        self.assertEqual(self.antibiotic.price, 100)
        self.assertEqual(self.antibiotic.animalsForDose, "bovino")

class TestFertilizer(unittest.TestCase):
    def setUp(self):
        self.fertilizer = fertilizer("ICA456", 200, "Nitrogen", "yearly", "2023-09-01")

    def test_fertilizer_attributes(self):
        self.assertEqual(self.fertilizer.IcaRegister, "ICA456")
        self.assertEqual(self.fertilizer.price, 200)
        self.assertEqual(self.fertilizer.productName, "Nitrogen")
        self.assertEqual(self.fertilizer.frecuencyProdct, "yearly")
        self.assertEqual(self.fertilizer.dateLastApllication, "2023-09-01")

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("John Doe", "123456")

    def test_client_attributes(self):
        self.assertEqual(self.client.name, "John Doe")
        self.assertEqual(self.client.id, "123456")

    def test_purchase_history_method(self):
        self.assertTrue(callable(getattr(self.client, 'purchaseHistory', None)))
        self.assertEqual(self.client.purchaseHistory(), [])

class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill("2024-10-10", 500)

    def test_receipt_attributes(self):  # Corrige "recipt" a "receipt"
        self.assertEqual(self.bill.date, "2024-10-10")  # Cambia self.recipt a self.bill
        self.assertEqual(self.bill.price, 500)

if __name__ == "__main__":
    unittest.main()