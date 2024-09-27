import sqlite3


class ModelVendedor():

    def __init__(self):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        
        self.return_query = None

    def create_table_vendedor(self):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS vendedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT,
            numero TEXT,
            bairro TEXT,
            cidade TEXT,
            observacoes TEXT,
            data_cadastro TEXT)""")

        self.connection.commit()
        self.connection.close()
        
    
    def insert_vendedor(self, nome, telefone, endereco, numero, bairro, cidade, observacoes):
        self.connection = sqlite3.connect("esquadriaDB.db")
        
        try:
            self.cursor = self.connection.cursor()

            self.cursor.execute("""
                                INSERT INTO vendedores (
                                    nome,
                                    telefone,
                                    endereco,
                                    numero,
                                    bairro,
                                    cidade,
                                    observacoes) VALUES (?,?,?,?,?,?,?)""", (nome, telefone, endereco, numero, bairro, cidade, observacoes))
            
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
    
    
    def update_vendedor(self, id, nome, telefone):
        pass
    
    
    def delete_vendedor(self, id):
        self.connection = sqlite3.connect("esquadriaDB.db")
        
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute("DELETE FROM vendedores WHERE id=?", id)
            
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
    
    
    def list_vendedores(self):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""SELECT * FROM vendedores""")
        
        self.return_query = self.cursor.fetchall()
        
        return self.return_query
    
    
    def find_vendedor(self, nome_vendedor):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("""SELECT * FROM vendedores WHERE nome=?""", nome_vendedor)
        
        self.return_query = self.cursor.fetchone()
        
        return self.return_query
        