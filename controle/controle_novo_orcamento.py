from PyQt5.QtWidgets import QMainWindow
from view.tela_novo_orcamento import Ui_tela_novo_orcamento
from controle.controle_buscar_cliente import ControleBuscarCliente
from view.tela_buscar_cliente import Ui_MainWindow_buscar_cliente

class ControleNovoOrcamento(QMainWindow):

    def __init__(self):
        super().__init__()
        self.novo_orcamento = Ui_tela_novo_orcamento()
        self.novo_orcamento.setupUi(self)
        
        ### AÇÕES DOS BOTÕES ###
        self.novo_orcamento.pushButton_buscar_cliente.clicked.connect(self.buscar_cliente)
        self.novo_orcamento.pushButton_cancelar.clicked.connect(self.fechar_orcamento)
        
        
    def buscar_cliente(self):
        self.chama_buscar_cliente = ControleBuscarCliente()
        self.chama_buscar_cliente.show()
        
    
    def fechar_orcamento(self):
        self.close()
        
    