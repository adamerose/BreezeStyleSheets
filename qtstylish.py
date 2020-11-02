import sys, os

dirname = os.path.dirname(__file__)


def dark():
    with open(os.path.join(dirname, "alternatives/breeze/dark.qss")) as f:
        import alternatives.breeze.breeze_resources
        return f.read()


def mydark():
    with open(os.path.join(dirname, "styling/compiled/style.qss")) as f:
        import styling.compiled.resources
        return f.read()


def light():
    with open(os.path.join(dirname, "alternatives/breeze/light.qss")) as f:
        import alternatives.breeze.breeze_resources
        return f.read()


def qdarkstyle():
    with open(os.path.join(dirname, "alternatives/qdarkstyle/style.qss")) as f:
        import alternatives.qdarkstyle.style_rc
        return f.read()
