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

        
        # VARIAVEIS UTILITÁRIAS
        self.combo_vendedores = None

        self.recebe_busca = None

        ### ESTADO DOS BOTÕES ###
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)

        self.preenche_combo_vendedores()

        ### AÇÕES DOS BOTÕES ###
        self.novo_orcamento.pushButton_buscar_cliente.clicked.connect(
            self.buscar_cliente)
        self.novo_orcamento.pushButton_cancelar.clicked.connect(
            self.cancelar_orcamento)
        self.novo_orcamento.pushButton_salvar_cliente.clicked.connect(
            self.salvar_cliente)
        self.novo_orcamento.pushButton_editar_cliente.clicked.connect(
            self.editar_cliente)

        self.novo_orcamento.pushButton_novo_cliente.clicked.connect(
            self.novo_cliente)

        # Condição de funcionamento dos botões
        if self.novo_orcamento.lineEdit_nome_cliente.text() == "":
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(False)
        else:
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)

    def preenche_combo_vendedores(self):
        self.vendedor = ModelVendedor()
        self.combo_vendedores = self.vendedor.list_vendedores()

        # Preenche o comboBox de vendedores com as informações do banco de dados
        for vendedor in self.combo_vendedores:
            self.novo_orcamento.comboBox_vendedores.addItem(vendedor[1])
            
    def preeche_combo_produtos(self):
        pass
    

    def buscar_cliente(self):
        self.controle_buscar_cliente = ControleBuscarCliente(self)
        self.controle_buscar_cliente.show()

    def cancelar_orcamento(self):
        self.novo_orcamento.lineEdit_nome_cliente.clear()
        self.novo_orcamento.lineEdit_endereco_cliente.clear()
        self.novo_orcamento.lineEdit_numero_cliente.clear()
        self.novo_orcamento.lineEdit_bairro_cliente.clear()
        self.novo_orcamento.lineEdit_cidade_cliente.clear()
        self.novo_orcamento.lineEdit_telefone_cliente.clear()
        self.novo_orcamento.textEdit_observacoes.clear()
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        
        ### Desabilita os campos ao cancelar o orçamento
        self.novo_orcamento.lineEdit_nome_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_endereco_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_numero_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_bairro_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_cidade_cliente.setEnabled(False)
        self.novo_orcamento.lineEdit_telefone_cliente.setEnabled(False)
        self.novo_orcamento.textEdit_observacoes.setEnabled(False)
        self.close()

    def salvar_cliente(self):
        nome_cliente = self.novo_orcamento.lineEdit_nome_cliente.text()
        endereco_cliente = self.novo_orcamento.lineEdit_endereco_cliente.text()
        numero_cliente = self.novo_orcamento.lineEdit_numero_cliente.text()
        bairro_cliente = self.novo_orcamento.lineEdit_bairro_cliente.text()
        cidade_cliente = self.novo_orcamento.lineEdit_cidade_cliente.text()
        telefone_cliente = self.novo_orcamento.lineEdit_telefone_cliente.text()
        observacoes_cliente = self.novo_orcamento.textEdit_observacoes.toPlainText()

        if nome_cliente and telefone_cliente:

            self.modelCliente = ModelCliente()        
            self.modelCliente.insert_cliente(nome_cliente, endereco_cliente, numero_cliente,
                                         bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente)

            self.menssagem('Cadastro Realizado com Sucesso!')
            self.novo_orcamento.pushButton_salvar_cliente.setEnabled(False)
            self.novo_orcamento.pushButton_editar_cliente.setEnabled(True)
            self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)
            self.novo_orcamento.lineEdit_nome_cliente.setEnabled(False)
            self.novo_orcamento.lineEdit_telefone_cliente.setEnabled(False)
            self.novo_orcamento.lineEdit_endereco_cliente.setEnabled(False)
            self.novo_orcamento.lineEdit_numero_cliente.setEnabled(False)
            self.novo_orcamento.lineEdit_bairro_cliente.setEnabled(False)
            self.novo_orcamento.lineEdit_cidade_cliente.setEnabled(False)
            self.novo_orcamento.textEdit_observacoes.setEnabled(False)
            self.novo_orcamento.comboBox_vendedores.setEnabled(False)
        else:
            self.menagem("Preencha pelo menos o Nome e o Telefone")

    def editar_cliente(self):
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.novo_orcamento.pushButton_editar_cliente.setEnabled(False)

    def novo_cliente(self):
        self.novo_orcamento.pushButton_salvar_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_nome_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_telefone_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_endereco_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_numero_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_bairro_cliente.setEnabled(True)
        self.novo_orcamento.lineEdit_cidade_cliente.setEnabled(True)
        self.novo_orcamento.textEdit_observacoes.setEnabled(True)
        # self.novo_orcamento.comboBox_vendedores.setEnabled(True)

    ### MESSAGEBOX ###
    def menssagem(self, menssagem):
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle('Information')
        self.msg_box.setText(menssagem)
        self.msg_box.setIcon(QMessageBox.Information)
        self.msg_box.setStandardButtons(QMessageBox.Ok)
        self.msg_box.exec_()

    def preenche_dados_cliente(self, nome_cliente, endereco_cliente, numero_cliente, bairro_cliente, cidade_cliente, telefone_cliente, observacoes_cliente):
        self.novo_orcamento.lineEdit_nome_cliente.setText(nome_cliente)
        self.novo_orcamento.lineEdit_endereco_cliente.setText(endereco_cliente)
        self.novo_orcamento.lineEdit_numero_cliente.setText(numero_cliente)
        self.novo_orcamento.lineEdit_bairro_cliente.setText(bairro_cliente)
        self.novo_orcamento.lineEdit_cidade_cliente.setText(cidade_cliente)
        self.novo_orcamento.lineEdit_telefone_cliente.setText(telefone_cliente)
        self.novo_orcamento.textEdit_observacoes.setText(observacoes_cliente)
        
        # Ativa o combobox de produtos e o botão de incluir
        self.novo_orcamento.comboBox_lista_produtos.setEnabled(True)
        self.novo_orcamento.pushButton_incluir_produto.setEnabled(True)
    
        
