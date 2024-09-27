# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_novo_orcamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tela_novo_orcamento(object):
    def setupUi(self, tela_novo_orcamento):
        tela_novo_orcamento.setObjectName("tela_novo_orcamento")
        tela_novo_orcamento.resize(995, 591)
        self.novo_orcamento = QtWidgets.QWidget(tela_novo_orcamento)
        self.novo_orcamento.setEnabled(True)
        self.novo_orcamento.setObjectName("novo_orcamento")
        self.tabWidget_novo_orcamento = QtWidgets.QTabWidget(self.novo_orcamento)
        self.tabWidget_novo_orcamento.setEnabled(True)
        self.tabWidget_novo_orcamento.setGeometry(QtCore.QRect(9, 9, 651, 261))
        self.tabWidget_novo_orcamento.setStyleSheet("")
        self.tabWidget_novo_orcamento.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_novo_orcamento.setTabsClosable(False)
        self.tabWidget_novo_orcamento.setMovable(False)
        self.tabWidget_novo_orcamento.setTabBarAutoHide(False)
        self.tabWidget_novo_orcamento.setObjectName("tabWidget_novo_orcamento")
        self.tab_dados_cliente = QtWidgets.QWidget()
        self.tab_dados_cliente.setObjectName("tab_dados_cliente")
        self.pushButton_buscar_cliente = QtWidgets.QPushButton(self.tab_dados_cliente)
        self.pushButton_buscar_cliente.setGeometry(QtCore.QRect(220, 30, 41, 23))
        self.pushButton_buscar_cliente.setAutoFillBackground(False)
        self.pushButton_buscar_cliente.setObjectName("pushButton_buscar_cliente")
        self.lineEdit_data = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_data.setEnabled(False)
        self.lineEdit_data.setGeometry(QtCore.QRect(573, 28, 60, 20))
        self.lineEdit_data.setMinimumSize(QtCore.QSize(10, 0))
        self.lineEdit_data.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_data.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_data.setMaxLength(10)
        self.lineEdit_data.setFrame(False)
        self.lineEdit_data.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_data.setPlaceholderText("")
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.label_data = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_data.setGeometry(QtCore.QRect(540, 30, 31, 16))
        self.label_data.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_data.setObjectName("label_data")
        self.lineEdit_endereco_cliente = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_endereco_cliente.setGeometry(QtCore.QRect(10, 82, 190, 20))
        self.lineEdit_endereco_cliente.setText("")
        self.lineEdit_endereco_cliente.setObjectName("lineEdit_endereco_cliente")
        self.lineEdit_telefone_cliente = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_telefone_cliente.setGeometry(QtCore.QRect(280, 32, 90, 20))
        self.lineEdit_telefone_cliente.setText("")
        self.lineEdit_telefone_cliente.setObjectName("lineEdit_telefone_cliente")
        self.label_endereco_cliente = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_endereco_cliente.setGeometry(QtCore.QRect(10, 62, 51, 16))
        self.label_endereco_cliente.setObjectName("label_endereco_cliente")
        self.label_numero_cliente = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_numero_cliente.setGeometry(QtCore.QRect(220, 62, 45, 16))
        self.label_numero_cliente.setObjectName("label_numero_cliente")
        self.lineEdit_cidade_cliente = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_cidade_cliente.setGeometry(QtCore.QRect(430, 82, 160, 20))
        self.lineEdit_cidade_cliente.setText("")
        self.lineEdit_cidade_cliente.setObjectName("lineEdit_cidade_cliente")
        self.label_nome_cliente = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_nome_cliente.setGeometry(QtCore.QRect(10, 12, 90, 16))
        self.label_nome_cliente.setObjectName("label_nome_cliente")
        self.label_bairro_cliente = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_bairro_cliente.setGeometry(QtCore.QRect(280, 62, 41, 16))
        self.label_bairro_cliente.setObjectName("label_bairro_cliente")
        self.label_vendedor = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_vendedor.setGeometry(QtCore.QRect(390, 12, 121, 16))
        self.label_vendedor.setObjectName("label_vendedor")
        self.pushButton_editar_cliente = QtWidgets.QPushButton(self.tab_dados_cliente)
        self.pushButton_editar_cliente.setGeometry(QtCore.QRect(100, 200, 75, 23))
        self.pushButton_editar_cliente.setObjectName("pushButton_editar_cliente")
        self.lineEdit_bairro_cliente = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_bairro_cliente.setGeometry(QtCore.QRect(280, 82, 130, 20))
        self.lineEdit_bairro_cliente.setText("")
        self.lineEdit_bairro_cliente.setObjectName("lineEdit_bairro_cliente")
        self.comboBox_vendedores = QtWidgets.QComboBox(self.tab_dados_cliente)
        self.comboBox_vendedores.setGeometry(QtCore.QRect(390, 32, 130, 22))
        self.comboBox_vendedores.setObjectName("comboBox_vendedores")
        self.comboBox_vendedores.addItem("")
        self.lineEdit_numero_cliente = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_numero_cliente.setGeometry(QtCore.QRect(220, 82, 41, 20))
        self.lineEdit_numero_cliente.setText("")
        self.lineEdit_numero_cliente.setObjectName("lineEdit_numero_cliente")
        self.lineEdit_nome_cliente = QtWidgets.QLineEdit(self.tab_dados_cliente)
        self.lineEdit_nome_cliente.setGeometry(QtCore.QRect(10, 32, 190, 20))
        self.lineEdit_nome_cliente.setText("")
        self.lineEdit_nome_cliente.setObjectName("lineEdit_nome_cliente")
        self.label_cidade_cliente = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_cidade_cliente.setGeometry(QtCore.QRect(430, 62, 41, 16))
        self.label_cidade_cliente.setObjectName("label_cidade_cliente")
        self.pushButton_salvar_cliente = QtWidgets.QPushButton(self.tab_dados_cliente)
        self.pushButton_salvar_cliente.setGeometry(QtCore.QRect(10, 200, 75, 23))
        self.pushButton_salvar_cliente.setObjectName("pushButton_salvar_cliente")
        self.label_telefone_cliente = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_telefone_cliente.setGeometry(QtCore.QRect(280, 12, 50, 16))
        self.label_telefone_cliente.setObjectName("label_telefone_cliente")
        self.textEdit_observacoes = QtWidgets.QTextEdit(self.tab_dados_cliente)
        self.textEdit_observacoes.setGeometry(QtCore.QRect(10, 130, 581, 51))
        self.textEdit_observacoes.setObjectName("textEdit_observacoes")
        self.label_observacoes = QtWidgets.QLabel(self.tab_dados_cliente)
        self.label_observacoes.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_observacoes.setObjectName("label_observacoes")
        self.pushButton_cancelar = QtWidgets.QPushButton(self.tab_dados_cliente)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(190, 200, 75, 23))
        self.pushButton_cancelar.setAutoFillBackground(False)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.tabWidget_novo_orcamento.addTab(self.tab_dados_cliente, "")
        self.tableWidget = QtWidgets.QTableWidget(self.novo_orcamento)
        self.tableWidget.setGeometry(QtCore.QRect(10, 290, 971, 241))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton_incluir_produto = QtWidgets.QPushButton(self.novo_orcamento)
        self.pushButton_incluir_produto.setGeometry(QtCore.QRect(680, 90, 111, 23))
        self.pushButton_incluir_produto.setObjectName("pushButton_incluir_produto")
        self.label_produto = QtWidgets.QLabel(self.novo_orcamento)
        self.label_produto.setGeometry(QtCore.QRect(680, 30, 51, 16))
        self.label_produto.setObjectName("label_produto")
        self.comboBox_lista_produtos = QtWidgets.QComboBox(self.novo_orcamento)
        self.comboBox_lista_produtos.setGeometry(QtCore.QRect(680, 50, 301, 22))
        self.comboBox_lista_produtos.setObjectName("comboBox_lista_produtos")
        self.pushButton_excluir_produto = QtWidgets.QPushButton(self.novo_orcamento)
        self.pushButton_excluir_produto.setGeometry(QtCore.QRect(10, 550, 75, 23))
        self.pushButton_excluir_produto.setObjectName("pushButton_excluir_produto")
        tela_novo_orcamento.setCentralWidget(self.novo_orcamento)

        self.retranslateUi(tela_novo_orcamento)
        self.tabWidget_novo_orcamento.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tela_novo_orcamento)
        tela_novo_orcamento.setTabOrder(self.lineEdit_nome_cliente, self.lineEdit_telefone_cliente)
        tela_novo_orcamento.setTabOrder(self.lineEdit_telefone_cliente, self.comboBox_vendedores)
        tela_novo_orcamento.setTabOrder(self.comboBox_vendedores, self.lineEdit_endereco_cliente)
        tela_novo_orcamento.setTabOrder(self.lineEdit_endereco_cliente, self.lineEdit_numero_cliente)
        tela_novo_orcamento.setTabOrder(self.lineEdit_numero_cliente, self.lineEdit_bairro_cliente)
        tela_novo_orcamento.setTabOrder(self.lineEdit_bairro_cliente, self.lineEdit_cidade_cliente)
        tela_novo_orcamento.setTabOrder(self.lineEdit_cidade_cliente, self.textEdit_observacoes)
        tela_novo_orcamento.setTabOrder(self.textEdit_observacoes, self.pushButton_salvar_cliente)
        tela_novo_orcamento.setTabOrder(self.pushButton_salvar_cliente, self.pushButton_editar_cliente)
        tela_novo_orcamento.setTabOrder(self.pushButton_editar_cliente, self.pushButton_buscar_cliente)
        tela_novo_orcamento.setTabOrder(self.pushButton_buscar_cliente, self.pushButton_incluir_produto)
        tela_novo_orcamento.setTabOrder(self.pushButton_incluir_produto, self.lineEdit_data)

    def retranslateUi(self, tela_novo_orcamento):
        _translate = QtCore.QCoreApplication.translate
        tela_novo_orcamento.setWindowTitle(_translate("tela_novo_orcamento", "Novo Orçamento"))
        self.pushButton_buscar_cliente.setToolTip(_translate("tela_novo_orcamento", "Localizar Cliente"))
        self.pushButton_buscar_cliente.setText(_translate("tela_novo_orcamento", "Buscar"))
        self.lineEdit_data.setToolTip(_translate("tela_novo_orcamento", "Data"))
        self.lineEdit_data.setText(_translate("tela_novo_orcamento", "21/05/2020"))
        self.label_data.setText(_translate("tela_novo_orcamento", "Data:"))
        self.lineEdit_endereco_cliente.setToolTip(_translate("tela_novo_orcamento", "Endereço da Obra ou do Cliente"))
        self.lineEdit_telefone_cliente.setToolTip(_translate("tela_novo_orcamento", "Telefone para contato"))
        self.label_endereco_cliente.setText(_translate("tela_novo_orcamento", "Endereço:"))
        self.label_numero_cliente.setText(_translate("tela_novo_orcamento", "Numero:"))
        self.lineEdit_cidade_cliente.setToolTip(_translate("tela_novo_orcamento", "Cidade da Obra"))
        self.label_nome_cliente.setText(_translate("tela_novo_orcamento", "Nome do Cliente:"))
        self.label_bairro_cliente.setText(_translate("tela_novo_orcamento", "Bairro:"))
        self.label_vendedor.setText(_translate("tela_novo_orcamento", "Vendedor Responsável:"))
        self.pushButton_editar_cliente.setToolTip(_translate("tela_novo_orcamento", "Editar dados do Cliente"))
        self.pushButton_editar_cliente.setText(_translate("tela_novo_orcamento", "Editar"))
        self.lineEdit_bairro_cliente.setToolTip(_translate("tela_novo_orcamento", "Bairro da Obra"))
        self.comboBox_vendedores.setToolTip(_translate("tela_novo_orcamento", "Vendedor Responsável"))
        self.comboBox_vendedores.setPlaceholderText(_translate("tela_novo_orcamento", "Selecione o vendedor"))
        self.comboBox_vendedores.setItemText(0, _translate("tela_novo_orcamento", "Selecione o vendedor"))
        self.lineEdit_numero_cliente.setToolTip(_translate("tela_novo_orcamento", "Numero da Obra"))
        self.lineEdit_nome_cliente.setToolTip(_translate("tela_novo_orcamento", "Nome do Cliente"))
        self.label_cidade_cliente.setText(_translate("tela_novo_orcamento", "Cidade:"))
        self.pushButton_salvar_cliente.setToolTip(_translate("tela_novo_orcamento", "Salvar dados do Cliente"))
        self.pushButton_salvar_cliente.setText(_translate("tela_novo_orcamento", "Salvar"))
        self.label_telefone_cliente.setText(_translate("tela_novo_orcamento", "Telefone:"))
        self.textEdit_observacoes.setToolTip(_translate("tela_novo_orcamento", "Observações sobre o Orçamento"))
        self.label_observacoes.setText(_translate("tela_novo_orcamento", "Observações:"))
        self.pushButton_cancelar.setToolTip(_translate("tela_novo_orcamento", "Cancelar Cadastro de Cliente"))
        self.pushButton_cancelar.setText(_translate("tela_novo_orcamento", "Cancelar"))
        self.tabWidget_novo_orcamento.setTabText(self.tabWidget_novo_orcamento.indexOf(self.tab_dados_cliente), _translate("tela_novo_orcamento", "Dados do Cliente"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("tela_novo_orcamento", "linha 1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("tela_novo_orcamento", "linha 2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tela_novo_orcamento", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tela_novo_orcamento", "Descrição"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tela_novo_orcamento", "Cor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("tela_novo_orcamento", "Grade"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("tela_novo_orcamento", "Quant."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("tela_novo_orcamento", "Valor Unit"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("tela_novo_orcamento", "Valor Total"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("tela_novo_orcamento", "Branco"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("tela_novo_orcamento", "Sem grade"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("tela_novo_orcamento", "Preto"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("tela_novo_orcamento", "Com grade"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_incluir_produto.setText(_translate("tela_novo_orcamento", "Incluir Produto"))
        self.label_produto.setText(_translate("tela_novo_orcamento", "Produto:"))
        self.pushButton_excluir_produto.setToolTip(_translate("tela_novo_orcamento", "Salvar dados do Cliente"))
        self.pushButton_excluir_produto.setText(_translate("tela_novo_orcamento", "Excluir"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     tela_novo_orcamento = QtWidgets.QMainWindow()
#     ui = Ui_tela_novo_orcamento()
#     ui.setupUi(tela_novo_orcamento)
#     tela_novo_orcamento.show()
#     sys.exit(app.exec_())
