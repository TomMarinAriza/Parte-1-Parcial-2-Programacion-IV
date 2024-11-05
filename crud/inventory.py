class Inventory:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        
        if quantity < 1:
            raise ValueError("La cantidad debe ser mayor o igual a 1.")
        
        
        product_id = getattr(product, 'product_name', str(id(product)))
        
        if product_id in self.items:
            self.items[product_id]['quantity'] += quantity
        else:
            self.items[product_id] = {'product': product, 'quantity': quantity}
        
        print(f"{quantity} unidades de {product_id} añadidas al inventario.")

    def remove_product(self, product, quantity=1):
       
        product_id = getattr(product, 'product_name', str(id(product)))
        
        if product_id not in self.items or self.items[product_id]['quantity'] < quantity:
            raise ValueError(f"No hay suficiente {product_id} en el inventario.")
        
        self.items[product_id]['quantity'] -= quantity
        if self.items[product_id]['quantity'] == 0:
            del self.items[product_id]
        
        print(f"{quantity} unidades de {product_id} removidas del inventario.")

    def show_inventory(self):
        
        for product_id, info in self.items.items():
            product = info['product']
            quantity = info['quantity']
            print(f"{product_id}: {quantity} unidades")
