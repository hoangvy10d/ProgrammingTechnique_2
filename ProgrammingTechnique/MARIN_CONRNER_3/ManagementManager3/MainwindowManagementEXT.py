from PyQt6.QtWidgets import QMainWindow

from FINAL_PROJECT.ManagementManager.MainwindowManagementManager import Ui_MainWindow


class MainwindowManagement(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.users = self.dc.get_all_users()
        self.selected_cate = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_users_ui()
        self.setupSignalANDslot()
        self.ui.lineEditNAME_MANAGER.setText(f"Xin chào, {objectname của login}")

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalANDslot(self):
        self.pushButtonSAVE.clicked.connect(self.process_save)
        self.pushButtonBROWSER.clicked.connect(self.process_browser)
        self.pushButtonWRITEREVIEW.clicked.connect(self.process_writeReview)

    def process_browser(self):
        self.MainWindow.close()  # close login window
        self.mainwindow = QMainWindow()
        self.myui = Mainwindow85()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    def process_writeReview(self):
        self.MainWindow.close()  # close login window
        self.mainwindow = QMainWindow()
        self.myui = Mainwindow85()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def process_save(self):
        #Step 1: get user input information:
        userid = self.lineEditUSERID.text()
        username = self.lineEditUSERNAME.text()
        password = float(self.lineEditPASSWORD.text())
        fan_num = int(self.lineEditFANFIC.text())
        email = self.lineEditEMAIL.text()
        sign_up=int(self.lineEditSIGNUPDATE.text())

        #Step 2: create Object Model
        self.users = self.dc.get_all_users()
        u= User(userid, username, password, fan_num, email,sign_up)
        index=self.dc.check_existing_user(self.u.userid) #để tên giống trong class users
        if index==-1:#not found-->insert new
            self.users.append(u)
        else:#found -> update
            self.users[index]=u
        #Step 3: Save all object into Hard disk:
        jff = JsonFileFactory()
        filename = "../dataset/users.json"
        jff.write_data(self.users, filename)
        #Step 4: Re-display data into GUI:
        if self.selected_user!=None:
            self.products = self.dc.get_products_by_cate(self.selected_cate.cateid)
        else:
            self.products = self.dc.get_products_by_cate(p.cateid)
        self.show_products_ui()




    def remove_product(self):
        #Step 1: Find the product that we want to remove it
        userid=self.lineEditUSERID.text()
        self.users=self.dc.get_all_users()
        index=self.dc.check_existing_product(self.products,userid)
        if index==-1:#not found->then end the algorithm
            return
        #Step 2: Remove product by index
        self.users.pop(index)
        #Step 3: Save all data into Hard Disk:
        jff = JsonFileFactory()
        filename = "../dataset/users.json"
        jff.write_data(self.users, filename)
        # Step 4: Re-display data into GUI:
        if self.selected_cate!=None:
            self.products=self.dc.get_products_by_cate(self.selected_cate.cateid)
        else:
            self.users =self.dc.get_all_users()
        self.show_users_ui()
        self.clear_detail_data()



