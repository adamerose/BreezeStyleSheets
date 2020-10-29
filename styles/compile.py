import sys, os
os.chdir(os.path.dirname(__file__))
import qtsass
qtsass.compile_filename("./dark.scss", "./style.qss")
os.system("pyrcc5 style.qrc -o resources.py")