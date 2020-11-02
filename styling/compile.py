import os
import qtsass

os.chdir(os.path.dirname(__file__))

# Compule SCSS into QSS
qtsass.compile_filename("./dark.scss", "./compiled/style.qss")
# Compile resource files defined by style.qrc into a python module
os.system("pyrcc5 ./style.qrc -o ./compiled/resources.py")