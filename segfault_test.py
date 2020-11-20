from example.example import Example
import sys
from PyQt5 import QtWidgets
import os
import qtstylish

sys.path.insert(0, os.path.abspath(
    os.path.dirname(os.path.abspath(__file__)) + '/..'))


class ThemeSwitcher(QtWidgets.QWidget):
    def __init__(self, widget_to_style):
        super().__init__()

        import importlib

        layout = QtWidgets.QVBoxLayout()
        btn_layout = QtWidgets.QHBoxLayout()

        btn = QtWidgets.QPushButton("Unstyled")
        btn.clicked.connect(lambda: self.setStyleSheet(""))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Red")
        btn.clicked.connect(lambda: self.setStyleSheet(
            "QWidget{background-color:red}"))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Green")
        btn.clicked.connect(lambda: self.setStyleSheet(
            "QWidget{background-color:green}"))
        btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)
        layout.addWidget(widget_to_style)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    example = QtWidgets.QListWidget()
    example.addItems(['one', 'two', 'three'])
    example = Example()
    switcher = ThemeSwitcher(example)

    switcher.resize(1000, 700)
    app.exec_()
