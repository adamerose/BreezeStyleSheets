import sys
import os
import qtsass

dirname = os.path.dirname(__file__)


def mydark():

    with open(os.path.join(dirname, "styling/compiled/style.qss")) as f:
        os.chdir(os.path.join(dirname, 'styling'))
        qtsass.compile_filename("./dark.scss", "./compiled/style.qss")
        os.system("pyrcc5 ./style.qrc -o ./compiled/resources.py")
        import styling.compiled.resources

        return f.read()


def mylight():
    with open(os.path.join(dirname, "styling/compiled/style.qss")) as f:
        os.chdir(os.path.join(dirname, 'styling'))
        qtsass.compile_filename("./light.scss", "./compiled/style.qss")
        os.system("pyrcc5 ./style.qrc -o ./compiled/resources.py")
        import styling.compiled.resources
        return f.read()


def qdarkstyle():
    with open(os.path.join(dirname, "alternatives/qdarkstyle/style.qss")) as f:
        import alternatives.qdarkstyle.style_rc
        return f.read()


# TODO
# https://stackoverflow.com/a/5510599/3620725
# #4169E1
