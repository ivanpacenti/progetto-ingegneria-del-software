# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confermatesseramento.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confermatesseramento(object):
    def setupUi(self, confermatesseramento):
        confermatesseramento.setObjectName("confermatesseramento")
        confermatesseramento.resize(400, 93)
        self.buttonBox = QtWidgets.QDialogButtonBox(confermatesseramento)
        self.buttonBox.setGeometry(QtCore.QRect(20, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(confermatesseramento)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 20))
        self.label.setObjectName("label")

        self.retranslateUi(confermatesseramento)
        self.buttonBox.accepted.connect(confermatesseramento.accept) # type: ignore
        self.buttonBox.rejected.connect(confermatesseramento.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(confermatesseramento)

    def retranslateUi(self, confermatesseramento):
        _translate = QtCore.QCoreApplication.translate
        confermatesseramento.setWindowTitle(_translate("confermatesseramento", "Dialog"))
        self.label.setText(_translate("confermatesseramento", "Tesseramento effettuato con successo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confermatesseramento = QtWidgets.QDialog()
    ui = Ui_confermatesseramento()
    ui.setupUi(confermatesseramento)
    confermatesseramento.show()
    sys.exit(app.exec_())