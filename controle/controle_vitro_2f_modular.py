from PyQt5.QtWidgets import QMainWindow
from view.tela_vitro_2f_modular import Ui_MainWindow_vitro_2f_modular



class ControleVitro2FModular(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tela_vitro_2f_modular = Ui_MainWindow_vitro_2f_modular()
        self.tela_vitro_2f_modular.setupUi(self)
        
        # Instancia de controle de vitro 2 folhas modular
        self.tela_vitro_2f_modular = ControleVitro2FModular()
        
        ### AÇÃO DOS BOTÕES ###
        # Ao clicar no botão "Vitro Modular 2 folhas" executa o método
        self.tela_menu_principal.pushButton_vitro_modular_2f.clicked.connect(self.botao_vitro_modular_2f)
        
        
    def botao_vitro_modular_2f(self):
        self.tela_vitro_2f_modular.show()