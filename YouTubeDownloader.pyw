import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Ui_YouTubeDownloaderForm import Ui_YouTubeDownloaderForm

import re

from pytube import YouTube
from threading import Thread
from time import sleep

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_YouTubeDownloaderForm()
        self.ui.setupUi(self)
        
        self.ui.pushButtonVideo.clicked.connect(self.downloadVideo)
        self.ui.pushButtonAudio.clicked.connect(self.downloadAudio)
        
        self.show()
        
    def downloadAudio(self):
        urls = self.urls()
        if not urls:
            return

        Thread(
            target = AppWindow.download, 
            args=(self.ui, urls, self.destPath(), lambda stream: stream.filter(only_audio=True).filter(subtype='mp4'))
        ).start()                
    
    def downloadVideo(self):
        urls = self.urls()
        if not urls:
            return

        Thread(
            target = AppWindow.download, 
            args=(self.ui, urls, self.destPath(), lambda stream: stream.filter(subtype='mp4'))
        ).start()            
      
    def destPath(self):
        return self.ui.lineEditDest.text().strip()
        
    def urls(self):        
        return [url.strip() for url in re.split(r'\n', self.ui.plainTextEditUrls.toPlainText().strip())]

    @staticmethod      
    def download(ui, urls, dest, streamFilter):
        leng = len(urls)
        ui.progressBar.setValue(5)
        for i, url in enumerate(urls, start=1):
            streamFilter(YouTube(url).streams).filter(subtype='mp4').first().download(dest)
            ui.progressBar.setValue(i / leng * 100)        
                

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())