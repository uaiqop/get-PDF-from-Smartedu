import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from ui import download_window


class MainWindow(QMainWindow, download_window.Ui_MainWindow_download, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 禁止调整窗口大小
        self.setFixedSize(self.width(), self.height())

        # 禁止窗口最大化，最小化和关闭
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        # 阻塞父类窗口，使父窗口不能点击
        self.setWindowModality(Qt.ApplicationModal)
