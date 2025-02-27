from PyQt6.QtWidgets import QApplication, QMainWindow

from DoAnNhomCK.ManagementManager2_1.ui.ManagerRemoveExt import ManagerRemoveExt

app=QApplication([])
mainwindow=QMainWindow()
myui=ManagerRemoveExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()