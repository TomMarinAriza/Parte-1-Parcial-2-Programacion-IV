from PyQt5.QtWidgets import QMainWindow
from UI.searchByIdWindow import Ui_searchWindow

class SearchByIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_searchWindow()
        self.ui.setupUi(self)
