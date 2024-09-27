from PyQt5.QtWidgets import QMainWindow, QMessageBox
from view.tela_novo_orcamento import Ui_tela_novo_orcamento
from controle.controle_buscar_cliente import ControleBuscarCliente
from model.model_cliente import ModelCliente
from model.model_vendedor import ModelVendedor


class ControleNovoOrcamento(QMainWindow):  
    """ 
        Classe que controla a tela de novo orçamento
    """

    def __init__(self):
        super().__init__()
        self.novo_orcamento = Ui_tela_novo_orcamento()
        self.novo_orcamento.setupUi(self)
        
        ### VARIAVEIS UTILITÁRIAS
        self.combo_vendedores = None
        
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
        
        ### Condição de funcionamento dos botões
        if self.novo_orcamento.lineEdit_nome_cliente.text() == "":
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(False)
        else:
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)
            
            
    def preenche_combo_vendedores(self):
        self.vendedor = ModelVendedor()
        self.combo_vendedores = self.vendedor.list_vendedores()
        
        ### Preenche o comboBox de vendedores com as informações do banco de dados
        for vendedor in self.combo_vendedores:
            self.novo_orcamento.comboBox_vendedores.addItem(vendedor[1])

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
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.close()

    def salvar_cliente(self):
        nome_cliente = self.novo_orcamento.lineEdit_nome_cliente.text()
        endereco_cliente = self.novo_orcamento.lineEdit_endereco_cliente.text()
        numero_cliente = self.novo_orcamento.lineEdit_numero_cliente.text()
        bairro_cliente = self.novo_orcamento.lineEdit_bairro_cliente.text()
        cidade_cliente = self.novo_orcamento.lineEdit_cidade_cliente.text()
        telefone_cliente = self.novo_orcamento.lineEdit_telefone_cliente.text()
        observacoes_cliente = self.novo_orcamento.textEdit_observacoes.toPlainText()
        
#       TODO FAZER UMA VERIFICAÇÃO PARA NÃO SALVAR CLIENTES EM BRANCO


        self.modelCliente = ModelCliente()
        self.modelCliente.insert_cliente(nome_cliente, endereco_cliente, numero_cliente,
                                         bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente)
        
        self.menssagem('Cadastro Realizado com Sucesso!')
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(False)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(True)
        self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)
        
    def editar_cliente(self):
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)
        
    ### MESSAGEBOX ###
    def menssagem(self, menssagem):    
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle('Information')
        self.msg_box.setText(menssagem)
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.exec_()
        
