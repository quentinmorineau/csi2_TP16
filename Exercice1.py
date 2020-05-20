from PySide2.QtWidgets import *
from PySide2.QtGui import *
import random
app = QApplication([])

class CyclesIsen(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncrea Ouest")
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()
        self.text = text
        self.label = QLabel(text)
        self.button = QPushButton("Changer le cycle")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.ButtonClicked)
        self.setLayout(self.layout)

    def ButtonClicked(self):
        liste = ["CSI","CIR","BIOST","CENT","BIAST","EST"]
        self.cycle = random.choice(liste)
        self.label.setText(self.cycle)


a = CyclesIsen("CSI")
a.show()
app.exec_()
