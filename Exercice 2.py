from PySide2.QtWidgets import *
from PySide2.QtGui import *
app = QApplication([])

class Chargement(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(400,200)
        self.layout = QHBoxLayout()
        self.barre = QProgressBar()
        self.slider = QSlider()
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.progressBarre)
        self.setLayout(self.layout)

    def progressBarre(self):
        self.barre.setValue(self.slider.value())



a = Chargement()
a.show()
app.exec_()
