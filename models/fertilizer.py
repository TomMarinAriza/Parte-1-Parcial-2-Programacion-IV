from models.controlProducts import controlProduct

class fertilizer(controlProduct):
    def __init__(self, icaRegister, price, productName, frequencyProduct, dateLastApplication):
        super().__init__(icaRegister, price, productName, frequencyProduct)
        self._dateLastApplication = dateLastApplication 
    
    @property
    def dateLastApplication(self):
        return self._dateLastApplication 

    @dateLastApplication.setter
    def dateLastApplication(self, dateLastApplication):
        self._dateLastApplication = dateLastApplication 
