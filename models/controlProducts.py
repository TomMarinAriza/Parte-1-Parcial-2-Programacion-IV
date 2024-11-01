class controlProduct:
    def __init__(self, icaRegister, price, productName, frequencyProduct):
        self._icaRegister = icaRegister  
        self._price = price              
        self._productName = productName  
        self._frequencyProduct = frequencyProduct  

    @property
    def IcaRegister(self):
        return self._icaRegister  
    
    @IcaRegister.setter
    def IcaRegister(self, icaRegister):
        self._icaRegister = icaRegister 
    
    @property
    def price(self):
        return self._price  
    
    @price.setter
    def price(self, price):
        self._price = price 

    @property
    def productName(self):
        return self._productName 
    
    @productName.setter
    def productName(self, productName):
        self._productName = productName  

    @property
    def frequencyProduct(self):
        return self._frequencyProduct 
    
    @frequencyProduct.setter
    def frequencyProduct(self, frequencyProduct):
        self._frequencyProduct = frequencyProduct  
