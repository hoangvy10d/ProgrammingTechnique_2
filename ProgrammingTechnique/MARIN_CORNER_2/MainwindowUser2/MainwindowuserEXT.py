from PyQt6.QtWidgets import QMainWindow

from FINAL_PROJECT.MainwindowUser.Mainwindowuser import Ui_MainWindow


class Mainwindowuser(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalANDslot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalANDslot(self):
        self.pushButtonWRITRE.clicked.connect(self.process_write)
        self.pushButtonREAD.clicked.connect(self.process_read)
    def process_read(self):
        self.MainWindow.close()  # close functions user
        self.mainwindow = QMainWindow()
        self.myui = Mainwindowread()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def process_write(self):
        self.MainWindow.close()  # close functions user
        self.mainwindow = QMainWindow()
        self.myui = Mainwindowwrite()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    