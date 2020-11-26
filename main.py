import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.ff)

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.flag = False
        for i in range(10):
            self.qp.setBrush(QColor(255, 255, 0))
            self.coords = [random.randint(10, 500), random.randint(10, 500)]
            v = random.randint(10, 500)
            self.qp.drawEllipse(*self.coords, v, v)


    def ff(self, event):
        self.paint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
