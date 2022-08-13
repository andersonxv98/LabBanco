from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from PyQt6.QtWidgets import QVBoxLayout, QLabel, QComboBox, QLineEdit, QHBoxLayout, QWidget


class PrimeiraParte(QVBoxLayout):
    def __init__(self):
        super(PrimeiraParte, self).__init__()
        #labels
        self.lb_numero = QLabel("Numero")
        self.lb_curso = QLabel("Curso")
        self.lb_ano = QLabel("Ano")
        self.lb_professor = QLabel("Professor")
        fonte = QFont("Times", 18)

        self.lb_numero.setFont(fonte)
        self.lb_curso.setFont(fonte)
        self.lb_ano.setFont(fonte)
        self.lb_professor.setFont(fonte)
        #Campos
        self.select = QComboBox()
        self.tb_numero = QLineEdit()
        self.tb_cod_professor = QLineEdit()
        self.tb_ano  = QLineEdit()
        self.tb_nome_professor = QLineEdit()
        #self.tb_nome_professor.setDisabled()



        self.row1 = QHBoxLayout()

        #self.LayoutEsquerda.setAlignment(Qt.AlignmentFlag.AlignTop)
        #self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.row1.addWidget(self.lb_numero)
        self.row1.addWidget(self.tb_numero)

        self.second_r1 = QHBoxLayout()
        self.second_r1.addWidget(self.lb_ano)
        self.second_r1.addWidget(self.tb_ano)

        self.second_r1.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.row1.addLayout(self.second_r1)

        self.row2 = QHBoxLayout()

        # self.LayoutEsquerda.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.row2.addWidget(self.lb_curso)
        self.row2.addWidget(self.select)

        self.row3 = QHBoxLayout()

        # self.LayoutEsquerda.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.row3.addWidget(self.lb_professor)
        self.row3.addWidget(self.tb_cod_professor)
        self.row3.addWidget(self.tb_nome_professor)


        self.addLayout(self.row1)
        self.addLayout(self.row2)
        self.addLayout(self.row3)
        #self.LayoutGeralDaWindow.addLayout(self.LayoutDoMeioCampoResolucao)
        #self.LayoutGeralDaWindow.addLayout(self.LayoutDeBaixoBotoesOperadores)

        #self.LayoutGeralDaWindow.addWidget(self.Button)

        # container = (QWidget())
        #container.setLayout(self)

        #self.setCentralWidget(container)



