class Bill:
    def __init__(self, date, price):
        self._price = price
        self._date = date
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
    
    def addProduct(self, product):
        self._products.append(product) 

    def getProducts(self):
        return self._products  
