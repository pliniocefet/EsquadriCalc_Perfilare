# tela_busca.py
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TelaBusca(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Busca de Clientes")
        self.setGeometry(100, 100, 400, 300)

        # Layout da tela de busca
        layout = QVBoxLayout()

        # Tabela de clientes
        self.tabela_clientes = QTableWidget(self)
        self.tabela_clientes.setColumnCount(2)
        self.tabela_clientes.setHorizontalHeaderLabels(["Nome", "Telefone"])
        layout.addWidget(self.tabela_clientes)

        # Definindo o layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
