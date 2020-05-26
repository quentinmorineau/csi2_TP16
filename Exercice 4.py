from PySide2.QtWidgets import *
from PySide2.QtGui import *
app = QApplication([])

class Calculatrice(QWidget):
    def __init__(self,i):
        QWidget.__init__(self)
        self.setWindowTitle("Calculatrice")
        self.setMinimumSize(300,300)
        self.i = i
        self.grid = QGridLayout()
        self.text = QTextEdit(self.i)
        self.bC = QPushButton("C")
        self.bCE = QPushButton("CE")
        self.b7 = QPushButton("7")
        self.b8 = QPushButton("8")
        self.b9 = QPushButton("9")
        self.div = QPushButton("/")
        self.b4 = QPushButton("4")
        self.b5 = QPushButton("5")
        self.b6 = QPushButton("6")
        self.mul = QPushButton("*")
        self.b1 = QPushButton("1")
        self.b2 = QPushButton("2")
        self.b3 = QPushButton("3")
        self.moi = QPushButton("-")
        self.b0 = QPushButton("0")
        self.vir = QPushButton(",")
        self.ega = QPushButton("=")
        self.plu = QPushButton("+")

    # utilisation de grid :
    #(self.XXX, ligne, colone, hauteur, largeur)

        self.grid.addWidget(self.text,0,1,1,4)
        self.grid.addWidget(self.bC,1,1,1,2)
        self.grid.addWidget(self.bCE,1,3,1,2)
        self.grid.addWidget(self.b7,2,1,1,1)
        self.grid.addWidget(self.b8,2,2,1,1)
        self.grid.addWidget(self.b9,2,3,1,1)
        self.grid.addWidget(self.div,2,4,1,1)
        self.grid.addWidget(self.b4,3,1,1,1)
        self.grid.addWidget(self.b5,3,2,1,1)
        self.grid.addWidget(self.b6,3,3,1,1)
        self.grid.addWidget(self.mul,3,4,1,1)
        self.grid.addWidget(self.b1,4,1,1,1)
        self.grid.addWidget(self.b2,4,2,1,1)
        self.grid.addWidget(self.b3,4,3,1,1)
        self.grid.addWidget(self.moi,4,4,1,1)
        self.grid.addWidget(self.b0,5,1,1,1)
        self.grid.addWidget(self.vir,5,2,1,1)
        self.grid.addWidget(self.ega,5,3,1,1)
        self.grid.addWidget(self.plu,5,4,1,1)

        self.b1.clicked.connect(self.button1)
        self.b2.clicked.connect(self.button2)
        self.b3.clicked.connect(self.button3)
        self.b4.clicked.connect(self.button4)
        self.b5.clicked.connect(self.button5)
        self.b6.clicked.connect(self.button6)
        self.b7.clicked.connect(self.button7)
        self.b8.clicked.connect(self.button8)
        self.b9.clicked.connect(self.button9)
        self.b0.clicked.connect(self.button0)
        self.vir.clicked.connect(self.bvirgule)
        self.div.clicked.connect(self.bdiv)
        self.mul.clicked.connect(self.bmul)
        self.moi.clicked.connect(self.bmoins)
        self.ega.clicked.connect(self.begal)
        self.plu.clicked.connect(self.bplus)
        #self.bCE.clicked.connect(self.buttonCE)
        #self.bC.clicked.connect(self.buttonC)

        self.setLayout(self.grid)

    def button7(self):
        self.i = self.i + self.b7.text()
        self.text.setText(self.i)

    def button6(self):
        self.i = self.i + self.b6.text()
        self.text.setText(self.i)

    def button5(self):
        self.i = self.i + self.b5.text()
        self.text.setText(self.i)

    def button4(self):
        self.i = self.i + self.b4.text()
        self.text.setText(self.i)

    def button3(self):
        self.i = self.i + self.b3.text()
        self.text.setText(self.i)

    def button2(self):
        self.i = self.i + self.b2.text()
        self.text.setText(self.i)

    def button1(self):
        self.i = self.i + self.b1.text()
        self.text.setText(self.i)

    def button9(self):
        self.i = self.i + self.b9.text()
        self.text.setText(self.i)

    def button8(self):
        self.i = self.i + self.b8.text()
        self.text.setText(self.i)

    def button0(self):
        self.i = self.i + self.b0.text()
        self.text.setText(self.i)

    def bvirgule(self):
        self.i = self.i + self.vir.text()
        self.text.setText(self.i)

    def begal(self):
        self.i = self.i + self.ega.text()
        self.text.setText(self.i)

    def bplus(self):
        self.i = self.i + self.plu.text()
        self.text.setText(self.i)

    def bmoins(self):
        self.i = self.i + self.moi.text()
        self.text.setText(self.i)

    def bmul(self):
        self.i = self.i + self.mul.text()
        self.text.setText(self.i)

    def bdiv(self):
        self.i = self.i + self.div.text()
        self.text.setText(self.i)

    #def buttonC(self):
        #self.i = self.text.setText("0")

    #def buttonCE(self):




a = Calculatrice("0")
a.show()
app.exec_()
