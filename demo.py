import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import os
import qtstylish

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..'))

from example.example import Example


class ThemeSwitcher(QtWidgets.QWidget):
    def __init__(self, widget_to_style):
        super().__init__()

        import importlib

        layout = QtWidgets.QVBoxLayout()
        btn_layout = QtWidgets.QHBoxLayout()

        btn = QtWidgets.QPushButton("Unstyled")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     widget_to_style.setStyleSheet("")])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Breeze Light")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     widget_to_style.setStyleSheet(qtstylish.light())])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Breeze Dark")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     widget_to_style.setStyleSheet(qtstylish.dark())])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QtStylish Dark")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     widget_to_style.setStyleSheet(qtstylish.mydark())])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QDarkStyle")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     widget_to_style.setStyleSheet(qtstylish.qdarkstyle())])
        btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)
        layout.addWidget(widget_to_style)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    example = Example()
    switcher = ThemeSwitcher(example)

    switcher.resize(1000, 1000)
    app.exec_()
