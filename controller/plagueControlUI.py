from PyQt5.QtWidgets import QWidget
from UI.plagueControlWindow import Ui_Form
from crud.bill import BillCRUD
from models.client import Client
from models.plagueControl import plagueControl

class PlagueControlWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.buyButton.clicked.connect(self.addPlague)
    
    def addPlague(self):
         ICA = self.ui.ICAGetter.text()
         productName = self.ui.productNameGetter.text()
         price = self.ui.priceGetter.text()
         frequency = self.ui.frequencyApplicationGetter.text()
         gracePeriod = self.ui.gracePeriodGetter.text()

         self.buyProduct(ICA, productName, price, frequency, gracePeriod)
    
    def buyProduct(self, ICA, productName, price, frequency, gracePeriod):
        
        bill_crud = BillCRUD() 
        bill = bill_crud.create_bill(date=gracePeriod, price=price)

        
        product = plagueControl(name=productName, price=price, ICA=ICA, frequency=frequency, gracePeriod=gracePeriod)

       
        bill.addProduct(product)

        
        self.client.addBill(bill)