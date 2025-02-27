from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QInputDialog, QMessageBox

from FINALEXAM.readofuserandreviewmana.UI.MainWindowuserreadnew import Ui_MainWindow


class MainwindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.model=QStandardItemModel()
        self.Qlistview_da_viet.setModel(self.model)
        self.Qlistview_da_viet.clicked.connect(self.display_selected_details)
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_Search.clicked.connect(self.process_search)

# hàm chức năng search:
    def process_search(self):
        name, ok = QInputDialog.getText(
            self.MainWindow,
            "Search by Name",
            "Enter the product name to search:"
        )
        if ok and name:
            name = name.strip().lower()
            filtered_products = [prod for prod in self.Qlistview_da_viet if prod.name.strip().lower() == name]
            self.display_search_results(filtered_products)

    def display_search_results(self, results):
        self.model.clear()
        if not results:
            QMessageBox.information(
                self.MainWindow,
                "No Results",
                "No products matched your criteria!"
            )
            return
        result_text = "\n".join(
            f" Name: {prod.name}"
            for prod in results
        )
        QMessageBox.information(
            self.MainWindow,
            "Search Results",
            result_text
        )

    def display_selected_details(self, index):
        """ Khi chọn sản phẩm trong QListView, hiển thị chi tiết vào các ô text """
        selected_item = self.model.itemFromIndex(index)
        product = selected_item.data()

        # Giả sử file UI có các QLabel như sau (cần khớp với tên thật trong Qt Designer)
        self.lineEdit_Author.setText(product.Author)
        self.lineEdit_Date.setText(product.Date)
        self.lineEdit_Title.setText(product.Titile)
        self.lineEdit_LinkFilm.setText({})
        self.lineEdit_Character.setText(product.Character)
        
