# Form implementation generated from reading ui file 'D:\KTLT\ProgrammingTechnique\MARIN_CORNER_2\UserRead2_1\UserReadReview.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 694)
        MainWindow.setStyleSheet("background-color: rgb(250, 232, 237);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 450, 881, 191))
        self.groupBox.setStyleSheet("background-color: rgb(255, 178, 197);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(203, 235, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_Date = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Date.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.gridLayout.addWidget(self.lineEdit_Date, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_Title = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Title.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Title.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.gridLayout.addWidget(self.lineEdit_Title, 0, 1, 1, 1)
        self.lineEdit_Character = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Character.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Character.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Character.setObjectName("lineEdit_Character")
        self.gridLayout.addWidget(self.lineEdit_Character, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.lineEdit_Author = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Author.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Author.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.gridLayout.addWidget(self.lineEdit_Author, 0, 3, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(4, -1, 4, -1)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox.setWhatsThis("")
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\KTLT\\ProgrammingTechnique\\MARIN_CORNER_2\\UserRead2_1\\../images/1Star.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.comboBox.addItem(icon, "")
        self.comboBox.setItemText(0, "")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.pushButton_Back = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_Back.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.horizontalLayout_8.addWidget(self.pushButton_Back)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 2, 1, 2)
        self.lineEdit_LinkFilm = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_LinkFilm.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_LinkFilm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_LinkFilm.setObjectName("lineEdit_LinkFilm")
        self.gridLayout.addWidget(self.lineEdit_LinkFilm, 1, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 5)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 0, 331, 411))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 178, 197);\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_Search = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_Search.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_Search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_Search.setText("")
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.horizontalLayout.addWidget(self.lineEdit_Search)
        self.pushButton_Search = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_Search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_Search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\KTLT\\ProgrammingTechnique\\MARIN_CORNER_2\\UserRead2_1\\../images/search.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Search.setIcon(icon1)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.Qlistview_da_viet = QtWidgets.QListView(parent=self.groupBox_2)
        self.Qlistview_da_viet.setMinimumSize(QtCore.QSize(0, 0))
        self.Qlistview_da_viet.setStatusTip("")
        self.Qlistview_da_viet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Qlistview_da_viet.setObjectName("Qlistview_da_viet")
        self.verticalLayout_2.addWidget(self.Qlistview_da_viet)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Film = QtWidgets.QPushButton(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Film.setFont(font)
        self.pushButton_Film.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.pushButton_Film.setObjectName("pushButton_Film")
        self.horizontalLayout_2.addWidget(self.pushButton_Film)
        self.pushButton_Fanfic = QtWidgets.QPushButton(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Fanfic.setFont(font)
        self.pushButton_Fanfic.setStyleSheet("background-color: rgb(203, 235, 255);\n"
"")
        self.pushButton_Fanfic.setObjectName("pushButton_Fanfic")
        self.horizontalLayout_2.addWidget(self.pushButton_Fanfic)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 501, 401))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("D:\\KTLT\\ProgrammingTechnique\\MARIN_CORNER_2\\UserRead2_1\\../../../Ky thuat lap trinh/FINALEXAM/readofuserandreviewmana/images/logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Date released</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Title</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Author</p></body></html>"))
        self.pushButton_Back.setText(_translate("MainWindow", "Back"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Link film</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Characters</p></body></html>"))
        self.lineEdit_Search.setPlaceholderText(_translate("MainWindow", "Search"))
        self.pushButton_Film.setText(_translate("MainWindow", "Film"))
        self.pushButton_Fanfic.setText(_translate("MainWindow", "Fanfic"))
