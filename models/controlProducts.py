class controlProduct :
    def __init__(self, IcaRegister, price , productName , frecuencyProdct ):
        self.IcaRegister = IcaRegister 
        self.price = price
        self.productName = productName
        self.frecuencyProdct = frecuencyProdct

    @property
    def IcaRegister(self):
        return self.IcaRegister
    
    @IcaRegister.setter
    def IcaRegister(self, IcaRegister):
        self.IcaRegister = IcaRegister
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, price):
        self.price = price

    @property
    def productName(self):
        return self.productName
    
    @productName.setter
    def productName(self, productName):
        self.productName = productName

    @property
    def frecuencyProdct(self):
        return self.frecuencyProdct
    
    @frecuencyProdct.setter
    def frecuencyProdct(self, frecuencyProdct):
        self.frecuencyProdct = frecuencyProdct
