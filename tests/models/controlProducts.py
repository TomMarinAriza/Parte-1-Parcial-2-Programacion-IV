class controlProduct :
    def __init__(self, IcaRegister, price , productName , frecuencyProdct ):
        self.IcaRegister = IcaRegister 
        self.price = price
        self.productName = productName
        self.frecuencyProdct = frecuencyProdct


class plagueControl (controlProduct):
    def __init__(self, IcaRegister, price , productName , frecuencyProdct , gracePeriod):
        super().__init__(IcaRegister, price , productName , frecuencyProdct)
        self.gracePeriod = gracePeriod

class  fertilizer(controlProduct):
    def __init__(self, IcaRegister, price, productName, frecuencyProdct, dateLastApllication):
        super().__init__(IcaRegister, price, productName, frecuencyProdct)
        self.dateLastApllication = dateLastApllication