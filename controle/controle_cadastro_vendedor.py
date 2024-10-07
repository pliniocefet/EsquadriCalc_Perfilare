

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from view.tela_cadastro_vendedores import Ui_tela_cadastro_vendedor
from model.model_vendedor import ModelVendedor

class ControleCadastroVendedor(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE CADASTRO DE VENDEDORES
        self.tela_cadastro_vendedores = Ui_tela_cadastro_vendedor()
        self.tela_cadastro_vendedores.setupUi(self)
        
        self.tela_cadastro_vendedores.pushButton_cancelar.clicked.connect(self.bt_cancelar)
        self.tela_cadastro_vendedores.pushButton_salvar.clicked.connect(self.bt_salvar)
        self.tela_cadastro_vendedores.pushButton_novo.clicked.connect(self.bt_novo)
        
        self.limpar_campos()
        
    
    def bt_novo(self):
        self.tela_cadastro_vendedores.lineEdit_nome_vendedor.setEnabled(True)
        self.tela_cadastro_vendedores.lineEdit_endereco_vendedor.setEnabled(True)
        self.tela_cadastro_vendedores.lineEdit_bairro_vendedor.setEnabled(True)
        self.tela_cadastro_vendedores.lineEdit_cidade_vendedor.setEnabled(True)
        self.tela_cadastro_vendedores.lineEdit_numero_vendedor.setEnabled(True)
        self.tela_cadastro_vendedores.lineEdit_telefone_vendedor.setEnabled(True)
        self.tela_cadastro_vendedores.textEdit_observacoes.setEnabled(True)
        self.tela_cadastro_vendedores.pushButton_salvar.setEnabled(True)
    
    
    def limpar_campos(self):
        self.tela_cadastro_vendedores.lineEdit_nome_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_endereco_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_bairro_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_cidade_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_numero_vendedor.clear()
        self.tela_cadastro_vendedores.lineEdit_telefone_vendedor.clear()
        self.tela_cadastro_vendedores.textEdit_observacoes.clear()
    
    def bt_cancelar(self):
        self.limpar_campos()
        self.tela_cadastro_vendedores.lineEdit_nome_vendedor.setEnabled(False)
        self.tela_cadastro_vendedores.lineEdit_endereco_vendedor.setEnabled(False)
        self.tela_cadastro_vendedores.lineEdit_bairro_vendedor.setEnabled(False)
        self.tela_cadastro_vendedores.lineEdit_cidade_vendedor.setEnabled(False)
        self.tela_cadastro_vendedores.lineEdit_numero_vendedor.setEnabled(False)
        self.tela_cadastro_vendedores.lineEdit_telefone_vendedor.setEnabled(False)
        self.tela_cadastro_vendedores.textEdit_observacoes.setEnabled(False)
        self.close()
        
    def bt_salvar(self):
        nome = self.tela_cadastro_vendedores.lineEdit_nome_vendedor.text()
        telefone = self.tela_cadastro_vendedores.lineEdit_telefone_vendedor.text()
        endereco = self.tela_cadastro_vendedores.lineEdit_endereco_vendedor.text()
        numero = self.tela_cadastro_vendedores.lineEdit_numero_vendedor.text()
        bairro = self.tela_cadastro_vendedores.lineEdit_bairro_vendedor.text()
        cidade = self.tela_cadastro_vendedores.lineEdit_cidade_vendedor.text()
        observacoes = self.tela_cadastro_vendedores.textEdit_observacoes.toPlainText()
        #data_cadastro = self.tela_cadastro_vendedores.lineEdit_data.text()
        
        
        # TODO Verificar como salvar a data do cadastro de vendedores pegando a data atual do computador
        
        self.model_vendedor = ModelVendedor()
        if nome and telefone:
            self.model_vendedor.insert_vendedor(nome, telefone, endereco, numero, bairro, cidade, observacoes)
            
            self.tela_cadastro_vendedores.pushButton_salvar.setEnabled(False)
            self.tela_cadastro_vendedores.pushButton_novo.setEnabled(True)
            self.tela_cadastro_vendedores.lineEdit_nome_vendedor.setEnabled(False)
            self.tela_cadastro_vendedores.lineEdit_telefone_vendedor.setEnabled(False)
            self.tela_cadastro_vendedores.lineEdit_endereco_vendedor.setEnabled(False)
            self.tela_cadastro_vendedores.lineEdit_numero_vendedor.setEnabled(False)
            self.tela_cadastro_vendedores.lineEdit_cidade_vendedor.setEnabled(False)
            self.tela_cadastro_vendedores.lineEdit_bairro_vendedor.setEnabled(False)
            self.tela_cadastro_vendedores.textEdit_observacoes.setEnabled(False)
            
            self.limpar_campos()
            self.menssagem("Cadastro Realizado com Sucesso!")
        else:
            self.menssagem("Preencha ao menos o nome e o telefone!")
        
    def menssagem(self, menssagem):    
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle('Information')
        self.msg_box.setText(menssagem)
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.exec_()