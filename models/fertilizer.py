from controlProducts import controlProduct

class  fertilizer(controlProduct):
    def __init__(self, IcaRegister, price, productName, frecuencyProdct, dateLastApllication):
        super().__init__(IcaRegister, price, productName, frecuencyProdct)
        self.dateLastApllication = dateLastApllication
    
    @property
    def dateLastApllication(self):
        return self.dateLastApllication