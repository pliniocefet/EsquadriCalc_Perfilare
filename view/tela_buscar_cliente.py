# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_buscar_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_buscar_cliente(object):
    def setupUi(self, MainWindow_buscar_cliente):
        MainWindow_buscar_cliente.setObjectName("MainWindow_buscar_cliente")
        MainWindow_buscar_cliente.resize(655, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow_buscar_cliente)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_nome_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome_cliente.setGeometry(QtCore.QRect(20, 30, 401, 20))
        self.lineEdit_nome_cliente.setObjectName("lineEdit_nome_cliente")
        self.label_nome_cliente = QtWidgets.QLabel(self.centralwidget)
        self.label_nome_cliente.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nome_cliente.setFont(font)
        self.label_nome_cliente.setObjectName("label_nome_cliente")
        self.pushButton_buscar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_buscar_cliente.setGeometry(QtCore.QRect(440, 30, 75, 23))
        self.pushButton_buscar_cliente.setObjectName("pushButton_buscar_cliente")
        self.tableWidget_clientes = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_clientes.setGeometry(QtCore.QRect(20, 70, 611, 192))
        self.tableWidget_clientes.setObjectName("tableWidget_clientes")
        self.tableWidget_clientes.setColumnCount(6)
        self.tableWidget_clientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clientes.setHorizontalHeaderItem(5, item)
        self.pushButton_inserir_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inserir_cliente.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushButton_inserir_cliente.setObjectName("pushButton_inserir_cliente")
        self.pushButton_fechar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fechar.setGeometry(QtCore.QRect(550, 280, 75, 23))
        self.pushButton_fechar.setObjectName("pushButton_fechar")
        MainWindow_buscar_cliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_buscar_cliente)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_buscar_cliente)

    def retranslateUi(self, MainWindow_buscar_cliente):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_buscar_cliente.setWindowTitle(_translate("MainWindow_buscar_cliente", "MainWindow"))
        self.label_nome_cliente.setText(_translate("MainWindow_buscar_cliente", "Nome do Cliente:"))
        self.pushButton_buscar_cliente.setText(_translate("MainWindow_buscar_cliente", "Buscar"))
        item = self.tableWidget_clientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_buscar_cliente", "Nome"))
        item = self.tableWidget_clientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_buscar_cliente", "Endereço"))
        item = self.tableWidget_clientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_buscar_cliente", "Número"))
        item = self.tableWidget_clientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_buscar_cliente", "Bairro"))
        item = self.tableWidget_clientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_buscar_cliente", "Cidade"))
        item = self.tableWidget_clientes.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow_buscar_cliente", "Telefone"))
        self.pushButton_inserir_cliente.setText(_translate("MainWindow_buscar_cliente", "Inserir"))
        self.pushButton_fechar.setText(_translate("MainWindow_buscar_cliente", "Fechar"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow_buscar_cliente = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow_buscar_cliente()
#     ui.setupUi(MainWindow_buscar_cliente)
#     MainWindow_buscar_cliente.show()
#     sys.exit(app.exec_())
