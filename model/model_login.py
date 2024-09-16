from model.conexao_usuario import ConexaoUsuario
import sqlite3

class ModelLogin():
	"""
		Classe responsável por validar o usuario e informar ao controle
	"""

	def event_bt_login (self, login, senha):
		"""
			METODO QUE VERIFICA NO BANCO DE DADOS O NOME DO USUARIO E A SENHA
			BOTÃO LOGIN
		"""
		# conexão com banco de dados
		conexao = sqlite3.connect('esquadriaDB.db')
		cursor = conexao.cursor()
		try:
			cursor.execute("SELECT * FROM usuarios where usuario = ? AND senha = ?", (login, senha))
			user = cursor.fetchone()
  
			if user:
				print("Login efetuado com sucesso!")
				return True
			else:
				print("Login ou senha incorretos!")
				return False
		except sqlite3.Error as e:
				print("Erro ao tentar efetuar login: ", e)
				return False
		finally:
			conexao.close()



   
#	def event_bt_login(self,login,senha):
#		"""
#			METODO QUE VERIFICA NO BANCO DE DADOS O NOME DO USUARIO E A SENHA
#			BOTÃO LOGIN
#		"""
#		# Conexão com banco de dados
#		self.conexao = ConexaoUsuario()
#		self.cursor = self.conexao.cursor()
#		try:
#			self.cursor.execute("SELECT * from usuarios where usuario=? and senha=?", (login, senha))
#			user = self.cursor.fetchone()
#			
# 			if user:
#				print("Login efetuado com sucesso!")
#				return True
#			else:
#				print("Login ou senha incorretos!")	
#				return False
#		except sqlite3.Error as e:
#			print("Erro ao tentar efetuar login: ", e)
#			return False
#		finally:
#			self.conexao.close()