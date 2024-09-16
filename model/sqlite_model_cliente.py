import sqlite3

"""
    Classe responsável pelas conexões com o banco que o cliente deve fazer
    e todos os metodos que envolvem o cliente estarão aqui
"""


class ModelCliente:
    """Metodo Construtor"""

    def __init__(self):
        """connetion recebe informações para conexao com sqlite"""
        self.connection = sqlite3.connect("esquadriaDB")

        """Instancia um objeto cursor"""
        self.cursor = self.connection.cursor()

        """Variavel que vai guardar o nome da tabela"""
        self.table_name = None

        """Variavel que vai guardar o SQL de insercao"""
        self.sql_insert = None
        self.sql_delete = None
        self.sql_query = None
        self.return_query = None
        self.valor_procurado = ()

        """Variavel que vai guardar os valores a serem inseridos no banco
            tem que ser uma tupla ( )"""
        self.inserted_values = ()
        self.delete_value = None

        # Verificar o que estes comandos fazem na conexão
        # self.autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        # self.connection.set_isolation_level(self.autocommit)

    def insert_cliente(self, value):
        try:
            """Instancia um objeto cursor"""
            self.cursor = self.connection.cursor()
            self.table_name = "clientes"
            self.sql_insert = "INSERT INTO " + self.table_name + "(nome, telefone, cpf, rg, rua, numero, cidade, bairro, estado, cep) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(self.sql_insert, value)

            """Realiza o commit na conexao(insere os dados no banco)"""
            self.connection.commit()
            print("Concluido", "Cadastro realizado com Sucesso!")

        except:
            print("Erro")
            self.connection = None

        finally:
            self.cursor.close()
            self.connection.close()

    def delete_cliente(self, delete_value):

        self.cursor = self.connection.cursor()
        self.delete_value = delete_value
        self.table_name = "clientes"
        self.sql_query = "Delete from " + self.table_name + " where codigo = %s "

        self.cursor.execute(self.sql_query, (self.delete_value,))
        self.connection.commit()
        # result = self.cursor.rowcount
        self.cursor.close()
        self.connection.close()

    def listar_cliente(self):
        self.cursor = self.connection.cursor()
        self.table_name = "clientes"
        self.sql_query = "Select * from " + self.table_name
        self.cursor.execute(self.sql_query)

        self.return_query = self.cursor.fetchall()

        return self.return_query
