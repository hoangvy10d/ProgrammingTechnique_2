from MARIN_CORNER_2.Viet_fanfic.Viet_fanfic import Ui_MainWindow


class Viet_fanfic_ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_Post.clicked.connect(self.process_post)
        self.pushButton_Back.clicked.connect(self.process_back)
        self.pushButton_Search.clicked.connect(self.process_search)
        self.pushButton_Save.clicked.connect(self.process_save)
    def process_post(self):
        pass
    def process_back(self):
        pass
    def process_search(self):
        pass
    def process_save(self):
        pass

