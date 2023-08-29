from PyQt5.QtWidgets import *

from ui import main_window
from logic import download_window, get_data


class MainWindow(QMainWindow, main_window.Ui_MainWindow, QMessageBox):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 禁止调整窗口大小
        self.setFixedSize(self.width(), self.height())

        # 创建下载窗口实例
        self.window_download = download_window.MainWindow()

        # 连接按钮点击事件
        self.pushButton_get.clicked.connect(self.get)

    def get(self):
        # 获取用户输入的url
        url = self.lineEdit_url.text()

        # 将教材的链接转换为pdf的链接
        download_url = get_data.get_pdf_url(url)

        # 获取教材标题
        title = get_data.get_pdf_name(url)

        # 检查是否能正常提取下载链接
        if download_url is not None:
            # 将用户输入的url通过函数传递给download_window模块
            download_window.initialize(title, download_url)
            # 显示下载窗口
            self.window_download.show()
        else:
            # 警告用户输入错误
            QMessageBox.warning(self, '链接错误', '请输入教材对应的链接')
