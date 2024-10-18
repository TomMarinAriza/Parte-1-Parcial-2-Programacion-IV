import unittest
from models.antibiotics import antibiotics  
from models.controlProducts import plagueControl, fertilizer
from models.client import client
from models.recipt import recipt

class TestAntibiotics(unittest.TestCase):
    def setUp(self):
        
        self.antibiotic = antibiotics("Amoxicillin", "500mg", 100, ["cows", "pigs"])

    def test_antibiotic_attributes(self):
        self.assertEqual(self.antibiotic.productName, "Amoxicillin")
        self.assertEqual(self.antibiotic.dose, "500mg")
        self.assertEqual(self.antibiotic.price, 100)
        self.assertEqual(self.antibiotic.animalsForDose, ["cows", "pigs"])


class TestControlProduct(unittest.TestCase):
    def setUp(self):
        
        self.control_product = plagueControl("ICA123", 150, "Insecticide", "monthly", 7)

    def test_control_product_attributes(self):
        self.assertEqual(self.control_product.IcaRegister, "ICA123")
        self.assertEqual(self.control_product.price, 150)
        self.assertEqual(self.control_product.productName, "Insecticide")
        self.assertEqual(self.control_product.frecuencyProdct, "monthly")
        self.assertEqual(self.control_product.gracePeriod, 7)


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
       
        self.client = client("John Doe", "123456")

    def test_client_attributes(self):
        self.assertEqual(self.client.name, "John Doe")
        self.assertEqual(self.client.id, "123456")

    def test_purchase_history_method(self):
        
        self.assertTrue(callable(getattr(self.client, 'purchaseHistory', None)))
        
        
        self.assertEqual(self.client.purchaseHistory(), [])


class TestRecipt(unittest.TestCase):
    def setUp(self):
       
        self.recipt = recipt("2024-10-10", 500)

    def test_recipt_attributes(self):
        self.assertEqual(self.recipt.date, "2024-10-10")
        self.assertEqual(self.recipt.price, 500)


if __name__ == "__main__":
    unittest.main()
