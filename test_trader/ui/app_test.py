from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QMenuBar, QMenu,
    QLabel, QVBoxLayout, QWidget, QStyle, QDockWidget, QListWidget
)

def on_file():
    status_label.setText("file")

def on_clear():
    status_label.setText("cleared")

    #这样是修改了标签的值，但之前使用这个标签的可能访问的是标签的对象，导致修改没有意义


app = QtWidgets.QApplication([])
#application是Qt的核心内，负责协调，核心逻辑等，其一定要实例化
#并且其是通过instance获取的单例对象
#其他功能模块通过instance方法访问这个类
main_window = QtWidgets.QMainWindow()
main_window.setWindowTitle("test")
main_window.resize(400, 300)

main_window.statusBar()
central_widget = QtWidgets.QWidget()
status_label = QLabel("waiting")
central_layout = QVBoxLayout(central_widget)
central_layout.addWidget(status_label)
main_window.setCentralWidget(central_widget)

file_icon = QtGui.QIcon(QApplication.style().standardIcon(QStyle.SP_FileIcon))
file_action = QtGui.QAction("file", main_window)
file_action.setIcon(file_icon)
file_action.setStatusTip("file1")
file_action.triggered.connect(on_file)

clear_icon = QtGui.QIcon(QApplication.style().standardIcon(QStyle.SP_LineEditClearButton))
clear_action = QtGui.QAction("clear", main_window)
clear_action.setIcon(clear_icon)
clear_action.setStatusTip("clear")
clear_action.triggered.connect(on_clear)

'''toolbar'''
toolbar = QToolBar("maintoolbar", main_window)
toolbar.addAction(file_action)
toolbar.addAction(clear_action)
toolbar.addSeparator()
toolbar.setMovable(False)
toolbar.setFloatable(False)
toolbar.setAllowedAreas(QtCore.Qt.TopToolBarArea | QtCore.Qt.BottomToolBarArea)
main_window.addToolBar(toolbar)



menubar = main_window.menuBar()
file_menu = menubar.addMenu("file")
file_menu.addAction(file_action)
file_menu.addAction(clear_action)

'''dock'''
dock = QDockWidget("list", main_window)
main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
file_list = QListWidget()
file_list.addItems(["file1","file2","file3"])
dock.setWidget(file_list)


main_window.show()
app.exec()

