from UI.buyingWindow import Ui_Form
from PyQt5.QtWidgets import QWidget

class BuyingWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)