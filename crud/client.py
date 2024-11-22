from models.client import Client

class ClientCrud:
    def __init__(self):
        self.clients = []

    def createClient(self, name, id):
        newClient = Client(name, id)
        self.clients.append(newClient)

    def readClient(self):
        return [{"id": client.id, "name": client.name} for client in self.clients]

    def updateClient(self, id, newName):
        for client in self.clients:
            if client.id == id:
                client.name = newName
                return True
        return False

    def deleteClient(self, id):
        self.clients = [client for client in self.clients if client.id != id]

    def findClientById(self, id):
        for client in self.clients:
            if client.id == id:
                return client
        return None

    def addBillToClient(self, client_id, bill):
        client = self.findClientById(client_id)
        if client:
            client.addBills(bill)
            return True
        return False

    def searchById(self, id):
        client = self.findClientById(id)
        if client:
            bills_info = []
            for bill in client.getBills():
                bills_info.append({
                    "date": bill.date,
                    "price": bill.price,
                    "products": bill.getProducts()
                })
            return bills_info
        return None
