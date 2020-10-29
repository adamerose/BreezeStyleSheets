
import sys, os
sys.path.append(os.path.dirname(__file__))

with open("./styles/breeze/dark.qss") as f:
    import styles.breeze.breeze_resources
    dark = f.read()

with open("./styles/style.qss") as f:
    import styles.resources
    mydark = f.read()
    
with open("./styles/breeze/light.qss") as f:
    import styles.breeze.breeze_resources
    light = f.read()