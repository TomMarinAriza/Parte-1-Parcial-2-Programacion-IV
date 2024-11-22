from PyQt5.QtWidgets import QWidget
from UI.clientRegisterWindow import Ui_Form
from crud.client import ClientCrud  # Asegúrate de importar correctamente la clase CRUD

class ClientRegisterWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.registerClient)
    
    def registerClient(self):
        name = self.ui.nameGetter.text()
        id = self.ui.idGetter.text()

        self.saveClient(name, id)
    
    def saveClient(self, name, id):
        # Crear una instancia de ClientCrud
        client_crud = ClientCrud()
        
        # Llamar al método createClient a través de la instancia
        client_crud.createClient(name, id)
