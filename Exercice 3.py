from PySide2.QtWidgets import *
from PySide2.QtGui import *
app = QApplication([])

class ClicClic(QWidget):
    def __init__(self,i):
        QWidget.__init__(self)
        self.i = i
        self.setWindowTitle("IHM")
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()
        self.button = QPushButton("Changer mon texte !")
        self.text = QTextEdit("Le nombre de clics va être affiché ici")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        #self.button.clicked.connect(self.Close)
        #self.button.clicked.connect(self.TextChangement)
        #self.button.clicked.connect(self.TextChanged)
        self.setLayout(self.layout)
    def Close(self):
        self.close()
    def TextChangement(self):
        self.i += 1
        a = "Clic" + "" + str(self.i)
        self.button.setText(a)
        print(a)
    def TextChanged(self):
        self.i += 1
        a = "Clic" + "" + str(self.i)
        self.text.setText(a)
        self.button.setText(a)
        print(a)



a = ClicClic(0)
a.show()
app.exec_()
