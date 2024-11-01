import unittest
from models.plagueControl import plagueControl
from models.fertilizer import fertilizer
from models.antibiotics import Antibiotics
from models.client import Client
from models.bill import Bill
from UI.ui import ShopUI
from crud.client import ClientCrud as clientCrud

from tests.test import (
    TestAntibiotics,
    TestFertilizer,
    TestClient,
    TestBill,
)

class TestShopUI(unittest.TestCase):
    def setUp(self):
        self.clientCrud = clientCrud()
        self.shopUI = ShopUI(self.clientCrud)
        self.clientCrud.createClient("John Doe", "123456")
        self.products = [
            Antibiotics("Amoxicillin", 500, 100, "bovino"),
            plagueControl("ICA123", 150, "Insecticide", "monthly", 7),
            fertilizer("ICA456", 200, "Nitrogen", "yearly", "2023-09-01")
        ]

    def testDisplayProducts(self):
        self.shopUI.displayProducts(self.products)

    def testAddToCart(self):
        self.shopUI.addToCart(self.products[0])
        self.assertIn(self.products[0], self.shopUI.shoppingCart)

    def testViewCart(self):
        self.shopUI.addToCart(self.products[1])
        self.shopUI.viewCart()

    def testCheckout(self):
        self.shopUI.addToCart(self.products[0])
        self.shopUI.checkout(client_id="123456")
        client = self.clientCrud.findClientById("123456")
        self.assertGreater(len(client.getBills()), 0)

def interactiveShop(shopUI):
    print("Welcome to the Shop!")
    while True:
        print("\nSelect an option:")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            shopUI.displayProducts()
        
        elif choice == "2":
            productName = input("Enter the product name to add to cart: ")
            productToAdd = next((prod for prod in shopUI.products if prod.product_name == productName), None)
            if productToAdd:
                shopUI.addToCart(productToAdd)
                print(f"Added {productToAdd.product_name} to cart.")
            else:
                print("Product not found.")

        elif choice == "3":
            shopUI.viewCart()
        
        elif choice == "4":
            clientId = input("Enter your client ID: ")
            shopUI.checkout(clientId)
        
        elif choice == "5":
            print("Exiting the shop. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")

def runTests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Asegúrate de que las siguientes son clases que heredan de unittest.TestCase
    suite.addTests(loader.loadTestsFromTestCase(TestAntibiotics))
    suite.addTests(loader.loadTestsFromTestCase(TestFertilizer))
    suite.addTests(loader.loadTestsFromTestCase(TestClient))
    suite.addTests(loader.loadTestsFromTestCase(TestBill))
    suite.addTests(loader.loadTestsFromTestCase(TestShopUI))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    runTests()

    clientCrud = clientCrud()
    shopUI = ShopUI(clientCrud)
    interactiveShop(shopUI)
