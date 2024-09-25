# TODO criar este modulo

from PyQt5.QtWidgets import QMainWindow
from view.tela_cadastro_vendedores import Ui_tela_cadastro_vendedor

class ControleCadastroVendedor(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE CADASTRO DE VENDEDORES
        self.tela_cadastro_vendedores = Ui_tela_cadastro_vendedor()
        self.tela_cadastro_vendedores.setupUi(self)