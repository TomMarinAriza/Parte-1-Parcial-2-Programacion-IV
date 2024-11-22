from PyQt5.QtWidgets import QWidget
from UI.antibioticWindow import Ui_Form
from crud.bill import BillCRUD
from models.antibiotics import Antibiotics
from models.client import Client

class AntibioticWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
     
        self.ui.buyButton_2.clicked.connect(self.addAntibiotic)
    
    def addAntibiotic(self):
        dose = self.ui.doseGetter.text()
        productName = self.ui.productNameGetter.text()
        price = self.ui.p.text()
        animalsForDose = self.ui.lineEdit_6.text()

        self.buyProduct(dose, productName, price, animalsForDose)
    

    def buyProduct(self, dose, productName, price, animalsForDose):
        bill_crud = BillCRUD() 
        bill = bill_crud.create_bill(date=price, price=price)

        
        product = Antibiotics(name=productName, price=price, dose=dose, animalsForDose=animalsForDose)

       
        bill.addProduct(product)

        
        self.client.addBill(bill)