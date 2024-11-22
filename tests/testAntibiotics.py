
import unittest
from models import antibiotics

class TestAntibiotics(unittest.TestCase):
    def setUp(self):
        self.antibiotic = antibiotics("Amoxicillin", 500, 100, "bovino")

    def test_antibiotic_attributes(self):
        self.assertEqual(self.antibiotic.productName, "Amoxicillin")
        self.assertEqual(self.antibiotic.dose, 500)  
        self.assertEqual(self.antibiotic.price, 100)
        self.assertEqual(self.antibiotic.animalsForDose, "bovino")