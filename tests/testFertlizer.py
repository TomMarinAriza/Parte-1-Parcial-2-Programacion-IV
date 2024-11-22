import unittest

from models.fertilizer import fertilizer

class TestFertilizer(unittest.TestCase):
    def setUp(self):
        self.fertilizer = fertilizer("ICA456", 200, "Nitrogen", "yearly", "2023-09-01")

    def test_fertilizer_attributes(self):
        self.assertEqual(self.fertilizer.IcaRegister, "ICA456")
        self.assertEqual(self.fertilizer.price, 200)
        self.assertEqual(self.fertilizer.productName, "Nitrogen")
        self.assertEqual(self.fertilizer.frecuencyProdct, "yearly")
        self.assertEqual(self.fertilizer.dateLastApllication, "2023-09-01")
