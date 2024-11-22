import unittest

from models.plagueControl import PlagueControl

class TestPlagueControl(unittest.TestCase):
    def setUp(self):
        self.plagueControl = PlagueControl("ICA456", 200, "Nitrogen", "yearly", "2023-09-01")

    def test_plagueControl_attributes(self):
        self.assertEqual(self.plagueControl.IcaRegister, "ICA456")
        self.assertEqual(self.plagueControl.price, 200)
        self.assertEqual(self.plagueControl.productName, "Nitrogen")
        self.assertEqual(self.plagueControl.frecuencyProdct, "yearly")
        self.assertEqual(self.plagueControl.dateLastApllication, "2023-09-01")