# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'erroretesseramento.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_erroretesseramento(object):
    def setupUi(self, erroretesseramento):
        erroretesseramento.setObjectName("erroretesseramento")
        erroretesseramento.resize(400, 93)
        self.buttonBox = QtWidgets.QDialogButtonBox(erroretesseramento)
        self.buttonBox.setGeometry(QtCore.QRect(20, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(erroretesseramento)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 20))
        self.label.setObjectName("label")

        self.retranslateUi(erroretesseramento)
        self.buttonBox.accepted.connect(erroretesseramento.accept) # type: ignore
        self.buttonBox.rejected.connect(erroretesseramento.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(erroretesseramento)

    def retranslateUi(self, erroretesseramento):

        _translate = QtCore.QCoreApplication.translate
        erroretesseramento.setWindowTitle(_translate("erroretesseramento", "Dialog"))
        self.label.setText(_translate("erroretesseramento", "Hai sbagliato a mettere i campi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    erroretesseramento = QtWidgets.QDialog()
    ui = Ui_erroretesseramento()
    ui.setupUi(erroretesseramento)
    erroretesseramento.show()
    sys.exit(app.exec_())
