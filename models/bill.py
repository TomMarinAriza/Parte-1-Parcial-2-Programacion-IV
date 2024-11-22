class Bill:
    def __init__(self, date, price, client):
        self._price = price
        self._date = date
        self._client = client  
        self._products = [] 
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price
    
    @property
    def client(self):
        return self._client
    
    def addProduct(self, product):
        """
        Añade un producto a la factura.
        :param product: Instancia de una clase de producto.
        """
        self._products.append(product)

    def removeProduct(self, product):
        """
        Elimina un producto de la factura.
        :param product: Instancia del producto a eliminar.
        """
        if product in self._products:
            self._products.remove(product)
        else:
            raise ValueError("El producto no está en la factura.")

    def getProducts(self):
        """
        Devuelve la lista de productos en la factura.
        """
        return self._products
