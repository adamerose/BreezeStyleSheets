from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from . import example_dock
from . import example_controls
from . import example_displays
from . import example_inputs
from . import example_menus
from . import example_tabs
from . import example_widgets
from . import example_buttons
from . import example_containers

import qtstylish


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        for x in [example_controls,
                  example_displays,
                  example_inputs,
                  example_menus,
                  example_tabs,
                  example_widgets,
                  example_buttons,
                  example_containers,
                  example_dock,
                  ]:
            self.tab_widget.addTab(x.Example(), x.__name__.split("_")[1])



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    example = Example()
    example.show()
    app.exec_()
