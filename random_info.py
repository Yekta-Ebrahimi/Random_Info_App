import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from sql import Database

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.database = Database("info_DB.db")
        self.ui.pushButton_show.clicked.connect(self.show_info)

    def show_info(self):
        category = self.ui.comboBox_topic.currentText()
        result = self.database.get_random_info(category)
        self.ui.textEdit_result.setText(result)

app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec())