# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_download(object):
    def setupUi(self, MainWindow_download):
        MainWindow_download.setObjectName("MainWindow_download")
        MainWindow_download.resize(414, 60)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/64x64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_download.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow_download)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar_download = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_download.setProperty("value", 24)
        self.progressBar_download.setTextVisible(False)
        self.progressBar_download.setObjectName("progressBar_download")
        self.verticalLayout.addWidget(self.progressBar_download)
        MainWindow_download.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_download)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 22))
        self.menubar.setObjectName("menubar")
        MainWindow_download.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow_download)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_download)

    def retranslateUi(self, MainWindow_download):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_download.setWindowTitle(_translate("MainWindow_download", "下载中"))
import icon_rc
