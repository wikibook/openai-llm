import datetime
import time
import webbrowser

# 1시간마다 임의의 노트북 열기
for i in range(12):
    browse = webbrowser.get("chrome")
    browse.open("<임의의 노트북 URL>")
    print(i, datetime.datetime.today())
    time.sleep(60*60)
