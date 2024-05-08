import sys
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow

app = QApplication(sys.argv)

with open("style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)

w = MainWindow()

app.exec()




'''

pyside6-uic pycode.ui -o pycode.py
pyside6-rcc res.qrc -o res_rc.py

'''