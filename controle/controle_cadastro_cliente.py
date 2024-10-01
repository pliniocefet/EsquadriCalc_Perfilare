from PyQt5.QtWidgets import QMainWindow, QMessageBox
from view.tela_cadastro_cliente import Ui_tela_cadastro_cliente
from model.model_vendedor import ModelVendedor
from model.model_cliente import ModelCliente


class ControleCadastroCliente(QMainWindow):

    def __init__(self):
        super().__init__()
        # CHAMA A TELA DE CADASTRO DE CLIENTES
        self.tela_cadastro_cliente = Ui_tela_cadastro_cliente()
        self.tela_cadastro_cliente.setupUi(self)

        ### AÇÕES DOS BOTÕES
        self.tela_cadastro_cliente.pushButton_cancelar.clicked.connect(
            self.bt_cancelar)
        self.tela_cadastro_cliente.pushButton_novo.clicked.connect(
            self.bt_novo)
        self.tela_cadastro_cliente.pushButton_salvar.clicked.connect(
            self.bt_salvar)
        self.tela_cadastro_cliente.pushButton_editar.clicked.connect(
            self.bt_editar)

        ### CARREGA OS CLIENTES NOS CAMPOS PARA EDIÇÃO
        self.carregar_clientes()
    
    
    def carregar_clientes(self):
        self.model_cliente = ModelCliente()
        cliente = self.model_cliente.list_clientes()
        
        self.tela_cadastro_cliente.lineEdit_nome_cliente.setText(str(cliente[0][1]))
        self.tela_cadastro_cliente.lineEdit_endereco_cliente.setText(str(cliente[0][2]))
        self.tela_cadastro_cliente.lineEdit_numero_cliente.setText(str(cliente[0][3]))
        self.tela_cadastro_cliente.lineEdit_bairro_cliente.setText(str(cliente[0][4]))
        self.tela_cadastro_cliente.lineEdit_cidade_cliente.setText(str(cliente[0][5]))
        self.tela_cadastro_cliente.lineEdit_telefone_cliente.setText(str(cliente[0][6]))
        self.tela_cadastro_cliente.textEdit_observacoes.setText(str(cliente[0][7]))
        
        
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
        self.preenche_combo_vendedores()

    
    def bt_salvar(self):
        nome_cliente = self.tela_cadastro_cliente.lineEdit_nome_cliente.text()
        telefone_cliente = self.tela_cadastro_cliente.lineEdit_telefone_cliente.text()
        endereco_cliente = self.tela_cadastro_cliente.lineEdit_endereco_cliente.text()
        numero_cliente = self.tela_cadastro_cliente.lineEdit_numero_cliente.text()
        bairro_cliente = self.tela_cadastro_cliente.lineEdit_bairro_cliente.text()
        cidade_cliente = self.tela_cadastro_cliente.lineEdit_cidade_cliente.text()
        observacoes_cliente = self.tela_cadastro_cliente.textEdit_observacoes.toPlainText()
        
        if nome_cliente and telefone_cliente:
            self.modelCliente = ModelCliente()
            self.modelCliente.insert_cliente(nome_cliente, endereco_cliente, numero_cliente,
                                         bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente)
            
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
            self.menssagem("Registro Salvo com Sucesso")
        else:
            self.menssagem("Insira ao menos o Nome e o Telefone do Cliente!")            
        
        
    
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
        
    
    def preenche_combo_vendedores(self):
        self.vendedor = ModelVendedor()
        self.combo_vendedores = self.vendedor.list_vendedores()
        
        ### Preenche o comboBox de vendedores com as informações do banco de dados
        for vendedor in self.combo_vendedores:
            self.tela_cadastro_cliente.comboBox_vendedores.addItem(vendedor[1])
        
