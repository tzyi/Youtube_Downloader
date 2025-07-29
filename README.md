# youtube_downloader
使用PyQt6建造一個下載Youtube影片與音訊的應用程式

- [Window(.exe)](https://github.com/cabie8399/youtube_downloader/releases)
<br>

![](https://images2.imgbox.com/e2/e0/dttX4PTb_o.jpg)


# 執行程式
```bash
cd src
python main.py
```

# 打包成.exe
```basg
cd src
pyinstaller -i .\img\yt.png -w main.py
```
- 會生成/dist，將img/整個資料夾複製到/dist/main，否則icon會消失