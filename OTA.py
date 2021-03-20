import requests
import json
import os
from PyQt5.QtCore import QProcess, QRunnable, QThreadPool, pyqtSlot, QThread, QMetaObject, Qt, Q_ARG, QObject, pyqtSignal

class OTARunnable(QRunnable):
    def __init__(self, url):
        QRunnable.__init__(self)
        self.url = url
    def run(self):
        dataJSONContent = requests.get(self.url).content
        dataDict = json.loads(dataJSONContent.decode())
        with open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "characterData.json"),'w',encoding='utf-8') as dataJSONFile:
            json.dump(dataDict, dataJSONFile, ensure_ascii=False)

def devMain():
    url = "https://github.91chifun.workers.dev//https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json"
    newOTARunnable = OTARunnable(url)
    newOTARunnable.run()
    
if __name__ == "__main__":
    # 直接执行则为开发模式入口
        devMain()
