class Client:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self.history = [] 

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

    def addBills(self, bill):
        self.history.append(bill)  

    def getBills(self):
        return self.history  
