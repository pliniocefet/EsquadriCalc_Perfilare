# TODO criar este modulo

from PyQt5.QtWidgets import QMainWindow
from view.tela_cadastro_vendedores import Ui_tela_cadastro_vendedor

class ControleCadastroVendedor(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE CADASTRO DE VENDEDORES
        self.tela_cadastro_vendedores = Ui_tela_cadastro_vendedor()
        self.tela_cadastro_vendedores.setupUi(self)
        
        self.tela_cadastro_vendedores.pushButton_cancelar.clicked.connect(self.bt_cancelar)
        
        self.limpar_campos()
        
    
    def limpar_campos(self):
        self.tela_cadastro_vendedores.lineEdit_nome_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_endereco_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_bairro_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_cidade_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_numero_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_telefone_vendedor.clear()
    
    def bt_cancelar(self):
        self.limpar_campos()
        self.close()