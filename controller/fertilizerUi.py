from PyQt5.QtWidgets import QWidget
from UI.fertilizerWindow import Ui_Form
from crud.bill import BillCRUD  
from models.client import Client
from models.fertilizer import fertilizer

class FertilizerWindow(QWidget, Ui_Form):
    def __init__(self):  
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
     
        self.ui.buyButton.clicked.connect(self.addFertilizer)
    
    def addFertilizer(self):
        ICA = self.ui.ICAGetter.text()
        productName = self.ui.productNameGetter.text()
        price = self.ui.priceGetter.text()
        frequency = self.ui.frequencyApplicationGetter.text()
        lastApplication = self.ui.lastApplicationGetter.text()

        
        self.buyProduct(ICA, productName, price, frequency, lastApplication)
    
    def buyProduct(self, ICA, productName, price, frequency, lastApplication):
       
        bill_crud = BillCRUD() 
        bill = bill_crud.create_bill(date=lastApplication, price=price)

        
        product = fertilizer(name=productName, price=price, ICA=ICA, frequency=frequency, lastApplication=lastApplication)

       
        bill.addProduct(product)

        
        self.client.addBill(bill)