from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # South tabs on left side
        self.dock1 = QtWidgets.QDockWidget("One")
        self.dock2 = QtWidgets.QDockWidget("Two")
        self.dock3 = QtWidgets.QDockWidget("Three")
        self.content1 = QtWidgets.QWidget()
        self.content1.setStyleSheet("background-color:#330000;")
        self.content1.setMinimumSize(QtCore.QSize(50, 50))
        self.content2 = QtWidgets.QWidget()
        self.content2.setStyleSheet("background-color:#770000;")
        self.content2.setMinimumSize(QtCore.QSize(50, 50))
        self.content3 = QtWidgets.QWidget()
        self.content3.setStyleSheet("background-color:#AA0000;")
        self.content3.setMinimumSize(QtCore.QSize(50, 50))
        self.dock1.setWidget(self.content1)
        self.dock2.setWidget(self.content2)
        self.dock3.setWidget(self.content3)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock1)
        self.tabifyDockWidget(self.dock1, self.dock2)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock3)
        self.setDockOptions(self.GroupedDragging | self.AllowTabbedDocks | self.AllowNestedDocks)
        self.setTabPosition(Qt.AllDockWidgetAreas, QtWidgets.QTabWidget.North)

        # North tabs on right side
        self.north_dock1 = QtWidgets.QDockWidget("One")
        self.north_dock2 = QtWidgets.QDockWidget("Two")
        self.north_dock3 = QtWidgets.QDockWidget("Three")
        self.north_content1 = QtWidgets.QWidget()
        self.north_content1.setStyleSheet("background-color:#003300;")
        self.north_content1.setMinimumSize(QtCore.QSize(50, 50))
        self.north_content2 = QtWidgets.QWidget()
        self.north_content2.setStyleSheet("background-color:#007700;")
        self.north_content2.setMinimumSize(QtCore.QSize(50, 50))
        self.north_content3 = QtWidgets.QWidget()
        self.north_content3.setStyleSheet("background-color:#00AA00;")
        self.north_content3.setMinimumSize(QtCore.QSize(50, 50))
        self.north_dock1.setWidget(self.north_content1)
        self.north_dock2.setWidget(self.north_content2)
        self.north_dock3.setWidget(self.north_content3)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.north_dock1)
        self.tabifyDockWidget(self.north_dock1, self.north_dock2)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.north_dock3)
        self.setDockOptions(self.GroupedDragging | self.AllowTabbedDocks | self.AllowNestedDocks)
        self.setTabPosition(Qt.LeftDockWidgetArea, QtWidgets.QTabWidget.South)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    example = Example()
    example.show()
    app.exec_()
