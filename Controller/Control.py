from PyQt6.QtWidgets import QLabel

from DAO.viewCliente import DaoViewCliente
from Model.Clientes import Clientes
from View.MainView import MainView
from DAO.Conexao import Conexao

class Control():
    def __init__(self):
        super(Control, self).__init__()
        self.db = Conexao()
        self.MainView = MainView()
        self.MainView.Botoes.btn_gravar.clicked.connect(self.carregarClientes)
        self.MainView.Botoes.btn_pesquisar.clicked.connect(self.carregarClientes)
        print(self.db)

    def getMainView(self):
        return self.MainView



    def carregarClientes(self):
        co = DaoViewCliente(self.db)
        a = co.getClientes()
        for cliente in a:
           cl =  Clientes(cliente[0], cliente[1],cliente[2], cliente[3])

           objeto_tratados_pro_front = [
               QLabel(cl.getNome()),
               QLabel(cl.getCidade()),
               QLabel(cl.getEstado())
           ]
           contador = 0
           self.MainView.SegundaParte.setRowCount(self.MainView.SegundaParte.n_row + 1)
           for item in objeto_tratados_pro_front:
               item.setStyleSheet("background-color: #adffed")
               self.MainView.SegundaParte.setCellWidget(self.MainView.SegundaParte.n_row, contador, item)
               contador +=1
           self.MainView.SegundaParte.n_row +=1
