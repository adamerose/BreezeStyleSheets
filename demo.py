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
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     self.setStyleSheet("")])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QtStylish Dark")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     self.setStyleSheet(qtstylish.mydark())])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QtStylish Light")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     self.setStyleSheet(qtstylish.mylight())])
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QDarkStyle")
        btn.clicked.connect(lambda: [print("Reloading styles..."),
                                     importlib.reload(qtstylish),
                                     print("Done"),
                                     self.setStyleSheet(qtstylish.qdarkstyle())])
        btn_layout.addWidget(btn)

        ###################

        # theme_btn_layout = QtWidgets.QHBoxLayout()
        # for style in QtWidgets.QStyleFactory().keys():
        #     btn = QtWidgets.QPushButton(style)
        #     btn.clicked.connect(lambda _, s=style: [app.setStyle(QtWidgets.QStyleFactory.create(s)),
        #                                             print(f"Setting style to {s}")])
        #     theme_btn_layout.addWidget(btn)
        # layout.addLayout(theme_btn_layout)

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
