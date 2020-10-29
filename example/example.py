from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Import examples UI
        from .ui.mw_menus_ui import Ui_MainWindow as ui_main
        from .ui.dw_buttons_ui import Ui_DockWidget as ui_buttons
        from .ui.dw_displays_ui import Ui_DockWidget as ui_displays
        from .ui.dw_inputs_fields_ui import Ui_DockWidget as ui_inputs_fields
        from .ui.dw_inputs_no_fields_ui import Ui_DockWidget as ui_inputs_no_fields
        from .ui.dw_widgets_ui import Ui_DockWidget as ui_widgets
        from .ui.dw_views_ui import Ui_DockWidget as ui_views
        from .ui.dw_containers_tabs_ui import Ui_DockWidget as ui_containers_tabs
        from .ui.dw_containers_no_tabs_ui import Ui_DockWidget as ui_containers_no_tabs

        window = QtWidgets.QMainWindow()

        ui = ui_main()
        ui.setupUi(window)

        window.setWindowTitle("Example")

        # Create docks for buttons
        dw_buttons = QtWidgets.QDockWidget()
        dw_buttons.setObjectName('buttons')
        ui_buttons = ui_buttons()
        ui_buttons.setupUi(dw_buttons)
        window.addDockWidget(Qt.RightDockWidgetArea, dw_buttons)

        # Add actions on popup toolbuttons
        menu = QtWidgets.QMenu()

        for action in ['Action A', 'Action B', 'Action C']:
            menu.addAction(action)

        ui_buttons.toolButtonDelayedPopup.setMenu(menu)
        ui_buttons.toolButtonInstantPopup.setMenu(menu)
        ui_buttons.toolButtonMenuButtonPopup.setMenu(menu)

        # Create docks for buttons
        dw_displays = QtWidgets.QDockWidget()
        dw_displays.setObjectName('displays')
        ui_displays = ui_displays()
        ui_displays.setupUi(dw_displays)
        window.addDockWidget(Qt.RightDockWidgetArea, dw_displays)

        # Create docks for inputs - no fields
        dw_inputs_no_fields = QtWidgets.QDockWidget()
        dw_inputs_no_fields.setObjectName('inputs_no_fields')
        ui_inputs_no_fields = ui_inputs_no_fields()
        ui_inputs_no_fields.setupUi(dw_inputs_no_fields)
        window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs_no_fields)

        # Create docks for inputs - fields
        dw_inputs_fields = QtWidgets.QDockWidget()
        dw_inputs_fields.setObjectName('inputs_fields')
        ui_inputs_fields = ui_inputs_fields()
        ui_inputs_fields.setupUi(dw_inputs_fields)
        window.addDockWidget(Qt.RightDockWidgetArea, dw_inputs_fields)

        # Create docks for widgets
        dw_widgets = QtWidgets.QDockWidget()
        dw_widgets.setObjectName('widgets')
        ui_widgets = ui_widgets()
        ui_widgets.setupUi(dw_widgets)
        window.addDockWidget(Qt.LeftDockWidgetArea, dw_widgets)

        # Create docks for views
        dw_views = QtWidgets.QDockWidget()
        dw_views.setObjectName('views')
        ui_views = ui_views()
        ui_views.setupUi(dw_views)
        window.addDockWidget(Qt.LeftDockWidgetArea, dw_views)

        # Create docks for containers - no tabs
        dw_containers_no_tabs = QtWidgets.QDockWidget()
        dw_containers_no_tabs.setObjectName('containers_no_tabs')
        ui_containers_no_tabs = ui_containers_no_tabs()
        ui_containers_no_tabs.setupUi(dw_containers_no_tabs)
        window.addDockWidget(Qt.LeftDockWidgetArea, dw_containers_no_tabs)

        # Create docks for containters - tabs
        dw_containers_tabs = QtWidgets.QDockWidget()
        dw_containers_tabs.setObjectName('containers_tabs')
        ui_containers_tabs = ui_containers_tabs()
        ui_containers_tabs.setupUi(dw_containers_tabs)
        window.addDockWidget(Qt.LeftDockWidgetArea, dw_containers_tabs)

        # Tabify right docks
        window.tabifyDockWidget(dw_buttons, dw_displays)
        window.tabifyDockWidget(dw_displays, dw_inputs_fields)
        window.tabifyDockWidget(dw_inputs_fields, dw_inputs_no_fields)

        # Tabify left docks
        window.tabifyDockWidget(dw_containers_no_tabs, dw_containers_tabs)
        window.tabifyDockWidget(dw_containers_tabs, dw_widgets)
        window.tabifyDockWidget(dw_widgets, dw_views)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(window)
        self.setLayout(self.layout)
