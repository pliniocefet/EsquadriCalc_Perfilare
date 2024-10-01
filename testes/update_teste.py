import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QDialog, QLabel

# Conexão com o banco de dados
def create_connection():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    conn.commit()
    return conn

# Janela do formulário de clientes
class ClientForm(QDialog):
    def __init__(self, main_window, client_data=None):
        super().__init__()
        self.main_window = main_window
        self.client_data = client_data
        
        self.setWindowTitle("Cliente")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        # Campos de nome e email
        self.name_label = QLabel("Nome:")
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit(self)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        
        # Se houver dados de cliente, preencher o formulário
        if client_data:
            self.name_input.setText(client_data[1])
            self.email_input.setText(client_data[2])
        
        # Botões de salvar e cancelar
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Salvar", self)
        self.save_button.clicked.connect(self.save_client)
        button_layout.addWidget(self.save_button)
        
        self.cancel_button = QPushButton("Cancelar", self)
        self.cancel_button.clicked.connect(self.close)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def save_client(self):
        nome = self.name_input.text()
        email = self.email_input.text()
        
        if nome and email:
            conn = create_connection()
            cursor = conn.cursor()
            
            if self.client_data:
                # Atualizando cliente
                cursor.execute('''
                    UPDATE clientes
                    SET nome = ?, email = ?
                    WHERE id = ?
                ''', (nome, email, self.client_data[0]))
            else:
                # Inserindo novo cliente
                cursor.execute('''
                    INSERT INTO clientes (nome, email) VALUES (?, ?)
                ''', (nome, email))
            
            conn.commit()
            self.main_window.load_data()  # Recarrega os dados na tabela
            self.close()

# Janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("CRUD de Clientes")
        self.setGeometry(100, 100, 600, 400)
        
        # Layout principal
        main_layout = QVBoxLayout()
        
        # Botões de adicionar, editar e excluir
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Adicionar Cliente", self)
        self.add_button.clicked.connect(self.open_add_form)
        button_layout.addWidget(self.add_button)
        
        self.edit_button = QPushButton("Editar Cliente", self)
        self.edit_button.clicked.connect(self.open_edit_form)
        button_layout.addWidget(self.edit_button)
        
        self.delete_button = QPushButton("Excluir Cliente", self)
        self.delete_button.clicked.connect(self.delete_client)
        button_layout.addWidget(self.delete_button)
        
        main_layout.addLayout(button_layout)
        
        # Tabela para exibir os clientes
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nome", "Email"])
        main_layout.addWidget(self.table_widget)
        
        # Widget central
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
        # Carregar dados da tabela
        self.load_data()
    
    def load_data(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        rows = cursor.fetchall()
        
        self.table_widget.setRowCount(0)  # Limpar tabela
        for row_data in rows:
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def open_add_form(self):
        self.client_form = ClientForm(self)
        self.client_form.exec_()
    
    def open_edit_form(self):
        selected_row = self.table_widget.currentRow()
        if selected_row != -1:
            client_id = int(self.table_widget.item(selected_row, 0).text())
            client_name = self.table_widget.item(selected_row, 1).text()
            client_email = self.table_widget.item(selected_row, 2).text()
            client_data = (client_id, client_name, client_email)
            self.client_form = ClientForm(self, client_data)
            self.client_form.exec_()
    
    def delete_client(self):
        selected_row = self.table_widget.currentRow()
        if selected_row != -1:
            client_id = int(self.table_widget.item(selected_row, 0).text())
            
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM clientes WHERE id = ?', (client_id,))
            conn.commit()
            
            self.load_data()

# Função principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())