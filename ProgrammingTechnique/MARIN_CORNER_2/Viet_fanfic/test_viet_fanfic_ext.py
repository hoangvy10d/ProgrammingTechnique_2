from PyQt6.QtWidgets import QMainWindow, QApplication

from MARIN_CORNER_2.Viet_fanfic.Viet_fanfic_ext import Viet_fanfic_ext

app=QApplication([])
Mainwindow=QMainWindow()
myui=Viet_fanfic_ext()
myui.setupUi(Mainwindow)
myui.showWindow()
app.exec()