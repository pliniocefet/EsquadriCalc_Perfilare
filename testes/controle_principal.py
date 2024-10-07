# controle_principal.py
from tela_principal import TelaPrincipal
from controle_busca import ControleBusca
from PyQt5.QtWidgets import QMainWindow

class ControlePrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = TelaPrincipal()  # Instancia a tela principal
        self.view.botao_buscar.clicked.connect(self.abrir_tela_busca)  # Conecta o botão ao método de busca

        # Inicializa a tela de busca
        self.controle_busca = ControleBusca(self)

    def abrir_tela_busca(self):
        self.controle_busca.mostrar_tela()

    def preencher_dados_cliente(self, nome, telefone):
        self.view.campo_nome.setText(nome)
        self.view.campo_telefone.setText(telefone)

    def mostrar_tela(self):
        self.view.show()
