import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import main_window
from logic import download_window


class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 禁止调整窗口大小
        self.setFixedSize(self.width(), self.height())

        self.window_download = download_window.MainWindow()
        self.pushButton_get.clicked.connect(self.get)

    def get(self):
        # self.window_download.exec_()
        self.window_download.show()


