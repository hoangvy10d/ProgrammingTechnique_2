from ProgrammingTechnique.MARIN_CORNER_2.Viet_fanfic.Viet_fanfic import Ui_MainWindow


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
    """
    khi post, mọi thông tin sẽ được lưu + ngày hiện tại
    bài post sẽ được hiện trong history mới nhất
    cập nhật trong file đc lưu, khi search sẽ tìm thấy
    """
    def process_back(self):
        pass
    """
    Khi nhấn back thì sẽ quay lại cái số 2
    giao diện hiện tại sẽ tắt để hiện giao diện số 2
    """
    def process_search(self):
        pass
    """
    Khi nhập vài chữ, máy sẽ tự động read file để đề xuất 
    những thứ trùng khớp với từ mình đag nhập
    """
    def process_save(self):
        pass
    """
    save là save cái script
    bài được save sẽ được lưu title, bản script đag viết dở
    khi save xong sẽ hiện bản qboxmessage để confirm là đã save thành công
    khi thoát ctrình, quay lại vẫn thấy bản save cũ
    """

