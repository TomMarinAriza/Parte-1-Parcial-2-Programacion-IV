from models.controlProducts import controlProduct

class plagueControl (controlProduct):
    def __init__(self, IcaRegister, price , productName , frecuencyProdct , gracePeriod):
        super().__init__(IcaRegister, price , productName , frecuencyProdct)
        self.gracePeriod = gracePeriod

    @property
    def gracePeriod(self):
        return self.gracePeriod