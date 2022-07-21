# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrazione_utente.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from Implementazione.Generali.Utente import Utente
from Implementazione.Gestione.GestoreUtenti import GestoreUtenti
from Implementazione.Viste.confermaiscrizione import Ui_ConfermaIscrizione
from Implementazione.Viste.erroreiscrizione import Ui_erroreiscrizione

class UI_Iscrizione(object):

    def creaUtente(self):
        if(self.nome.text() !="" and self.cognome.text()!= "" and self.nomeUtente.text()!= "" and self.password.text() != "" and self.cellulare.text() != ""and self.dataNascita.text() != ""):
            campoNome=self.nome.text()
            campoCognome=self.cognome.text()
            campoNomeUtente=self.nomeUtente.text()
            campoPassword=self.password.text()
            campoCellulare=self.cellulare.text()
            campoDataNascita=self.dataNascita.text()
            nuovoUtente=Utente(campoNome,campoCognome,campoDataNascita,campoCellulare,campoPassword,campoNomeUtente)
            GestoreUtenti.inserisciUtente(nuovoUtente)
            self.window_conferma = QtWidgets.QDialog()
            self.ui_conferma = Ui_ConfermaIscrizione()
            self.ui_conferma.setupUi(self.window_conferma)
            self.window_conferma.show()
        else:
            self.popupEI()


    def popupEI(self):
        self.window_eiscrizione = QtWidgets.QDialog()
        self.ui_eiscrizione = Ui_erroreiscrizione()
        self.ui_eiscrizione.setupUi(self.window_eiscrizione)
        self.window_eiscrizione.show()


    def modificaUtente(self):
        campoNome = self.nome.text()
        campoCognome = self.cognome.text()
        campoNomeUtente = self.nomeUtente.text()
        campoPassword = self.password.text()
        campoCellulare = self.cellulare.text()
        campoDataNascita = self.dataNascita.text()
        utenteModificato=Utente(campoNome,campoCognome,campoDataNascita,campoCellulare,campoPassword,campoNomeUtente)
        GestoreUtenti.modificaUtente(GestoreUtenti.utenteConnesso,utenteModificato)
        self.window_conferma = QtWidgets.QDialog()
        self.ui_conferma = Ui_ConfermaIscrizione()
        self.ui_conferma.setupUi(self.window_conferma)
        self.window_conferma.show()

    def modificaUtente(self,idUtente):
        campoNome = self.nome.text()
        campoCognome = self.cognome.text()
        campoNomeUtente = self.nomeUtente.text()
        campoPassword = self.password.text()
        campoCellulare = self.cellulare.text()
        campoDataNascita = self.dataNascita.text()
        utenteModificato=Utente(campoNome,campoCognome,campoDataNascita,campoCellulare,campoPassword,campoNomeUtente)
        GestoreUtenti.modificaUtente(GestoreUtenti.collectionUtenti[idUtente+2],utenteModificato)
        self.window_conferma = QtWidgets.QDialog()
        self.ui_conferma = Ui_ConfermaIscrizione()
        self.ui_conferma.setupUi(self.window_conferma)
        self.window_conferma.show()





    def setupUi(self, Iscrizione,idUtente):
        Iscrizione.setObjectName("Iscrizione")
        Iscrizione.resize(400, 300)
        self.label_3 = QtWidgets.QLabel(Iscrizione)
        self.label_3.setGeometry(QtCore.QRect(59, 90, 81, 20))
        self.label_3.setObjectName("label_3")
        self.cognome = QtWidgets.QLineEdit(Iscrizione)
        self.cognome.setGeometry(QtCore.QRect(150, 60, 141, 21))
        self.cognome.setObjectName("cognome")
        self.label = QtWidgets.QLabel(Iscrizione)
        self.label.setGeometry(QtCore.QRect(100, 30, 41, 16))
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(Iscrizione)
        self.password.setGeometry(QtCore.QRect(150, 120, 141, 21))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(Iscrizione)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.nomeUtente = QtWidgets.QLineEdit(Iscrizione)
        self.nomeUtente.setGeometry(QtCore.QRect(150, 90, 141, 21))
        self.nomeUtente.setObjectName("nomeUtente")
        self.nome = QtWidgets.QLineEdit(Iscrizione)
        self.nome.setGeometry(QtCore.QRect(150, 30, 141, 21))
        self.nome.setObjectName("nome")
        self.dataNascita = QtWidgets.QLineEdit(Iscrizione)
        self.dataNascita.setGeometry(QtCore.QRect(150, 180, 141, 21))
        self.dataNascita.setObjectName("dataNascita")
        self.label_5 = QtWidgets.QLabel(Iscrizione)
        self.label_5.setGeometry(QtCore.QRect(80, 150, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Iscrizione)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 60, 16))
        self.label_4.setObjectName("label_4")
        self.invia = QtWidgets.QPushButton(Iscrizione)
        self.invia.setGeometry(QtCore.QRect(150, 220, 113, 32))
        self.invia.setFlat(False)
        self.invia.setObjectName("invia")
        self.label_6 = QtWidgets.QLabel(Iscrizione)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 101, 20))
        self.label_6.setObjectName("label_6")
        self.cellulare = QtWidgets.QLineEdit(Iscrizione)
        self.cellulare.setGeometry(QtCore.QRect(150, 150, 141, 21))
        self.cellulare.setObjectName("cellulare")
        if(GestoreUtenti.loginEffettuato and GestoreUtenti.utenteConnesso.isAdmin==False):
            self.nome.setText(GestoreUtenti.utenteConnesso.nome)
            self.cognome.setText(GestoreUtenti.utenteConnesso.cognome)
            self.dataNascita.setText(GestoreUtenti.utenteConnesso.dataNascita)
            self.password.setText(GestoreUtenti.utenteConnesso.password)
            self.nomeUtente.setText(GestoreUtenti.utenteConnesso.nomeUtente)
            self.cellulare.setText(GestoreUtenti.utenteConnesso.cellulare)
            self.invia.clicked.connect(self.modificaUtente)
        elif(GestoreUtenti.loginEffettuato and GestoreUtenti.utenteConnesso.isAdmin==True):
            self.nome.setText(GestoreUtenti.collectionUtenti[idUtente].nome)
            self.cognome.setText(GestoreUtenti.collectionUtenti[idUtente].cognome)
            self.dataNascita.setText(GestoreUtenti.collectionUtenti[idUtente].dataNascita)
            self.password.setText(GestoreUtenti.collectionUtenti[idUtente].password)
            self.nomeUtente.setText(GestoreUtenti.collectionUtenti[idUtente].nomeUtente)
            self.cellulare.setText(GestoreUtenti.collectionUtenti[idUtente].cellulare)
            self.invia.clicked.connect(self.modificaUtente)
        else:
            self.invia.clicked.connect(self.creaUtente)

        Iscrizione.setTabOrder(self.nome, self.cognome)
        Iscrizione.setTabOrder(self.cognome, self.nomeUtente)
        Iscrizione.setTabOrder(self.nomeUtente, self.password)
        Iscrizione.setTabOrder(self.password, self.cellulare)
        Iscrizione.setTabOrder(self.cellulare, self.dataNascita)
        self.retranslateUi(Iscrizione)
        QtCore.QMetaObject.connectSlotsByName(Iscrizione)

    def retranslateUi(self, Iscrizione):
        _translate = QtCore.QCoreApplication.translate
        Iscrizione.setWindowTitle(_translate("Iscrizione", "Form"))
        self.label_3.setText(_translate("Iscrizione", "Nome Utente"))
        self.label.setText(_translate("Iscrizione", "Nome"))
        self.label_2.setText(_translate("Iscrizione", "Cognome"))
        self.label_4.setText(_translate("Iscrizione", "Password"))
        self.label_6.setText(_translate("Iscrizione", "Data di nascita"))
        self.invia.setText(_translate("Iscrizione", "Invia"))
        self.label_5.setText(_translate("Iscrizione", "Cellulare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Iscrizione = QtWidgets.QWidget()
    ui = Iscrizione()
    ui.setupUi(Iscrizione)
    Iscrizione.show()
    sys.exit(app.exec_())
