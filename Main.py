from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6 import uic
from Inferance import runInferance
import sys

app = QApplication(sys.argv)
window = uic.loadUi('main.ui')
Info = uic.loadUi('Dialog.ui')

def showInferance():

    runInferance()

def showInfo():
    Info.show()

def quitApp():
    sys.exit()


window.show()

start = window.findChild(QPushButton, "ButtonStart")
start.clicked.connect(showInferance)

info = window.findChild(QPushButton, "ButtonInfo")
info.clicked.connect(showInfo)

appQuit = window.findChild(QPushButton, "ButtonQuit")
appQuit.clicked.connect(quitApp)

sys.exit(app.exec())
