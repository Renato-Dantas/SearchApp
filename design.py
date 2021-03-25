# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(910, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("background-color:rgb(30, 30, 30)")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 121, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 121, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 101, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btRegistro = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btRegistro.setMaximumSize(QtCore.QSize(16777215, 70))
        self.btRegistro.setStyleSheet("QPushButton{color: #fff;}\n"
"QPushButton:hover{ background-color: gold; color: black;font: 63 12pt \"Segoe UI Semibold\";}\n"
"")
        self.btRegistro.setObjectName("btRegistro")
        self.verticalLayout_2.addWidget(self.btRegistro)
        self.btConsulta = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btConsulta.setMaximumSize(QtCore.QSize(16777215, 70))
        self.btConsulta.setStyleSheet("QPushButton{color: #fff;}\n"
"QPushButton:hover{ background-color: gold; color: black;font: 63 12pt \"Segoe UI Semibold\";}")
        self.btConsulta.setObjectName("btConsulta")
        self.verticalLayout_2.addWidget(self.btConsulta)
        self.btUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btUpdate.setMaximumSize(QtCore.QSize(16777215, 70))
        self.btUpdate.setStyleSheet("QPushButton{color: #fff;}\n"
"QPushButton:hover{ background-color: gold; color: black;font: 63 12pt \"Segoe UI Semibold\";}")
        self.btUpdate.setObjectName("btUpdate")
        self.verticalLayout_2.addWidget(self.btUpdate)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(130, 10, 771, 711))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pgRegistro = QtWidgets.QWidget()
        self.pgRegistro.setObjectName("pgRegistro")
        self.label_2 = QtWidgets.QLabel(self.pgRegistro)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 651, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #fff; background-color: rgb(39,39,39); border-radius: 5px;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.pgRegistro)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 170, 681, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.iptId = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptId.setFont(font)
        self.iptId.setStyleSheet("background: white; color: black;")
        self.iptId.setAlignment(QtCore.Qt.AlignCenter)
        self.iptId.setObjectName("iptId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iptId)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.iptNome = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptNome.setFont(font)
        self.iptNome.setStyleSheet("background: white; color: black;")
        self.iptNome.setAlignment(QtCore.Qt.AlignCenter)
        self.iptNome.setObjectName("iptNome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iptNome)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.iptCidade = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptCidade.setFont(font)
        self.iptCidade.setStyleSheet("background: white; color: black;")
        self.iptCidade.setAlignment(QtCore.Qt.AlignCenter)
        self.iptCidade.setObjectName("iptCidade")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.iptCidade)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.iptEmail = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptEmail.setFont(font)
        self.iptEmail.setStyleSheet("background: white; color: black;")
        self.iptEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.iptEmail.setObjectName("iptEmail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.iptEmail)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.iptTelefone = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptTelefone.setFont(font)
        self.iptTelefone.setStyleSheet("background: white; color: black;")
        self.iptTelefone.setAlignment(QtCore.Qt.AlignCenter)
        self.iptTelefone.setObjectName("iptTelefone")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.iptTelefone)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.iptTelefone2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptTelefone2.setFont(font)
        self.iptTelefone2.setStyleSheet("background: white; color: black;")
        self.iptTelefone2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptTelefone2.setObjectName("iptTelefone2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.iptTelefone2)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.iptLink = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptLink.setFont(font)
        self.iptLink.setStyleSheet("background: white; color: black;")
        self.iptLink.setAlignment(QtCore.Qt.AlignCenter)
        self.iptLink.setObjectName("iptLink")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.iptLink)
        self.cbAreaRegistro = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAreaRegistro.sizePolicy().hasHeightForWidth())
        self.cbAreaRegistro.setSizePolicy(sizePolicy)
        self.cbAreaRegistro.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.cbAreaRegistro.setFont(font)
        self.cbAreaRegistro.setStyleSheet("QComboBox{background:white; color:black; font: 63 12pt \"Segoe UI Semibold\";}")
        self.cbAreaRegistro.setObjectName("cbAreaRegistro")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbAreaRegistro)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.pgRegistro)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 529, 681, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btSave = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btSave.setMinimumSize(QtCore.QSize(0, 50))
        self.btSave.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btSave.setStyleSheet("QPushButton{background: rgb(39,39,39); color: #fff; font: 63 10pt \"Segoe UI Semibold\";;}\n"
"\n"
"QPushButton:hover{ background-color: gold; color: rgb(0, 0, 127); font: 87 12pt \"Segoe UI Black\";}\n"
"")
        self.btSave.setObjectName("btSave")
        self.horizontalLayout.addWidget(self.btSave)
        self.btCancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btCancel.setMinimumSize(QtCore.QSize(0, 50))
        self.btCancel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btCancel.setStyleSheet("QPushButton{background: rgb(39,39,39); color: #fff;\n"
"    font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"QPushButton:hover{ background-color: rgb(166, 1, 1); color: white;\n"
"    font: 63 12pt \"Segoe UI Semibold\";}\n"
"")
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout.addWidget(self.btCancel)
        self.stackedWidget.addWidget(self.pgRegistro)
        self.pgConsulta = QtWidgets.QWidget()
        self.pgConsulta.setObjectName("pgConsulta")
        self.label_11 = QtWidgets.QLabel(self.pgConsulta)
        self.label_11.setGeometry(QtCore.QRect(60, 10, 651, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #fff; background-color: rgb(39,39,39); border-radius: 5px;")
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.scrollArea = QtWidgets.QScrollArea(self.pgConsulta)
        self.scrollArea.setGeometry(QtCore.QRect(30, 170, 721, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 721, 531))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        self.tableWidget.setStyleSheet("QTableWidget{background:rgb(44, 44, 44); \n"
"color: gold;\n"
"text-align: center;\n"
"\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.cbArea = QtWidgets.QComboBox(self.pgConsulta)
        self.cbArea.setGeometry(QtCore.QRect(30, 130, 491, 31))
        self.cbArea.setMinimumSize(QtCore.QSize(0, 10))
        self.cbArea.setStyleSheet("QComboBox{background:white; color:black; font: 63 12pt \"Segoe UI Semibold\";}")
        self.cbArea.setObjectName("cbArea")
        self.btConsultar = QtWidgets.QPushButton(self.pgConsulta)
        self.btConsultar.setGeometry(QtCore.QRect(540, 130, 211, 31))
        self.btConsultar.setStyleSheet("QPushButton{color: #fff;}\n"
"QPushButton:hover{ background-color: gold; color: black;font: 63 12pt \"Segoe UI Semibold\";}\n"
"")
        self.btConsultar.setObjectName("btConsultar")
        self.stackedWidget.addWidget(self.pgConsulta)
        self.pgUpdate = QtWidgets.QWidget()
        self.pgUpdate.setObjectName("pgUpdate")
        self.label_12 = QtWidgets.QLabel(self.pgUpdate)
        self.label_12.setGeometry(QtCore.QRect(60, 10, 651, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #fff; background-color: rgb(39,39,39); border-radius: 5px;")
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.pgUpdate)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(50, 200, 681, 301))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.iptId_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptId_2.setFont(font)
        self.iptId_2.setStyleSheet("background: white; color: black;")
        self.iptId_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptId_2.setObjectName("iptId_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iptId_2)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.iptNome_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptNome_2.setFont(font)
        self.iptNome_2.setStyleSheet("background: white; color: black;")
        self.iptNome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptNome_2.setObjectName("iptNome_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iptNome_2)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.iptCidade_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptCidade_2.setFont(font)
        self.iptCidade_2.setStyleSheet("background: white; color: black;")
        self.iptCidade_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptCidade_2.setObjectName("iptCidade_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.iptCidade_2)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.iptEmail_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptEmail_2.setFont(font)
        self.iptEmail_2.setStyleSheet("background: white; color: black;")
        self.iptEmail_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptEmail_2.setObjectName("iptEmail_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.iptEmail_2)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.iptTelefone_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptTelefone_2.setFont(font)
        self.iptTelefone_2.setStyleSheet("background: white; color: black;")
        self.iptTelefone_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptTelefone_2.setObjectName("iptTelefone_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.iptTelefone_2)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_19.setFrameShape(QtWidgets.QFrame.Box)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.iptTelefone2_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptTelefone2_2.setFont(font)
        self.iptTelefone2_2.setStyleSheet("background: white; color: black;")
        self.iptTelefone2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptTelefone2_2.setObjectName("iptTelefone2_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.iptTelefone2_2)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel{color: #fff; background: rgb(39,39,39);}")
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.iptLink_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.iptLink_2.setFont(font)
        self.iptLink_2.setStyleSheet("background: white; color: black;")
        self.iptLink_2.setAlignment(QtCore.Qt.AlignCenter)
        self.iptLink_2.setObjectName("iptLink_2")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.iptLink_2)
        self.cbAreaUpdate = QtWidgets.QComboBox(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAreaUpdate.sizePolicy().hasHeightForWidth())
        self.cbAreaUpdate.setSizePolicy(sizePolicy)
        self.cbAreaUpdate.setMinimumSize(QtCore.QSize(0, 10))
        self.cbAreaUpdate.setStyleSheet("QComboBox{background:white; color:black; font: 63 12pt \"Segoe UI Semibold\";}\n"
"")
        self.cbAreaUpdate.setObjectName("cbAreaUpdate")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbAreaUpdate)
        self.cbName = QtWidgets.QComboBox(self.pgUpdate)
        self.cbName.setGeometry(QtCore.QRect(50, 140, 461, 31))
        self.cbName.setMinimumSize(QtCore.QSize(0, 10))
        self.cbName.setStyleSheet("QComboBox{background:white; color:black; font: 63 12pt \"Segoe UI Semibold\";}")
        self.cbName.setObjectName("cbName")
        self.cbName.addItem("")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.pgUpdate)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 540, 681, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btSaveUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btSaveUpdate.setMinimumSize(QtCore.QSize(0, 50))
        self.btSaveUpdate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btSaveUpdate.setStyleSheet("QPushButton{background: rgb(39,39,39); color: #fff; font: 63 10pt \"Segoe UI Semibold\";;}\n"
"\n"
"QPushButton:hover{ background-color: gold; color: rgb(0, 0, 127); font: 87 12pt \"Segoe UI Black\";}")
        self.btSaveUpdate.setObjectName("btSaveUpdate")
        self.horizontalLayout_2.addWidget(self.btSaveUpdate)
        self.btCancelUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btCancelUpdate.setMinimumSize(QtCore.QSize(0, 50))
        self.btCancelUpdate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btCancelUpdate.setStyleSheet("QPushButton{background: rgb(39,39,39); color: #fff;\n"
"    font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"QPushButton:hover{ background-color: rgb(166, 1, 1); color: white;\n"
"    font: 63 12pt \"Segoe UI Semibold\";}")
        self.btCancelUpdate.setObjectName("btCancelUpdate")
        self.horizontalLayout_2.addWidget(self.btCancelUpdate)
        self.btConsultar_2 = QtWidgets.QPushButton(self.pgUpdate)
        self.btConsultar_2.setGeometry(QtCore.QRect(520, 140, 211, 31))
        self.btConsultar_2.setStyleSheet("QPushButton{color: #fff;}\n"
"QPushButton:hover{ background-color: gold; color: black;font: 63 12pt \"Segoe UI Semibold\";}\n"
"")
        self.btConsultar_2.setObjectName("btConsultar_2")
        self.stackedWidget.addWidget(self.pgUpdate)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.label.setText(_translate("Main", "Páginas"))
        self.btRegistro.setText(_translate("Main", "Registro"))
        self.btConsulta.setText(_translate("Main", "Consulta"))
        self.btUpdate.setText(_translate("Main", "Update"))
        self.label_2.setText(_translate("Main", "Registro de Fonecedor"))
        self.label_3.setText(_translate("Main", "Código Mirallis:"))
        self.label_4.setText(_translate("Main", "Nome Fornecedor:"))
        self.label_5.setText(_translate("Main", "Área de Atuação:"))
        self.label_6.setText(_translate("Main", "Cidade:"))
        self.label_7.setText(_translate("Main", "E-mail:"))
        self.label_8.setText(_translate("Main", "Telefone:"))
        self.label_9.setText(_translate("Main", "Telefone 2:"))
        self.label_10.setText(_translate("Main", "Link Website:"))
        self.btSave.setText(_translate("Main", "Save"))
        self.btCancel.setText(_translate("Main", "Cancel"))
        self.label_11.setText(_translate("Main", "Consulta de Fornecedores"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Main", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Main", "Área"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Main", "Cidade"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Main", "E-Mail"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Main", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Main", "Telefone 2"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Main", "Website"))
        self.btConsultar.setText(_translate("Main", "Consultar"))
        self.label_12.setText(_translate("Main", "Update de Informações"))
        self.label_13.setText(_translate("Main", "Código Mirallis:"))
        self.label_14.setText(_translate("Main", "Nome Fornecedor:"))
        self.label_15.setText(_translate("Main", "Área de Atuação:"))
        self.label_16.setText(_translate("Main", "Cidade:"))
        self.label_17.setText(_translate("Main", "E-mail:"))
        self.label_18.setText(_translate("Main", "Telefone:"))
        self.label_19.setText(_translate("Main", "Telefone 2:"))
        self.label_20.setText(_translate("Main", "Link Website:"))
        self.cbName.setCurrentText(_translate("Main", "Escolha um fornecedor para atualizar"))
        self.cbName.setItemText(0, _translate("Main", "Escolha um fornecedor para atualizar"))
        self.btSaveUpdate.setText(_translate("Main", "Save"))
        self.btCancelUpdate.setText(_translate("Main", "Cancel"))
        self.btConsultar_2.setText(_translate("Main", "Consultar"))
