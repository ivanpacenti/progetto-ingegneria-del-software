# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Implementazione.Viste.login import Login
from Implementazione.Viste.registrazione_socio import Ui_registrazionesocio
from Implementazione.Gestione.GestoreUtente import GestoreUtente
from Implementazione.Viste.gestione_organizzazione import Ui_gestioneOrganizzazione

class Ui_Form(object):
    def gestioneUtente(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Login()
        self.ui.setupUi(self.window)
        self.window.show()

    def gestioneTesseramento(self):
        if GestoreUtente.loginEffettuato == True:
            self.window=QtWidgets.QWidget()
            self.ui=Ui_registrazionesocio()
            self.ui.setupUi(self.window)
            self.window.show()

    def gestioneOrganizzazione(self):
        if (GestoreUtente.loginEffettuato == True and GestoreUtente.utenteConnesso.isAdmin == True):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_gestioneOrganizzazione()
            self.ui.setupUi(self.window)
            self.window.show()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 405)
        self.gestioneprenotazioni = QtWidgets.QPushButton(Form)
        self.gestioneprenotazioni.setGeometry(QtCore.QRect(20, 30, 171, 111))
        self.gestioneprenotazioni.setObjectName("gestionePrenotazioni")
        self.gestioneutente = QtWidgets.QPushButton(Form)
        self.gestioneutente.setGeometry(QtCore.QRect(210, 30, 171, 111))
        self.gestioneutente.setObjectName("gestioneUtente")
        self.gestionetesseramento = QtWidgets.QPushButton(Form)
        self.gestionetesseramento.setGeometry(QtCore.QRect(20, 160, 171, 111))
        self.gestionetesseramento.setObjectName("gestioneTesseramento")
        self.gestionetorneo = QtWidgets.QPushButton(Form)
        self.gestionetorneo.setGeometry(QtCore.QRect(210, 160, 171, 111))
        self.gestionetorneo.setObjectName("gestioneTorneo")
        self.gestioneorganizzazione = QtWidgets.QPushButton(Form)
        self.gestioneorganizzazione.setGeometry(QtCore.QRect(50, 290, 301, 111))
        self.gestioneorganizzazione.setObjectName("gestioneOrganizzazione")

        #azioni dei pulsanti
        self.gestioneutente.clicked.connect(self.gestioneUtente)
        self.gestionetesseramento.clicked.connect(self.gestioneTesseramento)
        self.gestioneorganizzazione.clicked.connect(self.gestioneOrganizzazione)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gestioneprenotazioni.setText(_translate("Form", "Gestione Prenotazioni"))
        self.gestioneutente.setText(_translate("Form", "Gestione Utente"))
        self.gestionetesseramento.setText(_translate("Form", "Gestione Tesseramento"))
        self.gestionetorneo.setText(_translate("Form", "Gestione Torneo"))
        self.gestioneorganizzazione.setText(_translate("Form", "Gestione Organizzazione"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
