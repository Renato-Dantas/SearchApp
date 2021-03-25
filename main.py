#pyuic5 design.ui -o design.py
from sys import argv
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QTableWidgetItem, QMessageBox
from design import Ui_Main
from sqlStructure import sqliteFunctions

class main(QMainWindow, Ui_Main, sqliteFunctions):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        super()

        self.sql = sqliteFunctions()

        self.btRegistro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgRegistro))
        self.btConsulta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgConsulta))
        self.btUpdate.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgUpdate))
        

        self.btSave.clicked.connect(self.saveInfo)
        self.btCancel.clicked.connect(self.cancelAction)

        self.btConsultar.clicked.connect(self.showTable)
        self.btConsultar_2.clicked.connect(self.consultarUpdate)
        self.btCancelUpdate.clicked.connect(self.cancelActionUpdate)
        self.btSaveUpdate.clicked.connect(self.infoUpdate)

        areaList = self.sql.readTxt()        
        for area in areaList:
            self.cbArea.addItem(area)
            self.cbAreaRegistro.addItem(area)
            self.cbAreaUpdate.addItem(area)

        nameList = self.sql.searchListNames()
        for name in nameList:
            self.cbName.addItem(str(name[0]))

        
    def showTable(self):
        area = self.cbArea.currentText()
        data = self.sql.searchSqlArea(area)
        registros = []
        for reg in data:
            reg = list(reg)
            registros.append(reg)       
        row = 0
        index = 0
        self.tableWidget.setRowCount(len(registros))
        for registro in data:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(registros[index][0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(registros[index][1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(registros[index][2]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(registros[index][3]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(registros[index][4]))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(registros[index][5]))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(registros[index][6]))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(registros[index][7]))
            row +=1
            index +=1

    # Função que apaga os campos preenchidos caso o botão "Cancel" seja clicado
    def cancelAction(self):
        self.iptId.setText('')
        self.iptNome.setText('')
        self.cbAreaRegistro.setCurrentIndex(0)
        self.iptCidade.setText('')
        self.iptEmail.setText('')
        self.iptTelefone.setText('')
        self.iptTelefone2.setText('')
        self.iptLink.setText('')
        self.sql.selectAllData()

    def cancelActionUpdate(self):
        self.iptId_2.setText('')
        self.iptNome_2.setText('')
        self.cbAreaUpdate.setCurrentIndex(0)
        self.iptCidade_2.setText('')
        self.iptEmail_2.setText('')
        self.iptTelefone_2.setText('')
        self.iptTelefone2_2.setText('')
        self.iptLink_2.setText('')


    # Função que pega os dados inseridos no formulário - Futuramente os dados serão enviados a um bando SQLite
    def saveInfo(self):
        cod = self.iptId.text()
        nome = self.iptNome.text()
        area = self.cbAreaRegistro.currentText()
        cidade = self.iptCidade.text()
        email = self.iptEmail.text()
        fone1 = self.iptTelefone.text()
        fone2 = self.iptTelefone2.text()
        link = self.iptLink.text()

        print(f'Código: {cod}\nArea: {area}\nCidade: {cidade}\nEmail: {email}\nFone: {fone1}\nFone2: {fone2}\nLink: {link}')
        info = [cod, nome, area, cidade, email, fone1, fone2, link]
        self.sql.insertValues(info)
        self.popup('Fornecedor Registrado com sucesso!')


    def consultarUpdate(self):
        nome = self.cbName.currentText()
        data = self.sql.searchSqlName(nome)
        data = list(data[0])
        self.iptId_2.setText(str(data[0]))
        self.iptNome_2.setText(data[1])
        self.cbAreaUpdate.setCurrentText(data[2])
        self.iptCidade_2.setText(data[3])
        self.iptEmail_2.setText(data[4])
        self.iptTelefone_2.setText(data[5])
        self.iptTelefone2_2.setText(data[6])
        self.iptLink_2.setText(data[7])

    def infoUpdate(self):
        nome_atual = self.cbName.currentText()
        cod = self.iptId_2.text()
        nome = self.iptNome_2.text()
        area = self.cbAreaUpdate.currentText()
        cidade = self.iptCidade_2.text()
        email = self.iptEmail_2.text()
        fone1 = self.iptTelefone_2.text()
        fone2 = self.iptTelefone2_2.text()
        link = self.iptLink_2.text()
        info = [cod, nome, area, cidade, email, fone1, fone2, link, nome_atual]
        self.sql.updateData(info)
        self.popup('Dados Atualizados com sucesso!')

    def popup(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Saved!")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


if __name__ == '__main__':
    qt = QApplication(argv)
    screen = main()
    screen.show()
    qt.exec_()

