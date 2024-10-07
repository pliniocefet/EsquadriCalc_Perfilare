from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QDialog
from view.tela_buscar_cliente import Ui_Dialog_buscar_cliente
from model.model_cliente import ModelCliente


class ControleBuscarCliente(QDialog):

    def __init__(self, controle_principal):
        super().__init__()

        self.tela_buscar_cliente = Ui_Dialog_buscar_cliente()
        self.tela_buscar_cliente.setupUi(self)
        
        # Referencia para NovoControleNovoOrcamento
        self.controle_principal = controle_principal

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
        endereco = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 2).text()
        numero = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 3).text()
        bairro = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 4).text()
        cidade = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 5).text()
        telefone = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 6).text()
        observacoes = self.tela_buscar_cliente.tableWidget_clientes.item(linha, 7).text()

        for col in range(self.tela_buscar_cliente.tableWidget_clientes.columnCount()):
            item = self.tela_buscar_cliente.tableWidget_clientes.item(linha, col)

            if item is not None:
                self.row_itens.append(item.text())

            else:
                self.row_itens.append("")
                
        self.controle_principal.preenche_dados_cliente(nome, endereco, numero, bairro, cidade, telefone, observacoes)


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
                self.tela_buscar_cliente.tableWidget_clientes.setItem(row, column, QTableWidgetItem(str(data)))