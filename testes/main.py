# main.py
import sys
from PyQt5.QtWidgets import QApplication
from controle_principal import ControlePrincipal

def main():
    app = QApplication(sys.argv)

    # Instancia o controlador principal
    controle_principal = ControlePrincipal()

    # Mostra a tela principal
    controle_principal.mostrar_tela()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
