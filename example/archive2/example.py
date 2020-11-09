from PyQt5 import QtWidgets

import example_widgets, example_buttons, example_dock, example_menus, example_containers, \
    example_other, example_inputs, example_tabs, example_displays, example_controls

from pandasgui import show
from pandasgui.datasets import titanic


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
                  example_other]:
            self.tab_widget.addTab(x.Example(), x.__name__.split("_")[1])
        gui = show(titanic, settings={'block': False})
        self.tab_widget.addTab(gui, 'pandasgui')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    example = Example()
    example.show()
    app.exec_()
