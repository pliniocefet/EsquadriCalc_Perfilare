from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from view.tela_buscar_cliente import Ui_MainWindow_buscar_cliente
from model.model_cliente import ModelCliente
from view.tela_novo_orcamento import Ui_tela_novo_orcamento



class ControleBuscarCliente(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tela_buscar_cliente = Ui_MainWindow_buscar_cliente()
        self.tela_buscar_cliente.setupUi(self)
        
        #TODO: encontrar uma forma de capturar o cliente da tela_buscar_cliente para trazer para a tela_novo_orcamento
        #self.novo_orcamento = Ui_tela_novo_orcamento()
        
        
        # preecher a tabela de clientes ao abrir a tela
        self.preenche_tabela()
        
        ### AÇÕES DE BOTÕES E TABELA
        # captura informações da tabela de acordo com o item clicado
        self.tela_buscar_cliente.tableWidget_clientes.itemClicked.connect(self.captura_cliente)
        
        self.tela_buscar_cliente.pushButton_fechar.clicked.connect(self.bt_fechar)
        self.tela_buscar_cliente.pushButton_buscar_cliente.clicked.connect(self.bt_buscar)
        self.tela_buscar_cliente.pushButton_inserir_cliente.clicked.connect(self.bt_inserir)
        
    
    def bt_fechar(self):
        self.close()
        
    
    def bt_buscar(self):
        pass
    
    
    def bt_inserir(self):
        pass
    
    
    def captura_cliente(self, item):
        row = item.row()
        row_itens = []
        
        for col in range(self.tela_buscar_cliente.tableWidget_clientes.colorCount()):
            item = self.tela_buscar_cliente.tableWidget_clientes.item(row, col)
            
            if item is not None:
                row_itens.append(item.text())
                
            else:
                row_itens.append("")
                
        # self.novo_orcamento.lineEdit_nome_cliente.setText(row_itens[1])
        # self.novo_orcamento.lineEdit_endereco_cliente.setText(row_itens[2])
        # self.novo_orcamento.lineEdit_numero_cliente.setText(row_itens[3])
        # self.novo_orcamento.lineEdit_bairro_cliente.setText(row_itens[4])
        # self.novo_orcamento.lineEdit_cidade_cliente.setText(row_itens[5])
        # self.novo_orcamento.lineEdit_telefone_cliente.setText(row_itens[6])
        # self.novo_orcamento.textEdit_observacoes.toPlainText(row_itens[7])
        # self.novo_orcamento.pushButton_salvar_cliente.setEnabled(False)
        # self.novo_orcamento.pushButton_editar_cliente.setEnabled(True)
        
    
    def preenche_tabela(self):
        self.model_cliente = ModelCliente()
        clientes = self.model_cliente.list_clientes()
        
        # Para descobrir o numero de linhas
        self.tela_buscar_cliente.tableWidget_clientes.setRowCount(len(clientes))
        
        # Primeiro FOR cria as linhas da tabela 
        for row, text in enumerate(clientes):
            # Segundo for preenche a linha com o conteudo do banco de acordo com cada coluna
            # str(data) -> converte todo o conteudo do banco para string
           for column, data in enumerate(text):
               self.tela_buscar_cliente.tableWidget_clientes.setItem(row, column, QTableWidgetItem(str(data)))
            