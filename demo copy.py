from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QPushButton, QVBoxLayout

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import Qt


class Table(QtWidgets.QTableView):
    def __init__(self, data=None):
        super().__init__()
        if data is None:
            data = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.setModel(self.TableModel(data))

    class TableModel(QtCore.QAbstractTableModel):
        def __init__(self, data):
            super().__init__()
            self.data = data

        def headerData(self, section: int, orientation: Qt.Orientation, role: int):
            if role == QtCore.Qt.DisplayRole:
                if orientation == Qt.Horizontal:
                    return "Column " + str(section)
                else:
                    return "Row " + str(section)

        def rowCount(self, parent=QtCore.QModelIndex()):
            return len(self.data)

        def columnCount(self, parent=QtCore.QModelIndex()):
            return len(self.data[0])

        def data(self, index, role=QtCore.Qt.DisplayRole):
            if role == QtCore.Qt.DisplayRole:
                row = index.row()
                col = index.column()
                return str(self.data[row][col])


class ExampleWidgets(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setup
        layout = QVBoxLayout()
        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        ####################################################
        # Small stuff
        ss_container = QtWidgets.QWidget()
        ss_layout = QtWidgets.QHBoxLayout()
        ss_container.setLayout(ss_layout)

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button2.setEnabled(False)

        checkbox1 = QtWidgets.QCheckBox("Checkbox 1")
        checkbox2 = QtWidgets.QCheckBox("Checkbox 2")
        checkbox2.setEnabled(False)

        radio1 = QtWidgets.QRadioButton("Radio 1")
        radio2 = QtWidgets.QRadioButton("Radio 2")
        radio2.setEnabled(False)
        radio_group = QtWidgets.QButtonGroup()
        radio_group.addButton(radio1)
        radio_group.addButton(radio2)

        spin_box = QtWidgets.QDoubleSpinBox()

        combo_box = QtWidgets.QComboBox()
        combo_box.addItems(["Item 1", "Item 2", "Item 3"])

        dial = QtWidgets.QDial()

        for item in [button1,
                     button2,
                     checkbox1,
                     checkbox2,
                     radio1,
                     radio2,
                     spin_box,
                     combo_box,
                     dial]:
            try:
                ss_layout.addWidget(item)
            except:
                ss_layout.addLayout(item)

        ####################################################
        # Big stuff
        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setSliderPosition(70)

        scroll_bar = QtWidgets.QScrollBar(Qt.Horizontal)

        progress_bar = QtWidgets.QProgressBar()
        progress_bar.setValue(30)
        tabs = QtWidgets.QTabWidget()
        tabs.addTab(QtWidgets.QWidget(), "Tab 1")
        tabs.addTab(QtWidgets.QWidget(), "Tab 2")
        tabs.addTab(QtWidgets.QWidget(), "Tab 3")

        table = Table()

        docks = QtWidgets.QMainWindow()
        dock1 = QtWidgets.QDockWidget("Dock 1")
        dock2 = QtWidgets.QDockWidget("Dock 2")
        dock3 = QtWidgets.QDockWidget("Dock 3")
        docks.setTabPosition(Qt.AllDockWidgetAreas, QtWidgets.QTabWidget.North)
        docks.addDockWidget(Qt.RightDockWidgetArea, dock1)
        docks.addDockWidget(Qt.RightDockWidgetArea, dock2)
        docks.addDockWidget(Qt.RightDockWidgetArea, dock3)
        docks.tabifyDockWidget(dock1, dock2)

        for item in [ss_container,
                     slider,
                     scroll_bar,
                     progress_bar,
                     tabs,
                     table,
                     docks]:
            layout.addWidget(item)


        ####################################################
        # Dialogs
class Demo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        import qtstylish

        example_ui = ExampleWidgets()

        layout = QtWidgets.QVBoxLayout()
        btn_layout = QtWidgets.QHBoxLayout()

        btn = QtWidgets.QPushButton("Unstyled")
        btn.clicked.connect(lambda: self.setStyleSheet(""))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Light")
        btn.clicked.connect(lambda: self.setStyleSheet(qtstylish.light))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Dark")
        btn.clicked.connect(lambda: self.setStyleSheet(qtstylish.dark))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("New Dark")
        btn.clicked.connect(lambda: self.setStyleSheet(qtstylish.new_dark))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("QDarkStyle")
        import qdarkstyle
        btn.clicked.connect(lambda: self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()))
        btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)
        layout.addWidget(example_ui)
        self.setLayout(layout)
        self.resize(1000,1000)
        self.show()

        app.setStyle('Fusion')
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = Demo()
    app.exec_()
