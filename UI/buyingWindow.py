# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buyingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 431)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 50, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fertilizerButton = QtWidgets.QPushButton(Form)
        self.fertilizerButton.setGeometry(QtCore.QRect(170, 130, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fertilizerButton.setFont(font)
        self.fertilizerButton.setObjectName("fertilizerButton")
        self.plageControlButton = QtWidgets.QPushButton(Form)
        self.plageControlButton.setGeometry(QtCore.QRect(120, 190, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plageControlButton.setFont(font)
        self.plageControlButton.setObjectName("plageControlButton")
        self.antibioticButton = QtWidgets.QPushButton(Form)
        self.antibioticButton.setGeometry(QtCore.QRect(170, 270, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.antibioticButton.setFont(font)
        self.antibioticButton.setObjectName("antibioticButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Seleccione el producto a comprar"))
        self.fertilizerButton.setText(_translate("Form", "Fertilizantes"))
        self.plageControlButton.setText(_translate("Form", "Controles de plagas"))
        self.antibioticButton.setText(_translate("Form", "Antibioticos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
