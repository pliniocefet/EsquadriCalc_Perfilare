from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from view.tela_buscar_cliente import Ui_MainWindow_buscar_cliente
from model.model_cliente import ModelCliente



class ControleBuscarCliente(QMainWindow):

    def __init__(self):
        super().__init__()
        self.tela_buscar_cliente = Ui_MainWindow_buscar_cliente()
        self.tela_buscar_cliente.setupUi(self)
        
        # preecher a tabela de clientes ao abrir a tela
        self.preenche_tabela()
        
        self.tela_buscar_cliente.pushButton_fechar.clicked.connect(self.bt_fechar)
        self.tela_buscar_cliente.pushButton_buscar_cliente.clicked.connect(self.bt_buscar)
        self.tela_buscar_cliente.pushButton_inserir_cliente.clicked.connect(self.bt_inserir)
    
    def bt_fechar(self):
        self.close()
        
    
    def bt_buscar(self):
        pass
    
    
    def bt_inserir(self):
        pass
    
    
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
            