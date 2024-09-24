from PyQt5.QtWidgets import QMainWindow, QMessageBox
from view.tela_novo_orcamento import Ui_tela_novo_orcamento
from controle.controle_buscar_cliente import ControleBuscarCliente
from model.model_cliente import ModelCliente


class ControleNovoOrcamento(QMainWindow):  
    """ 
        Classe que controla a tela de novo orçamento
    """

    def __init__(self):
        super().__init__()
        self.novo_orcamento = Ui_tela_novo_orcamento()
        self.novo_orcamento.setupUi(self)
        
        ### ESTADO DOS BOTÕES ###
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)
        
        ### PREENCHE O COMBOBOX DE VENDEDORES ###
        self.preenche_combo_vendedores()

        ### AÇÕES DOS BOTÕES ###
        self.novo_orcamento.pushButton_buscar_cliente.clicked.connect(
            self.buscar_cliente)
        self.novo_orcamento.pushButton_cancelar.clicked.connect(
            self.cancelar_orcamento)
        self.novo_orcamento.pushButton_salvar_cliente.clicked.connect(
            self.salvar_cliente)
        self.novo_orcamento.pushButton_editar_cliente.clicked.connect(self.editar_cliente)

    
    def preenche_combo_vendedores(self):
        pass
    

    def buscar_cliente(self):
        self.chama_buscar_cliente = ControleBuscarCliente()
        self.chama_buscar_cliente.show()

    def cancelar_orcamento(self):
        self.novo_orcamento.lineEdit_nome_cliente.clear()
        self.novo_orcamento.lineEdit_endereco_cliente.clear()
        self.novo_orcamento.lineEdit_numero_cliente.clear()
        self.novo_orcamento.lineEdit_bairro_cliente.clear()
        self.novo_orcamento.lineEdit_cidade_cliente.clear()
        self.novo_orcamento.lineEdit_telefone_cliente.clear()
        self.novo_orcamento.textEdit_observacoes.clear()
        self.close()

    def salvar_cliente(self):
        self.modelCliente = ModelCliente()
        nome_cliente = self.novo_orcamento.lineEdit_nome_cliente.text()
        endereco_cliente = self.novo_orcamento.lineEdit_endereco_cliente.text()
        numero_cliente = self.novo_orcamento.lineEdit_numero_cliente.text()
        bairro_cliente = self.novo_orcamento.lineEdit_bairro_cliente.text()
        cidade_cliente = self.novo_orcamento.lineEdit_cidade_cliente.text()
        telefone_cliente = self.novo_orcamento.lineEdit_telefone_cliente.text()
        observacoes_cliente = self.novo_orcamento.textEdit_observacoes.toPlainText()

        self.modelCliente.insert_cliente(nome_cliente, endereco_cliente, numero_cliente,
                                         bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente)
        
        self.menssagem()
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(False)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(True)
        
        
    def editar_cliente(self):
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)
        
    ### MESSAGEBOX ###
    def menssagem(self):    
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle('Information')
        self.msg_box.setText('Cadastro Realizado com Sucesso')
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.exec_()
        
