# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YouTubeDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YouTubeDownloaderForm(object):
    def setupUi(self, YouTubeDownloaderForm):
        YouTubeDownloaderForm.setObjectName("YouTubeDownloaderForm")
        YouTubeDownloaderForm.resize(664, 499)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(YouTubeDownloaderForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDest = QtWidgets.QLabel(YouTubeDownloaderForm)
        self.labelDest.setObjectName("labelDest")
        self.verticalLayout.addWidget(self.labelDest)
        self.lineEditDest = QtWidgets.QLineEdit(YouTubeDownloaderForm)
        self.lineEditDest.setObjectName("lineEditDest")
        self.verticalLayout.addWidget(self.lineEditDest)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelUrls = QtWidgets.QLabel(YouTubeDownloaderForm)
        self.labelUrls.setObjectName("labelUrls")
        self.verticalLayout_2.addWidget(self.labelUrls)
        self.urlsScrollArea = QtWidgets.QScrollArea(YouTubeDownloaderForm)
        self.urlsScrollArea.setWidgetResizable(True)
        self.urlsScrollArea.setObjectName("urlsScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 331))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEditUrls = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEditUrls.setObjectName("plainTextEditUrls")
        self.horizontalLayout_2.addWidget(self.plainTextEditUrls)
        self.urlsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.urlsScrollArea)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAudio = QtWidgets.QPushButton(YouTubeDownloaderForm)
        self.pushButtonAudio.setObjectName("pushButtonAudio")
        self.horizontalLayout.addWidget(self.pushButtonAudio)
        self.pushButtonVideo = QtWidgets.QPushButton(YouTubeDownloaderForm)
        self.pushButtonVideo.setObjectName("pushButtonVideo")
        self.horizontalLayout.addWidget(self.pushButtonVideo)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(YouTubeDownloaderForm)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)

        self.retranslateUi(YouTubeDownloaderForm)
        QtCore.QMetaObject.connectSlotsByName(YouTubeDownloaderForm)

    def retranslateUi(self, YouTubeDownloaderForm):
        _translate = QtCore.QCoreApplication.translate
        YouTubeDownloaderForm.setWindowTitle(_translate("YouTubeDownloaderForm", "YouTube 下載器"))
        self.labelDest.setText(_translate("YouTubeDownloaderForm", "下載至："))
        self.lineEditDest.setText(_translate("YouTubeDownloaderForm", "C:\\workspace"))
        self.labelUrls.setText(_translate("YouTubeDownloaderForm", "YouTube 網址清單："))
        self.pushButtonAudio.setText(_translate("YouTubeDownloaderForm", "下載聲音"))
        self.pushButtonVideo.setText(_translate("YouTubeDownloaderForm", "下載影片"))

