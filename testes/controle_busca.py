# controle_busca.py
from tela_busca import TelaBusca
from model import Model
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class ControleBusca(QMainWindow):
    def __init__(self, controle_principal):
        super().__init__()
        self.view = TelaBusca()
        self.model = Model()
        # Referência ao controlador principal
        self.controle_principal = controle_principal

        # Conectar o evento de clique na tabela
        self.view.tabela_clientes.itemClicked.connect(self.item_clicado)

    def mostrar_tela(self):
        # Carregar os dados dos clientes
        clientes = self.model.buscar_clientes()

        # Popular a tabela com os clientes
        self.view.tabela_clientes.setRowCount(len(clientes))
        for row, cliente in enumerate(clientes):
            self.view.tabela_clientes.setItem(row, 0, QTableWidgetItem(cliente[0]))
            self.view.tabela_clientes.setItem(row, 1, QTableWidgetItem(cliente[1]))

        self.view.show()

    def item_clicado(self, item):
        # Pega a linha do item clicado
        linha = item.row()
        nome = self.view.tabela_clientes.item(linha, 0).text()
        telefone = self.view.tabela_clientes.item(linha, 1).text()

        # Preenche os dados na tela principal
        self.controle_principal.preencher_dados_cliente(nome, telefone)

        # Fecha a tela de busca
        self.view.close()
