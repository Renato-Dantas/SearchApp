#pyuic5 mirallisDesign.ui -o mirallisDesign.py
from sys import argv
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_Main
from sqlStructure import sqliteFunctions


class main(QMainWindow, Ui_Main, sqliteFunctions):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        super()

        self.btRegistro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgRegistro))
        self.btConsulta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgConsulta))
        self.btUpdate.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgUpdate))

        self.btSave.clicked.connect(self.get_info)
        self.btCancel.clicked.connect(self.cancelAction)

    # Função que apaga os campos preenchidos caso o botão "Cancel" seja clicado
    def cancelAction(self):
        self.iptId.setText('')
        self.iptNome.setText('')
        self.iptArea.setText('')
        self.iptCidade.setText('')
        self.iptEmail.setText('')
        self.iptTelefone.setText('')
        self.iptTelefone2.setText('')
        self.iptLink.setText('')
        self.selectAllData()

    # Função que pega os dados inseridos no formulário - Futuramente os dados serão enviados a um bando SQLite
    def get_info(self):
        cod = self.iptId.text()
        nome = self.iptNome.text()
        area = self.iptArea.text()
        cidade = self.iptCidade.text()
        email = self.iptEmail.text()
        fone1 = self.iptTelefone.text()
        fone2 = self.iptTelefone2.text()
        link = self.iptLink.text()

        print(f'Código: {cod}\nArea: {area}\nCidade: {cidade}\nEmail: {email}\nFone: {fone1}\nFone2: {fone2}\nLink: {link}')
        info = [cod, nome, area, cidade, email, fone1, fone2, link]
        self.insertValues(info)

if __name__ == '__main__':
    qt = QApplication(argv)
    screen = main()
    screen.show()
    qt.exec_()