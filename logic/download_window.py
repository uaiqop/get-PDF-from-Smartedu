import sys
import requests
import pathlib
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from ui import download_window
from logic import download_thread, get_config


url: str = ""
file_name: str = ""


def initialize(title, download_url):
    """
    接收从main_window模块传递来的url和教材标题
    :param title:
    :param download_url:
    :return:
    """
    # 全局变量声明
    global url
    global file_name
    url = download_url
    file_name = title + ".pdf"


class MainWindow(QMainWindow, download_window.Ui_MainWindow_download, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.file_path = None
        self.download_thread = None

        self.setupUi(self)

        # 禁止调整窗口大小
        self.setFixedSize(self.width(), self.height())

        # 禁止窗口最大化，最小化和关闭
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        # 阻塞父类窗口，使父窗口不能点击
        self.setWindowModality(Qt.ApplicationModal)

        # 调整进度条为0
        self.progressBar_download.setValue(0)

    def showEvent(self, *args, **kwargs):
        """
        窗口显示后执行
        :param args:
        :param kwargs:
        :return:
        """
        self.start_download()

    def start_download(self):
        global file_name
        # 获取文件的数据
        # 文件大小
        file_size = requests.get(url, stream=True).headers['Content-Length']
        # 下载完整路径
        self.file_path = get_config.get_download_dir("./config.json") + fr"\{file_name}"
        # 文件对象创建
        file_obj = open(self.file_path, 'wb')

        # 创建下载线程
        self.download_thread = download_thread.DownloadThread(url, file_size, file_obj, buffer=10240)
        self.download_thread.download_proess_signal.connect(self.set_progressbar_value)
        # 开始线程
        self.download_thread.start()

    def set_progressbar_value(self, value):
        """
        设置进度条
        :param value:
        :return:
        """
        self.progressBar_download.setValue(value)
        if value == 100:
            # 打开文件夹并且选中刚刚下载的文件
            os.system(f'explorer /select, "{self.file_path}')
            # 关闭下载窗口
            self.close()
