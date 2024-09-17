import sqlite3


class ModelCliente():

    def __init__(self):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        
        self.return_query = None

    def create_table_cliente(self):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT,
            numero TEXT,
            bairro TEXT,
            cidade TEXT,
            telefone TEXT NOT NULL,
            observacoes TEXT)""")

        self.connection.commit()
        self.connection.close()
        
    
    def insert_cliente(self, nome, endereco, numero, bairro, cidade, telefone, observacoes):
        self.connection = sqlite3.connect("esquadriaDB.db")
        
        try:
            self.cursor = self.connection.cursor()

            self.cursor.execute("""
                                INSERT INTO clientes (
                                    nome,
                                    endereco,
                                    numero,
                                    bairro,
                                    cidade,
                                    telefone,
                                    observacoes) VALUES (?,?,?,?,?,?,?)""", (nome, endereco, numero, bairro, cidade, telefone, observacoes))
            
            self.connection.commit()
            print("Registro inserido com sucesso!")
        except:
            Erro = self.connection.Error
            print(Erro)
            self.connection = None
        finally:
            if self.connection != None:
                self.cursor.close()
                self.connection.close()
                print("Conexão encerrada")
    
    
    def update_cliente(self, id, nome, endereco, numero, bairro, cidade, telefone, observacoes):
        pass
    
    
    def delete_cliente(self, id):
        self.connection = sqlite3.connect("esquadriaDB.db")
        
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute("DELETE FROM clientes WHERE id=?", id)
            
            self.connection.commit()
            print("Registro excluido com sucesso!")
        except:
            Erro = self.connection.Error
            print(Erro)
            self.connection = None
        finally:
            if self.connection != None:
                self.cursor.close()
                self.connection.close()
                print("Conexão encerrada")
    
    
    def list_clientes(self):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""SELECT * FROM clientes""")
        
        self.return_query = self.cursor.fetchall()
        
        return self.return_query
    
    
    def find_cliente(self, cliente):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""SELECT * FROM clientes WHERE cliente=?""", cliente)
        