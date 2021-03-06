# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ArknightsRecruimentHelperGUI(object):
    def setupUi(self, ArknightsRecruimentHelperGUI):
        ArknightsRecruimentHelperGUI.setObjectName("ArknightsRecruimentHelperGUI")
        ArknightsRecruimentHelperGUI.resize(803, 372)
        self.instructionLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.instructionLabel.setGeometry(QtCore.QRect(20, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.instructionLabel.setFont(font)
        self.instructionLabel.setObjectName("instructionLabel")
        self.tagOneLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.tagOneLabel.setGeometry(QtCore.QRect(160, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tagOneLabel.setFont(font)
        self.tagOneLabel.setObjectName("tagOneLabel")
        self.tagTwoLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.tagTwoLabel.setGeometry(QtCore.QRect(160, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tagTwoLabel.setFont(font)
        self.tagTwoLabel.setObjectName("tagTwoLabel")
        self.tagThreeLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.tagThreeLabel.setGeometry(QtCore.QRect(160, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tagThreeLabel.setFont(font)
        self.tagThreeLabel.setObjectName("tagThreeLabel")
        self.tagFourLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.tagFourLabel.setGeometry(QtCore.QRect(160, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tagFourLabel.setFont(font)
        self.tagFourLabel.setObjectName("tagFourLabel")
        self.tagFiveLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.tagFiveLabel.setGeometry(QtCore.QRect(160, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tagFiveLabel.setFont(font)
        self.tagFiveLabel.setObjectName("tagFiveLabel")
        self.handleSelectorComboBox = QtWidgets.QComboBox(ArknightsRecruimentHelperGUI)
        self.handleSelectorComboBox.setGeometry(QtCore.QRect(60, 340, 201, 22))
        self.handleSelectorComboBox.setObjectName("handleSelectorComboBox")
        self.handleSelector = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.handleSelector.setGeometry(QtCore.QRect(10, 340, 51, 21))
        self.handleSelector.setObjectName("handleSelector")
        self.queryStatusTag = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.queryStatusTag.setGeometry(QtCore.QRect(210, 300, 111, 31))
        self.queryStatusTag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.queryStatusTag.setObjectName("queryStatusTag")
        self.updateHandleSelectorListButton = QtWidgets.QPushButton(ArknightsRecruimentHelperGUI)
        self.updateHandleSelectorListButton.setGeometry(QtCore.QRect(270, 340, 51, 23))
        self.updateHandleSelectorListButton.setObjectName("updateHandleSelectorListButton")
        self.tagImageOneGraphicsView = QtWidgets.QGraphicsView(ArknightsRecruimentHelperGUI)
        self.tagImageOneGraphicsView.setGeometry(QtCore.QRect(40, 60, 100, 32))
        self.tagImageOneGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageOneGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageOneGraphicsView.setObjectName("tagImageOneGraphicsView")
        self.tagImageTwoGraphicsView = QtWidgets.QGraphicsView(ArknightsRecruimentHelperGUI)
        self.tagImageTwoGraphicsView.setGeometry(QtCore.QRect(40, 100, 100, 32))
        self.tagImageTwoGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageTwoGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageTwoGraphicsView.setObjectName("tagImageTwoGraphicsView")
        self.tagImageThreeGraphicsView = QtWidgets.QGraphicsView(ArknightsRecruimentHelperGUI)
        self.tagImageThreeGraphicsView.setGeometry(QtCore.QRect(40, 140, 100, 32))
        self.tagImageThreeGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageThreeGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageThreeGraphicsView.setObjectName("tagImageThreeGraphicsView")
        self.tagImageFourGraphicsView = QtWidgets.QGraphicsView(ArknightsRecruimentHelperGUI)
        self.tagImageFourGraphicsView.setGeometry(QtCore.QRect(40, 180, 100, 32))
        self.tagImageFourGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageFourGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageFourGraphicsView.setObjectName("tagImageFourGraphicsView")
        self.tagImageFiveGraphicsView = QtWidgets.QGraphicsView(ArknightsRecruimentHelperGUI)
        self.tagImageFiveGraphicsView.setGeometry(QtCore.QRect(40, 220, 100, 32))
        self.tagImageFiveGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageFiveGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tagImageFiveGraphicsView.setObjectName("tagImageFiveGraphicsView")
        self.manualRecognizeAndAnalyzeButton = QtWidgets.QPushButton(ArknightsRecruimentHelperGUI)
        self.manualRecognizeAndAnalyzeButton.setGeometry(QtCore.QRect(230, 10, 91, 31))
        self.manualRecognizeAndAnalyzeButton.setObjectName("manualRecognizeAndAnalyzeButton")
        self.updateDataButton = QtWidgets.QPushButton(ArknightsRecruimentHelperGUI)
        self.updateDataButton.setGeometry(QtCore.QRect(60, 300, 61, 31))
        self.updateDataButton.setObjectName("updateDataButton")
        self.singleTagStrategyListLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.singleTagStrategyListLabel.setGeometry(QtCore.QRect(390, 10, 54, 12))
        self.singleTagStrategyListLabel.setObjectName("singleTagStrategyListLabel")
        self.doubleTagStrategyListLabel = QtWidgets.QLabel(ArknightsRecruimentHelperGUI)
        self.doubleTagStrategyListLabel.setGeometry(QtCore.QRect(600, 10, 54, 12))
        self.doubleTagStrategyListLabel.setObjectName("doubleTagStrategyListLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(ArknightsRecruimentHelperGUI)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(380, 30, 201, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.singleTagStrategyListLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.singleTagStrategyListLayout.setContentsMargins(0, 0, 0, 0)
        self.singleTagStrategyListLayout.setObjectName("singleTagStrategyListLayout")
        self.singleTagStrategyListTempPlainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.singleTagStrategyListTempPlainTextEdit.setObjectName("singleTagStrategyListTempPlainTextEdit")
        self.singleTagStrategyListLayout.addWidget(self.singleTagStrategyListTempPlainTextEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ArknightsRecruimentHelperGUI)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 30, 201, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.doubleTagStrategyListLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.doubleTagStrategyListLayout.setContentsMargins(0, 0, 0, 0)
        self.doubleTagStrategyListLayout.setObjectName("doubleTagStrategyListLayout")
        self.doubleTagStrategyListTempPlainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.doubleTagStrategyListTempPlainTextEdit.setObjectName("doubleTagStrategyListTempPlainTextEdit")
        self.doubleTagStrategyListLayout.addWidget(self.doubleTagStrategyListTempPlainTextEdit)

        self.retranslateUi(ArknightsRecruimentHelperGUI)
        QtCore.QMetaObject.connectSlotsByName(ArknightsRecruimentHelperGUI)

    def retranslateUi(self, ArknightsRecruimentHelperGUI):
        _translate = QtCore.QCoreApplication.translate
        ArknightsRecruimentHelperGUI.setWindowTitle(_translate("ArknightsRecruimentHelperGUI", "ArknightsRecruimentHelperGUI"))
        self.instructionLabel.setText(_translate("ArknightsRecruimentHelperGUI", "<html><head/><body><p><span style=\" font-size:20pt;\">操作指示</span></p></body></html>"))
        self.tagOneLabel.setText(_translate("ArknightsRecruimentHelperGUI", "<html><head/><body><p>重装干员</p></body></html>"))
        self.tagTwoLabel.setText(_translate("ArknightsRecruimentHelperGUI", "<html><head/><body><p>近卫干员</p></body></html>"))
        self.tagThreeLabel.setText(_translate("ArknightsRecruimentHelperGUI", "<html><head/><body><p>高级资深干员</p></body></html>"))
        self.tagFourLabel.setText(_translate("ArknightsRecruimentHelperGUI", "<html><head/><body><p>控场</p></body></html>"))
        self.tagFiveLabel.setText(_translate("ArknightsRecruimentHelperGUI", "<html><head/><body><p>新手</p></body></html>"))
        self.handleSelector.setText(_translate("ArknightsRecruimentHelperGUI", "游戏句柄"))
        self.queryStatusTag.setText(_translate("ArknightsRecruimentHelperGUI", "TextLabel"))
        self.updateHandleSelectorListButton.setText(_translate("ArknightsRecruimentHelperGUI", "刷新"))
        self.manualRecognizeAndAnalyzeButton.setText(_translate("ArknightsRecruimentHelperGUI", "手动识别分析"))
        self.updateDataButton.setText(_translate("ArknightsRecruimentHelperGUI", "更新数据"))
        self.singleTagStrategyListLabel.setText(_translate("ArknightsRecruimentHelperGUI", "单Tag可锁"))
        self.doubleTagStrategyListLabel.setText(_translate("ArknightsRecruimentHelperGUI", "双Tag可锁"))
