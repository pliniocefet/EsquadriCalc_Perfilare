import sqlite3


class ConexaoUsuario:

    """Metodo Construtor"""

    def __init__(self):
        """connetion recebe informacoes para conexao com sqlite"""
        self.connection = sqlite3.connect("esquadriaDB.db")

        """Instancia um objeto cursor"""
        self.cursor = self.connection.cursor()

        """Variavel que vai guardar o SQL de insercao"""
        self.sql_insert = None
        self.sql_delete = None
        self.return_query = None
        self.delete_value = None

        # Verificar o que estes comandos fazem na conexão
        # self.autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        # self.connection.set_isolation_level(self.autocommit)

    def create_table(self):
        """ Método para criar a tabela no banco caso não esteja criado"""

        self.connection = sqlite3.connect("esquadriaDB.db")

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL)''')

        self.connection.commit()
        self.connection.close()

    def create_user(self, usuario, senha):
        self.connection = sqlite3.connect("esquadriaDB.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            '''INSERT INTO usuarios (usuario, senha) VALUES (?, ?)''', (usuario, senha))
        self.connection.commit()
        self.connection.close()

    def insert_user(self, usuario, senha):

        self.connection = sqlite3.connect("esquadriaDB.db")

        try:
            """Instancia um objeto cursor"""
            self.cursor = self.connection.cursor()

            self.cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (
                usuario, senha))
            print("Registro inserido com sucesso!")

            """Realiza o commit na conexao(insere os dados no banco)"""
            self.connection.commit()
            print("Mensagem", "Usuário cadastrado com sucesso")

        except:
            Erro = self.connection.Error
            print(Erro)
            self.connection = None

        finally:
            if self.connection != None:
                self.cursor.close()
                self.connection.close()
                print("Conexão com banco encerrada")

    def delete_user(self, usuario):

        self.connection = sqlite3.connect("esquadriaDB.db")

        try:
            self.cursor = self.connection.cursor()

            self.cursor.execute(
                "DELETE FROM usuarios where usuario = ?", (usuario,))

            self.connection.commit()
            print("Usuario apagado com sucesso!")

        except:
            Erro = self.connection.Error
            print(Erro)
            self.connection = None
        finally:
            if self.connection != None:
                self.cursor.close()
                self.connection.close()
                print("Conexão com banco encerrada")

    def buscar_user(self, usuario):

        self.connection = sqlite3.connect('esquadriaDB.db')

        self.cursor.execute(
            "SELECT usuario FROM usuarios where usuario = ?", (usuario,))

        self.return_query = self.cursor.fetchall()


        return self.return_query
