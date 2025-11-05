from PySide6 import QtGui, QtWidgets, QtCore
import sys
import qdarkstyle
from .setting import SETTINGS


'''
qt signal and slot:
1. all events came from xserver were put into event queue.
2. main thread repeated deal with all events.
3. click() are called, emit a signal, which is dealt within the thread or
sent to working thread. all information needed to perform the slot is bound 
to signal with connect() method.

'''

def main():
    qapp: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    qapp.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))
    font: QtGui.QFont = QtGui.QFont(SETTINGS["font.family"], SETTINGS["font.size"])
    qapp.setFont(font)

