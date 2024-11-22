import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from UI import mainWindow
from controller.searcherUi import SearchByIdWindow
from controller.clientRegisterUI import ClientRegisterWindow
from controller.buyingUI import BuyingWindow
from controller.antibioticUI import AntibioticWindow
from controller.fertilizerUi import FertilizerWindow
from controller.plagueControlUI import PlagueControlWindow

class MainApplication(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.searchByIDButtom.clicked.connect(self.searchById)
        self.ui.buyProductsButtom.clicked.connect(self.registerClient)
    
    def searchById(self):
        self.searchByIdWindow = SearchByIdWindow()
        self.searchByIdWindow.show()

    def registerClient(self):
        self.clientRegisterWindow = ClientRegisterWindow()
        self.clientRegisterWindow.show()
        self.clientRegisterWindow.ui.pushButton.clicked.connect(self.buyProducts)
    
    def buyProducts(self):
        self.buyingWindow = BuyingWindow()
        self.buyingWindow.show()
        self.buyingWindow.ui.antibioticButton.clicked.connect(self.antibiotic)
        self.buyingWindow.ui.fertilizerButton.clicked.connect(self.fertilizer)
        self.buyingWindow.ui.plageControlButton.clicked.connect(self.plagueControl)

    def antibiotic(self):
        self.antibioticWindow = AntibioticWindow()
        self.antibioticWindow.show()
    
    def fertilizer(self):
        self.fertilizerWindow = FertilizerWindow()
        self.fertilizerWindow.show()

    def plagueControl(self):
        self.plagueControlWindow = PlagueControlWindow()
        self.plagueControlWindow.show()
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApplication()
    main_app.show()
    sys.exit(app.exec_())
