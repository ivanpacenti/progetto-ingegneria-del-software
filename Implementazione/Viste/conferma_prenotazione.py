# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conferma_prenotazione.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_conferma_prenotazione(object):
    def setupUi(self, conferma_prenotazione):
        conferma_prenotazione.setObjectName("conferma_prenotazione")
        conferma_prenotazione.resize(400, 107)
        self.buttonBox = QtWidgets.QDialogButtonBox(conferma_prenotazione)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(conferma_prenotazione)
        self.label.setGeometry(QtCore.QRect(50, 30, 231, 41))
        self.label.setObjectName("label")

        self.retranslateUi(conferma_prenotazione)
        self.buttonBox.accepted.connect(conferma_prenotazione.accept) # type: ignore
        self.buttonBox.rejected.connect(conferma_prenotazione.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(conferma_prenotazione)

    def retranslateUi(self, conferma_prenotazione):
        _translate = QtCore.QCoreApplication.translate
        conferma_prenotazione.setWindowTitle(_translate("conferma_prenotazione", "Dialog"))
        self.label.setText(_translate("conferma_prenotazione", "<html><head/><body><p>Confermi la prenotazione per la data </p><p>e l\'orario selezionati?</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conferma_prenotazione = QtWidgets.QDialog()
    ui = Ui_conferma_prenotazione()
    ui.setupUi(conferma_prenotazione)
    conferma_prenotazione.show()
    sys.exit(app.exec_())