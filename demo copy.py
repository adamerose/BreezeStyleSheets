from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        widget = QWidget()
        self.setLayout(layout)
        layout.addWidget(widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
    example = Example()
    example.show()
    app.exec_()
