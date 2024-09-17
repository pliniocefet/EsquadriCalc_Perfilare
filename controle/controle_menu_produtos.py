from PyQt5.QtWidgets import QMainWindow
from view.tela_menu_produtos import Ui_MainWindow_menu_produtos



class ControleMenuProdutos(QMainWindow):
    """
        Classe que controla a tela do menu de Produtos do Software
        Aqui se manipula todas as telas que estão na view
        Executando metodos da camada Model se necessário
    """

    def __init__(self):
        super().__init__()
        self.tela_menu_produtos = Ui_MainWindow_menu_produtos()
        self.tela_menu_produtos.setupUi(self)