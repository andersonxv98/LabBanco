import sys

from PyQt6.QtWidgets import QApplication
from Controller.Control import Control

app = QApplication(sys.argv)
controllador  = Control()

window = controllador.getMainView()
#window = TesteEvento()
window.show()
#window.AddLabel()

app.exec()