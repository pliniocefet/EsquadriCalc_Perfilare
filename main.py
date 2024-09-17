from PyQt5.QtWidgets import QApplication, QMainWindow
#from controle.controle_menu_principal import ControleMenuPrincipal
from controle.controle_principal import ControlePrincipal
from view.tela_login import Ui_MainWindow_login
from model.model_login import ModelLogin
import sys


class Main(QMainWindow):
    """
            Classe que controla o Login do Software
            Classe com o main - primeiro a ser executado
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_login()
        self.ui.setupUi(self)
        self.model_login = ModelLogin()

        # ESCONDE O FRAME DE ERRO
        self.ui.frame_error.hide()

        # TELA PRINCIPAL
        self.tela_principal = ControlePrincipal()
        

        # AÇÃO DO BOTÃO lOGIN
        # Chama o metodo que exibe a tela principal
        self.ui.pushButton_login.clicked.connect(self.validar_usuario)

    def validar_usuario(self):
        usuario = self.ui.lineEdit_user.text()
        senha = self.ui.lineEdit_password.text()

        # TODO
        # implementar save_check
        save_check = self.ui.checkBox_save_user.checkState()

        if self.model_login.event_bt_login(usuario, senha):

            self.chama_tela_principal()
        else:
            print("usuario não encontrado")

    def chama_tela_principal(self):
        # esconde a tela de login
        self.hide()
        # chama a tela principal
        self.tela_principal.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
