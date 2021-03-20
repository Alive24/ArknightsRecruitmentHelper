from PIL import Image, ImageQt
import numpy as np
import sys
import os
import copy
import quamash
import asyncio
import logging
import win32gui
import re
import json
import cv2
from cnocr import CnOcr
from OTA import OTARunnable
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView, QLabel, QWidget, QTextBrowser, QMessageBox, QButtonGroup, QCheckBox, QDialog, QMenu, QAction, QPlainTextEdit
from PyQt5.QtCore import QProcess, QRunnable, QThreadPool, pyqtSlot, QThread, QMetaObject, Qt, Q_ARG, QObject, pyqtSignal
from PyQt5 import QtGui, QtCore, QtNetwork

## Version Info
global globalVersion
globalVersion = 'ArknightsRecruimentHelper-v0.0.1-beta1'
global dataDict


## PrepareInitialPaths
if not os.path.exists(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper")):
    os.makedirs(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper"))
if not os.path.exists(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "characterData.json")):
    with open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper",  "characterData.json"),'w',encoding='utf-8') as file:
        emptyDict = {"char_285_medic2": ""}
        json.dump(emptyDict, file, ensure_ascii=False)



## Prepare Local Modules
from exceptHookHandler import ExceptHookHandler
from GUI import Ui_ArknightsRecruimentHelperGUI
import util

## Prepare Logging
global_logger = logging.getLogger()

class GUIMainWin(QMainWindow, Ui_ArknightsRecruimentHelperGUI):
    def __init__(self, parent=None):
        super(GUIMainWin, self).__init__(parent)
        # Basic Setups
        self.setupUi(self)
        self.appExceptionHandler = ExceptHookHandler(self, logFile=os.path.join(os.path.expanduser('~'), "PCRJJCAnalyzer", "log.txt"))
        self.setWindowTitle(globalVersion)
        # Key Initializations
        self.handle = 0
        self.initializeHandleSelector()
        self.tagImageSceneList = [QGraphicsScene(), QGraphicsScene(), QGraphicsScene(), QGraphicsScene(), QGraphicsScene()]
        self.tagTypeList = ["", "", "", "", ""]
        # Handler Connections
        self.manualRecognizeAndAnalyzeButton.clicked.connect(self.recognizeAndAnalyze)
        self.updateDataButton.clicked.connect(self.updateData)
        self.ocrInstance = CnOcr(model_name='conv-lite-fc')
    def initializeHandleSelector(self):
        emulator_lst = dict()
        emulator_hwnd = ["subWin", "canvasWin", "BlueStacksApp"] # subWin: nox, ldplayer | canvasWin: mumu
        def check_emulator_window(hwnd, p):
            if win32gui.GetClassName(hwnd) in emulator_hwnd and hwnd not in emulator_lst:
                emulator_lst.update({hwnd: p})
            else:
                win32gui.EnumChildWindows(hwnd, check_emulator_window, p)
        def gui_get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                if win32gui.GetClassName(hwnd) == "UnityWndClass" and win32gui.GetWindowText(hwnd) == "PrincessConnectReDive": # DMM Game Player
                    # emulator_lst.update({hwnd: "DMM_PrincessConnectReDive"})
                    print("yo!")
                else:
                    win32gui.EnumChildWindows(hwnd, check_emulator_window, win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(gui_get_all_hwnd, 0)
        self.handleList = []
        for h,t in emulator_lst.items():
            if t is not "":
                self.handleList.append([h, t])
        self.titleList = [handle[1] for handle in self.handleList]
        self.handleSelectorComboBox.clear()
        self.handleSelectorComboBox.addItems(self.titleList)
        if len(self.titleList) == 1:
            self.handle = list(emulator_lst.keys())[0]
            self.queryStatusTag.setText('等待查询')
            self.queryStatusTag.setStyleSheet("color:green")
        else:
            self.queryStatusTag.setText("请选择句柄")
            self.queryStatusTag.setStyleSheet("color:red")
    def recognizeAndAnalyze(self, slotNum:[0,1,2,3]):
        self.tagOneLabel.setText("识别中...")
        self.tagTwoLabel.setText("识别中...")
        self.tagThreeLabel.setText("识别中...")
        self.tagFourLabel.setText("识别中...")
        self.tagFiveLabel.setText("识别中...")
        if self.handle == 0:
            QMessageBox.information(self, "No Handle", "No Handle")
            self.queryStatusTag.setText("请选择句柄")
            self.queryStatusTag.setStyleSheet("color:red")
            return
        gameImage = screen.grabWindow(self.handle).toImage() # 直接截取vbox子窗口和DMM的UnityWnd
        translatedCharH = gameImage.height()*config_dict['tagImageParams']['heightRatio']
        translatedCharW = gameImage.width()*config_dict['tagImageParams']['widthRatio']
        self.tagImageList = [gameImage.copy(gameImage.width() * ratioCordinates['x'], gameImage.height() * ratioCordinates['y'], translatedCharW, translatedCharH).scaledToWidth(100) for ratioCordinates in config_dict['tagImageParams']['tagLocationRatio']]
        self.tagImagePixList = [QtGui.QPixmap.fromImage(tagImage) for tagImage in self.tagImageList]
        self.tagImageItemList = [QGraphicsPixmapItem(tagImagePix) for tagImagePix in self.tagImagePixList]
        for i in range(len(self.tagImageSceneList)):
            self.tagImageSceneList[i].addItem(self.tagImageItemList[i])
        self.tagImageOneGraphicsView.setScene(self.tagImageSceneList[0])
        self.tagImageTwoGraphicsView.setScene(self.tagImageSceneList[1])
        self.tagImageThreeGraphicsView.setScene(self.tagImageSceneList[2])
        self.tagImageFourGraphicsView.setScene(self.tagImageSceneList[3])
        self.tagImageFiveGraphicsView.setScene(self.tagImageSceneList[4])
        # tagImageToTagTypeRunnableList = []
        # for i in range(5):
        #     tagImageToTagTypeRunnableList.append(tagImageToTagTypeRunnable(self.tagImageList[i], i, self))
        try:
            for i in range(5):
                rawImage = self.tagImageList[i].convertToFormat(4)
                w = rawImage.width()
                h = rawImage.height()
                ptr = rawImage.bits()
                ptr.setsize(rawImage.byteCount())
                preparedImage = np.array(ptr).reshape(h, w, 4) #此处完成转换
                preparedImage = cv2.cvtColor(preparedImage, cv2.COLOR_BGRA2BGR)
                tagType = "".join(self.ocrInstance.ocr_for_single_line(preparedImage))
                tagType = re.sub('[\x00-\xff]', '', tagType)
                self.tagTypeList[i] = tagType
                if i == 0:
                    self.tagOneLabel.setText(tagType)
                if i == 1:
                    self.tagTwoLabel.setText(tagType)
                if i == 2:
                    self.tagThreeLabel.setText(tagType)
                if i == 3:
                    self.tagFourLabel.setText(tagType)
                if i == 4:
                    self.tagFiveLabel.setText(tagType)
        except:
            pass
        self.tagTypeList = list(filter(lambda item: item != "新手", self.tagTypeList))
        candidateList = []
        for key in list(dataDict.keys()):
            try:
                processedTagList = copy.deepcopy(dataDict[key]["tagList"])
                if dataDict[key]['position'] == "RANGED":
                    processedTagList.append("远程位")
                else:
                    processedTagList.append("近战位位")
                intersection = list(set(processedTagList) & set(self.tagTypeList))
                if len(intersection) != 0:
                    candidateList.append(dataDict[key])
            except:
                pass
        readableCandidateList = [candidate["name"] for candidate in candidateList]
        print(readableCandidateList)
    def updateData(self):
        url = "https://github.91chifun.workers.dev//https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json"
        newOTARunnable = OTARunnable(url)
        QThreadPool.globalInstance().start(newOTARunnable)
        # 这里可能会产生异步问题
        dataDict = util.loadDataDict()
        print(dataDict)

# class tagImageToTagTypeRunnable(QRunnable):
#     def __init__(self, image, tagIndex, GUIMainWin):
#         QRunnable.__init__(self)
#         self.image = image
#         self.tagIndex = tagIndex
#         self.GUIMainWin = GUIMainWin
#     def run(self):
#         ocr = CnOcr(root="./OCRmodels")
#         rawImage = self.image.convertToFormat(4)
#         w = rawImage.width()
#         h = rawImage.height()
#         ptr = rawImage.bits()
#         ptr.setsize(rawImage.byteCount())
#         preparedImage = np.array(ptr).reshape(h, w, 4) #此处完成转换
#         preparedImage = cv2.cvtColor(preparedImage, cv2.COLOR_BGRA2BGR)
#         tagType = "".join(ocr.ocr(preparedImage)[0])
#         self.GUIMainWin.tagTypeList[self.tagIndex] = tagType
#         if self.tagIndex == 0:
#             self.GUIMainWin.tagOneLabel.setText(tagType)
#         if self.tagIndex == 1:
#             self.GUIMainWin.tagTwoLabel.setText(tagType)
#         if self.tagIndex == 2:
#             self.GUIMainWin.tagThreeLabel.setText(tagType)
#         if self.tagIndex == 3:
#             self.GUIMainWin.tagFourLabel.setText(tagType)
#         if self.tagIndex == 4:
#             self.GUIMainWin.tagFiveLabel.setText(tagType)
        

if __name__ == '__main__':
    ### CLI测试部分
    config_dict = util.config_loadConfig()
    dataDict = util.loadDataDict()
    # refImageParams = util.config_getRefImageParams()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    loop = quamash.QEventLoop(app)
    asyncio.set_event_loop(loop)  # NEW must set the event loop

    with loop:
        mainWin = GUIMainWin()
        mainWin.show()
        loop.run_forever()
    