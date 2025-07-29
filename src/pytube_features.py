import os
from pytube import YouTube, Playlist
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class PytubeDownload():
    def __init__(self, url, download_path, progressObj):
        os.chdir(download_path)
        self.url = url
        self.progressObj = progressObj

    def onYTProgress(self, stream, chunk, remains):
        '''
        單獨影片的進度條顯示
        '''
        total = stream.filesize
        percent = (total-remains) / total * 100
        self.progressObj.setValue(int(percent))
    
    def onPListProgress(self, num):
        '''
        播放清單的進度條顯示
        因為Playlist物件沒有on_progress_callback
        只好用總數為單位
        '''
        self.progressObj.setValue(int(num))

    def isPlaylist(self):
        str = self.url.split("/")[3].split("?")[0]
        self.progressObj.setValue(0)
        if str=='playlist':
            p = Playlist(self.url)
            self.progressObj.setFormat('%v/%m')
            self.progressObj.setRange(0, len(p))
            return [True, p]
        else:
            yt = YouTube(self.url, on_progress_callback=self.onYTProgress)
            self.progressObj.setFormat('%p%')
            self.progressObj.setRange(0, 100)
            return [False, yt]

    def downloadVideo(self):
        res, obj = self.isPlaylist()
        if res:
            num = 1
            for i in obj.videos:
                i.streams.first().download()
                self.onPListProgress(num)
                num+=1
        else:
            obj.streams.filter().get_highest_resolution().download()

    def downloadAudio(self):
        res, obj = self.isPlaylist()
        if res:
            num = 1
            for i in obj.videos:
                i.streams.filter(only_audio=True).first().download()
                self.onPListProgress(num)
                num+=1
        else:
            obj.streams.filter(only_audio=True).first().download()