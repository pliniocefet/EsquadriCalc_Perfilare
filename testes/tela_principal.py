# tela_principal.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Principal")

        # Layout da janela principal
        layout = QVBoxLayout()

        # Campo de nome do cliente
        self.campo_nome = QLineEdit(self)
        self.campo_nome.setPlaceholderText("Nome do Cliente")
        layout.addWidget(self.campo_nome)

        # Campo de telefone
        self.campo_telefone = QLineEdit(self)
        self.campo_telefone.setPlaceholderText("Telefone")
        layout.addWidget(self.campo_telefone)

        # Botão de buscar
        self.botao_buscar = QPushButton("Buscar", self)
        layout.addWidget(self.botao_buscar)

        # Definindo o layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
