from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.content1 = QtWidgets.QWidget()
        self.content1.setStyleSheet("background-color:#330000;")
        self.content1.setMinimumSize(QtCore.QSize(50, 50))
        self.content2 = QtWidgets.QWidget()
        self.content2.setStyleSheet("background-color:#770000;")
        self.content2.setMinimumSize(QtCore.QSize(50, 50))

        self.splitter = QtWidgets.QSplitter()
        self.splitter.addWidget(self.content1)
        self.splitter.addWidget(self.content2)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    example = Example()
    example.show()
    app.exec_()
