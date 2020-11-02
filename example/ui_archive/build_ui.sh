pyuic5 -x example_buttons.ui -o example_buttons.py
pyuic5 -x example_containers.ui -o example_containers.py
pyuic5 -x example_controls.ui -o example_controls.py
pyuic5 -x example_displays.ui -o example_displays.py
pyuic5 -x example_inputs.ui -o example_inputs.py
pyuic5 -x example_menus.ui -o example_menus.py
pyuic5 -x example_tabs.ui -o example_tabs.py
pyuic5 -x example_widgets.ui -o example_widgets.py

# https://stackoverflow.com/a/49652982/3620725
#find . -type f -name "example_*.py" -exec sed -i 's:(object):(QtWidgets.QWidget):g' {} +
find . -type f -name "example_*.py" -exec sed -i 's:Ui_MainWindow:Ui_Form:g' {} +
#

