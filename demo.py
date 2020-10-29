import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..'))

from example.example import Example

class Demo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        import qtstylish

        example_ui = Example()

        layout = QtWidgets.QVBoxLayout()
        btn_layout = QtWidgets.QHBoxLayout()
        
        import importlib

        btn = QtWidgets.QPushButton("Unstyled")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                    importlib.reload(qtstylish),
                                    print("Done"),
                                     self.setStyleSheet("")])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Breeze Light")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                    importlib.reload(qtstylish),
                                    print("Done"),
                                     self.setStyleSheet(qtstylish.light)])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Breeze Dark")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                    importlib.reload(qtstylish),
                                    print("Done"),
                                     self.setStyleSheet(qtstylish.dark)])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QtStylish Dark")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                    importlib.reload(qtstylish),
                                    print("Done"),
                                     self.setStyleSheet(qtstylish.mydark)])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QDarkStyle")
        import qdarkstyle
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                    importlib.reload(qtstylish),
                                    print("Done"),
                                    self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())])
        btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)
        layout.addWidget(example_ui)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = Demo()
    app.exec_()
