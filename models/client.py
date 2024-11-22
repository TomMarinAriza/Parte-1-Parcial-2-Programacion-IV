class Client:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._bills = []  

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    def addBill(self, bill):
        """
        Añade una factura al historial de facturas del cliente.
        :param bill: Instancia de la clase Bill.
        """
        self._bills.append(bill)  

    def getBills(self):
        """
        Devuelve el historial de facturas del cliente.
        """
        return self._bills
    