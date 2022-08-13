from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from PyQt6.QtWidgets import QLabel, QTableWidget, QHeaderView, QAbstractItemView


class Tabela(QTableWidget):
    def __init__(self):
        super(Tabela, self).__init__()

        self.setMinimumWidth(400)
        self.n_row = 0
        self.setColumnCount(3)
        #self.setRowCount(self.n_row + 1)
        self.setHorizontalHeaderLabels(('CODIGO', 'NOME', 'NOTA'))
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)



