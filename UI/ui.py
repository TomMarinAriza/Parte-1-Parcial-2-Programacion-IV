from datetime import datetime
from models import bill

class ShopUI:
    def __init__(self, clientCrud):
        self.clientCrud = clientCrud
        self.shoppingCart = [] 

    def displayProducts(self, products):
        print("Available Products:")
        for product in products:
            print(f"ID: {product.productName}, Price: ${product.price}")

    def addToCart(self, product):
        self.shoppingCart.append(product)
        print(f"{product.productName} added to cart.")

    def viewCart(self):
        if not self.shoppingCart:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for product in self.shoppingCart:
            print(f"- {product.productName} (${product.price})")
        total = sum(product.price for product in self.shoppingCart)
        print(f"Total: ${total}")

    def checkout(self, client_id):
        client = self.clientCrud.findClientById(client_id)
        if not client:
            print("Client not found.")
            return
        
       
        bill = bill(price=sum(product.price for product in self.shoppingCart))
        for product in self.shoppingCart:
            bill.addProduct(product)

       
        client.addBills(bill)
        print(f"Bill created for {client.name} on {bill.date}. Total: ${bill.price}.")
        self.shoppingCart.clear() 
