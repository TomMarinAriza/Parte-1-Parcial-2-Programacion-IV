import unittest
from models.controlProducts import plagueControl
from models.controlProducts import fertilizer
from models.antibiotics import antibiotics
from models.client import client
from models.recipt import recipt
from tests.test import (
    TestAntibiotics,
    TestControlProduct,
    TestFertilizer,
    TestClient,
    TestRecipt,
)

def run_tests():
    
    
    test_antibiotics = TestAntibiotics()
    test_control_product = TestControlProduct()
    test_fertilizer = TestFertilizer()
    test_client = TestClient()
    test_recipt = TestRecipt()

    test_antibiotics.antibiotic = antibiotics("Amoxicillin", int (500), 100,"bovino")
    test_control_product.control_product = plagueControl("ICA123", 150, "Insecticide", "monthly", 7)
    test_fertilizer.fertilizer = fertilizer("ICA456", 200, "Nitrogen", "yearly", "2023-09-01")
    test_client.client = client("John Doe", "123456")
    test_recipt.recipt = recipt("2024-10-10", 500)

    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestAntibiotics))
    suite.addTests(loader.loadTestsFromTestCase(TestControlProduct))
    suite.addTests(loader.loadTestsFromTestCase(TestFertilizer))
    suite.addTests(loader.loadTestsFromTestCase(TestClient))
    suite.addTests(loader.loadTestsFromTestCase(TestRecipt))

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
