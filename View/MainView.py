from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel

from View.Botoes import Botoes
from View.PrimeiraParte import PrimeiraParte
from View.Tabela import Tabela


class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.PrimeiraParte = PrimeiraParte()
        self.SegundaParte = Tabela()
        self.Botoes = Botoes()

        self.setWindowTitle("Lab. Banco Dados")
        self.labelTitulo = QLabel("Funcao Fundamental Gerenciar Turma")
        fonte = QFont("Times", 20)
        self.labelTitulo.setFont(fonte)

        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.LayoutGeralDaWindow = QVBoxLayout()
        self.LayoutDeCimeEnunciado = QHBoxLayout()

        self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignTop)
        #self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.LayoutDeCimeEnunciado.addWidget(self.labelTitulo)

        self.PrimeiraParte.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.LayoutGeralDaWindow.addLayout(self.LayoutDeCimeEnunciado)
        self.LayoutGeralDaWindow.addLayout(self.PrimeiraParte)
        self.LayoutGeralDaWindow.addWidget(self.SegundaParte)
        self.LayoutGeralDaWindow.addLayout(self.Botoes)
        #self.LayoutGeralDaWindow.addLayout(self.LayoutDoMeioCampoResolucao)
        #self.LayoutGeralDaWindow.addLayout(self.LayoutDeBaixoBotoesOperadores)

        #self.LayoutGeralDaWindow.addWidget(self.Button)

        container = (QWidget())
        container.setLayout(self.LayoutGeralDaWindow)
        self.setCentralWidget(container)



