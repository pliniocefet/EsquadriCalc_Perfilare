from PyQt5.QtWidgets import QMainWindow
from view.tela_buscar_cliente import Ui_MainWindow_buscar_cliente



class ControleBuscarCliente(QMainWindow):

    def __init__(self):
        super().__init__()
        self.screen_buscar_cliente = Ui_MainWindow_buscar_cliente()
        self.screen_buscar_cliente.setupUi(self)
        
        self.screen_buscar_cliente.pushButton_fechar.clicked.connect(self.fechar_buscar_cliente)
        
    
    def fechar_buscar_cliente(self):
        self.close()
        