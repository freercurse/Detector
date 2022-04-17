from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6 import uic

import sys

app = QApplication(sys.argv)
window = uic.loadUi('main.ui')
Info = uic.loadUi('Dialog.ui')


def showInfo():
    Info.show()

def quitApp():
    sys.exit()


window.show()

info = window.findChild(QPushButton, "ButtonInfo")
info.clicked.connect(showInfo)

appQuit = window.findChild(QPushButton, "ButtonQuit")
appQuit.clicked.connect(quitApp)

sys.exit(app.exec())
