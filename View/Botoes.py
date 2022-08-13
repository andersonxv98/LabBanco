from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout


class Botoes(QHBoxLayout):
    def __init__(self):
        super(Botoes, self).__init__()
        self.btn_pesquisar = QPushButton("Pesquisar")
        self.btn_gravar = QPushButton("Gravar")
        self.btn_excluir = QPushButton("Excluir")
        self.btn_pesquisar.setStyleSheet("background-color: lightgreen")
        self.btn_gravar.setStyleSheet("background-color: lightblue")
        self.btn_excluir.setStyleSheet("background-color: pink")



        self.lb = QLabel("Quantidade de Aluno")
        self.tb_qtdaluno = QLineEdit()

        self.addWidget(self.btn_pesquisar)
        self.addWidget(self.btn_gravar)
        self.addWidget(self.btn_excluir)

        self.Lays = QVBoxLayout()
        self.tb_qtdaluno.setMaximumWidth(150)
        self.Lays.addWidget(self.lb)
        self.Lays.addWidget(self.tb_qtdaluno)
        self.addLayout(self.Lays)
