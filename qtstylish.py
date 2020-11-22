import sys
import os
import qtsass
import importlib
import pyqt5ac
from compiled import qtstylish_rc

dirname = os.path.dirname(__file__)

DARK = None
LIGHT = None
with open(os.path.join(dirname, "compiled/dark.qss")) as f:
    DARK = f.read()
with open(os.path.join(dirname, "compiled/light.qss")) as f:
    LIGHT = f.read()


def dark():
    compile()
    return DARK


def light():
    compile()
    return LIGHT


def qdarkstyle():
    with open(os.path.join(dirname, "alternatives/qdarkstyle/style.qss")) as f:
        import alternatives.qdarkstyle.style_rc
        return f.read()


def compile():
    # Compule SCSS into QSS
    qtsass.compile_filename(os.path.join(dirname, "./styling/dark.scss"),
                            os.path.join(dirname, "./compiled/dark.qss"))
    qtsass.compile_filename(os.path.join(dirname, "./styling/light.scss"),
                            os.path.join(dirname, "./compiled/light.qss"))
    # Compile resources defined by style.qrc into a python module
    os.system("pyrcc5 ./styling/main.qrc -o ./compiled/qtstylish_rc.py")

    # This part is for hot reload
    with open(os.path.join(dirname, "compiled/dark.qss")) as f:
        global DARK
        DARK = f.read()
    with open(os.path.join(dirname, "compiled/light.qss")) as f:
        global LIGHT
        LIGHT = f.read()


if __name__ == "__main__":
    compile()


# TODO
# https://stackoverflow.com/a/5510599/3620725
# #4169E1
