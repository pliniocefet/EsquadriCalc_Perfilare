from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from view.tela_buscar_cliente import Ui_Dialog_buscar_cliente
from view.tela_novo_orcamento import Ui_tela_novo_orcamento
from model.model_cliente import ModelCliente
from model.model_vendedor import ModelVendedor


class NovoControleNovoOrcamento(QMainWindow):
    """ 
        Classe que controla a tela de novo orçamento
        Janela Principal de Controle
    """

    def __init__(self):
        super().__init__()
        self.novo_orcamento = Ui_tela_novo_orcamento()
        self.novo_orcamento.setupUi(self)

        
        # VARIAVEIS UTILITÁRIAS
        self.combo_vendedores = None

        self.recebe_busca = None

        ### ESTADO DOS BOTÕES ###
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)

        self.preenche_combo_vendedores()

        ### AÇÕES DOS BOTÕES ###
        self.novo_orcamento.pushButton_buscar_cliente.clicked.connect(
            self.buscar_cliente)
        self.novo_orcamento.pushButton_cancelar.clicked.connect(
            self.cancelar_orcamento)
        self.novo_orcamento.pushButton_salvar_cliente.clicked.connect(
            self.salvar_cliente)
        self.novo_orcamento.pushButton_editar_cliente.clicked.connect(
            self.editar_cliente)

        self.novo_orcamento.pushButton_novo_cliente.clicked.connect(
            self.novo_cliente)

        # Condição de funcionamento dos botões
        if self.novo_orcamento.lineEdit_nome_cliente.text() == "":
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(False)
        else:
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)

    def preenche_combo_vendedores(self):
        self.vendedor = ModelVendedor()
        self.combo_vendedores = self.vendedor.list_vendedores()

        # Preenche o comboBox de vendedores com as informações do banco de dados
        for vendedor in self.combo_vendedores:
            self.novo_orcamento.comboBox_vendedores.addItem(vendedor[1])

    def buscar_cliente(self):
        self.controle_buscar_cliente = NovoControleBuscarCliente(self)
        self.controle_buscar_cliente.show()

    def cancelar_orcamento(self):
        self.novo_orcamento.lineEdit_nome_cliente.clear()
        self.novo_orcamento.lineEdit_endereco_cliente.clear()
        self.novo_orcamento.lineEdit_numero_cliente.clear()
        self.novo_orcamento.lineEdit_bairro_cliente.clear()
        self.novo_orcamento.lineEdit_cidade_cliente.clear()
        self.novo_orcamento.lineEdit_telefone_cliente.clear()
        self.novo_orcamento.textEdit_observacoes.clear()
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.close()

    def salvar_cliente(self):
        nome_cliente = self.novo_orcamento.lineEdit_nome_cliente.text()
        endereco_cliente = self.novo_orcamento.lineEdit_endereco_cliente.text()
        numero_cliente = self.novo_orcamento.lineEdit_numero_cliente.text()
        bairro_cliente = self.novo_orcamento.lineEdit_bairro_cliente.text()
        cidade_cliente = self.novo_orcamento.lineEdit_cidade_cliente.text()
        telefone_cliente = self.novo_orcamento.lineEdit_telefone_cliente.text()
        observacoes_cliente = self.novo_orcamento.textEdit_observacoes.toPlainText()

#       TODO FAZER UMA VERIFICAÇÃO PARA NÃO SALVAR CLIENTES EM BRANCO

        self.modelCliente = ModelCliente()
        self.modelCliente.insert_cliente(nome_cliente, endereco_cliente, numero_cliente,
                                         bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente)

        self.menssagem('Cadastro Realizado com Sucesso!')
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(False)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(True)
        self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)
        self.novo_orcamento.lineEdit_nome_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_telefone_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_endereco_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_numero_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_bairro_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_cidade_cliente.setEnabled(False)
        self.novo_orcamento.textEdit_observacoes.setEnabled(False)
        self.novo_orcamento.comboBox_vendedores.setEnabled(False)

    def editar_cliente(self):
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)

    def novo_cliente(self):
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_nome_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_telefone_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_endereco_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_numero_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_bairro_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_cidade_cliente.setEnabled(True)
        self.novo_orcamento.textEdit_observacoes.setEnabled(True)
        # self.novo_orcamento.comboBox_vendedores.setEnabled(True)

    ### MESSAGEBOX ###
    def menssagem(self, menssagem):
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle('Information')
        self.msg_box.setText(menssagem)
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.exec_()

    def preenche_dados_cliente(self, nome_cliente):
        self.novo_orcamento.lineEdit_nome_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_nome_cliente.setText(nome_cliente)



class NovoControleBuscarCliente(QDialog):
    """
            Janela secundária para buscar clientes

    """
    def __init__(self, controle_principal):
        super().__init__()

        self.tela_buscar_cliente = Ui_Dialog_buscar_cliente()
        self.tela_buscar_cliente.setupUi(self)
        
        # Referencia para NovoControleNovoOrcamento
        self.controle_principal = controle_principal

    # TODO: encontrar uma forma de capturar o cliente da tela_buscar_cliente para trazer para a tela_novo_orcamento
        self.row_itens = []

    # preecher a tabela de clientes ao abrir a tela
        self.preenche_tabela()

    # AÇÕES DE BOTÕES E TABELA
    # captura informações da tabela de acordo com o item clicado
        self.tela_buscar_cliente.tableWidget_clientes.itemClicked.connect(
            self.captura_cliente)

        self.tela_buscar_cliente.pushButton_fechar.clicked.connect(self.close)
        self.tela_buscar_cliente.pushButton_buscar_cliente.clicked.connect(
            self.bt_buscar)
        self.tela_buscar_cliente.pushButton_inserir_cliente.clicked.connect(
            self.bt_inserir)
        

    def bt_buscar(self):
        pass

    def bt_inserir(self):
        pass

    def captura_cliente(self, item):

        linha = item.row()
        nome = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 1).text()

        for col in range(self.tela_buscar_cliente.tableWidget_clientes.columnCount()):
            item = self.tela_buscar_cliente.tableWidget_clientes.item(linha, col)

            if item is not None:
                self.row_itens.append(item.text())

            else:
                self.row_itens.append("")
                
        self.controle_principal.preenche_dados_cliente(nome)


        self.close()

    def preenche_tabela(self):
        self.model_cliente = ModelCliente()
        clientes = self.model_cliente.list_clientes()

    # Para descobrir o numero de linhas
        self.tela_buscar_cliente.tableWidget_clientes.setRowCount(len(clientes))

    # Primeiro FOR cria as linhas da tabela
        for row, text in enumerate(clientes):
            # Segundo for preenche a linha com o conteudo do banco de acordo com cada coluna
            # str(data) -> converte todo o conteudo do banco para string
            for column, data in enumerate(text):
                self.tela_buscar_cliente.tableWidget_clientes.setItem(
                    row, column, QTableWidgetItem(str(data)))
