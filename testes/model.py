# model.py
import sqlite3

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def buscar_clientes(self):
        self.cursor.execute("SELECT nome, telefone FROM clientes")
        return self.cursor.fetchall()
    
    def fechar_conexao(self):
        self.conn.close()
