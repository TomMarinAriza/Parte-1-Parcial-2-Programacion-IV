class client:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.history = [] 

    def purchaseHistory(self):
        return self.history 
