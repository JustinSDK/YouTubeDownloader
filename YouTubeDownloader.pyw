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
        leng = len(urls)
        if leng == 0:
            return
            
        dest = self.destPath()
        ui = self.ui
        
        def download():
            ui.progressBar.setValue(5)
            for i, url in enumerate(urls):
                YouTube(url).streams.filter(only_audio=True).filter(subtype='mp4').first().download(dest)
                ui.progressBar.setValue((i + 1) / leng * 100)
            ui.progressBar.setValue(100)        
        
        Thread(target = download).start()                
    
    def downloadVideo(self):
        urls = self.urls()
        leng = len(urls)
        if leng == 0:
            return
            
        dest = self.destPath()
        ui = self.ui
        
        def download():
            ui.progressBar.setValue(5)
            for i, url in enumerate(urls):
                YouTube(url).streams.filter(subtype='mp4').first().download(dest)
                ui.progressBar.setValue((i + 1) / leng * 100)
            ui.progressBar.setValue(100)        
        
        Thread(target = download).start()
        

    def destPath(self):
        return self.ui.lineEditDest.text().strip()
        
    def urls(self):        
        return [url.strip() for url in re.split(r'\n', self.ui.plainTextEditUrls.toPlainText().strip())]

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())