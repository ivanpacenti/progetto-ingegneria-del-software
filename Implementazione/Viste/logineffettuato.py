# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logineffettuato.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Implementazione.Gestione.GestoreUtente import GestoreUtente


class Ui_logineffettuato(object):
    def setupUi(self, logineffettuato):
        logineffettuato.setObjectName("logineffettuato")
        logineffettuato.resize(400, 110)
        self.buttonBox = QtWidgets.QDialogButtonBox(logineffettuato)
        self.buttonBox.setGeometry(QtCore.QRect(10, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(logineffettuato)
        self.label.setGeometry(QtCore.QRect(120, 20, 201, 20))
        self.label.setObjectName("label")

        self.retranslateUi(logineffettuato)
        self.buttonBox.accepted.connect(logineffettuato.accept) # type: ignore
        self.buttonBox.rejected.connect(logineffettuato.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(logineffettuato)

    def retranslateUi(self, logineffettuato):
        _translate = QtCore.QCoreApplication.translate
        logineffettuato.setWindowTitle(_translate("logineffettuato", "Dialog"))
        if (GestoreUtente.loginEffettuato==True):
            self.label.setText(_translate("logineffettuato", "Login effettuato con successo"))
        else:
            self.label.setText(_translate("logineffettuato", "Logout effettuato con successo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    logineffettuato = QtWidgets.QDialog()
    ui = Ui_logineffettuato()
    ui.setupUi(logineffettuato)
    logineffettuato.show()
    sys.exit(app.exec_())
