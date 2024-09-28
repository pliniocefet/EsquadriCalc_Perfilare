from PyQt5.QtWidgets import QMainWindow, QMessageBox
from view.tela_cadastro_cliente import Ui_tela_cadastro_cliente

from model.model_cliente import ModelCliente


class ControleCadastroCliente(QMainWindow):

    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE CADASTRO DE CLIENTES
        self.tela_cadastro_cliente = Ui_tela_cadastro_cliente()
        self.tela_cadastro_cliente.setupUi(self)

        self.tela_cadastro_cliente.pushButton_cancelar.clicked.connect(
            self.bt_cancelar)
        self.tela_cadastro_cliente.pushButton_novo.clicked.connect(
            self.bt_novo)
        self.tela_cadastro_cliente.pushButton_salvar.clicked.connect(
            self.bt_salvar)
        self.tela_cadastro_cliente.pushButton_editar.clicked.connect(
            self.bt_editar)

    
    def bt_novo(self):
        self.tela_cadastro_cliente.lineEdit_nome_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_telefone_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_endereco_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_numero_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_bairro_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_cidade_cliente.setEnabled(True)
        self.tela_cadastro_cliente.textEdit_observacoes.setEnabled(True)
        self.tela_cadastro_cliente.comboBox_vendedores.setEnabled(True)
        self.tela_cadastro_cliente.pushButton_salvar.setEnabled(True)
        self.tela_cadastro_cliente.pushButton_novo.setEnabled(False)
        self.limpar_campos()

    
    def bt_salvar(self):
        nome_cliente = self.tela_cadastro_cliente.lineEdit_nome_cliente.text()
        telefone_cliente = self.tela_cadastro_cliente.lineEdit_telefone_cliente.text()
        endereco_cliente = self.tela_cadastro_cliente.lineEdit_endereco_cliente.text()
        numero_cliente = self.tela_cadastro_cliente.lineEdit_numero_cliente.text()
        bairro_cliente = self.tela_cadastro_cliente.lineEdit_bairro_cliente.text()
        cidade_cliente = self.tela_cadastro_cliente.lineEdit_cidade_cliente.text()
        observacoes_cliente = self.tela_cadastro_cliente.textEdit_observacoes.toPlainText()
        
        self.modelCliente = ModelCliente()
        self.modelCliente.insert_cliente(nome_cliente, endereco_cliente, numero_cliente,
                                         bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente)
        self.menssagem("Registro Salvo com Sucesso")

        self.tela_cadastro_cliente.pushButton_salvar.setEnabled(False)
        self.tela_cadastro_cliente.pushButton_editar.setEnabled(True)
        self.tela_cadastro_cliente.pushButton_novo.setEnabled(True)

        self.tela_cadastro_cliente.lineEdit_nome_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_telefone_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_endereco_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_numero_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_bairro_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_cidade_cliente.setEnabled(False)
        self.tela_cadastro_cliente.textEdit_observacoes.setEnabled(False)
        self.tela_cadastro_cliente.comboBox_vendedores.setEnabled(False)

    
    def bt_cancelar(self):
        self.limpar_campos()
        self.tela_cadastro_cliente.lineEdit_nome_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_telefone_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_endereco_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_numero_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_bairro_cliente.setEnabled(False)
        self.tela_cadastro_cliente.lineEdit_cidade_cliente.setEnabled(False)
        self.tela_cadastro_cliente.textEdit_observacoes.setEnabled(False)
        self.tela_cadastro_cliente.comboBox_vendedores.setEnabled(False)
        
        self.tela_cadastro_cliente.pushButton_salvar.setEnabled(False)
        self.tela_cadastro_cliente.pushButton_editar.setEnabled(False)
        self.tela_cadastro_cliente.pushButton_novo.setEnabled(True)
        self.close()
        
        
    def bt_editar(self):
        self.tela_cadastro_cliente.lineEdit_nome_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_telefone_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_endereco_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_numero_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_bairro_cliente.setEnabled(True)
        self.tela_cadastro_cliente.lineEdit_cidade_cliente.setEnabled(True)
        self.tela_cadastro_cliente.textEdit_observacoes.setEnabled(True)
        self.tela_cadastro_cliente.comboBox_vendedores.setEnabled(True)
        
        self.tela_cadastro_cliente.pushButton_salvar.setEnabled(True)
        self.tela_cadastro_cliente.pushButton_editar.setEnabled(False)
        self.tela_cadastro_cliente.pushButton_novo.setEnabled(False)

    
    def limpar_campos(self):
        self.tela_cadastro_cliente.lineEdit_nome_cliente.clear()
        self.tela_cadastro_cliente.lineEdit_telefone_cliente.clear()
        self.tela_cadastro_cliente.lineEdit_endereco_cliente.clear()
        self.tela_cadastro_cliente.lineEdit_numero_cliente.clear()
        self.tela_cadastro_cliente.lineEdit_bairro_cliente.clear()
        self.tela_cadastro_cliente.lineEdit_cidade_cliente.clear()
        self.tela_cadastro_cliente.textEdit_observacoes.clear()
        self.tela_cadastro_cliente.comboBox_vendedores.clear()
        
    
    def menssagem(self, menssagem):    
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle('Information')
        self.msg_box.setText(menssagem)
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.exec_()
        
