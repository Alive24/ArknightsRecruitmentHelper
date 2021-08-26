import logging
import copy
import os
import json
import requests
from itertools import combinations
# Prepare Logging
global_logger = logging.getLogger()
hwnd_title = dict()

default_dict = {
    "tagImageParams":
        {
            "widthRatio": 0.1120, 
            "heightRatio": 0.035,
            "tagLocationRatio":
                [
                    {
                        'x': 0.2975,
                        'y': 0.515,
                    },
                    {
                        'x': 0.425,
                        'y': 0.515,
                    },
                    {
                        'x': 0.55625,
                        'y': 0.515,
                    },
                    {
                        'x': 0.2975,
                        'y': 0.615,
                    },
                    {
                        'x': 0.425,
                        'y': 0.615,
                    },
                ]
        }
}

# 应当寻找更稳定的自动计算的方式
defaultExcludedOperatorList = [
    '豆苗', '月禾', '蜜蜡', '波登可', '松果', '断崖', '石棉', '闪击', '梅', '安比尔', '安哲拉', '慑砂',
    '巫恋', '孑', '卡夫卡', '槐琥', '乌有', '空', '霜华'
]

defaultStrategyListDict = {
    'singleTagStrategyList': [], 
    'doubleTagStrategyList': []
}

def config_loadConfig():
    try:
        config_file = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "config.json"),'r',encoding='utf-8')
        config_dict_toLoad = json.load(config_file)
        config_dict = copy.deepcopy(default_dict)
        for key in list(config_dict_toLoad.keys()):
            config_dict[key] = config_dict_toLoad[key]
        config_file.close()
    except Exception as e:
        global_logger.exception("config_loadConfig()错误")
        config_dict = copy.deepcopy(default_dict)
        config_file = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "config.json"),'w',encoding='utf-8')
        json.dump(config_dict,config_file,ensure_ascii=False)
        config_file.close()
    return config_dict

def config_loadExcludedOperatorList():
    try:
        excludedOperatorListFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "excludedOperatorList.json"),'r',encoding='utf-8')
        excludedOperatorListtoLoad = json.load(excludedOperatorListFile)
        excludedOperatorList = copy.deepcopy(defaultExcludedOperatorList)
        for excludedOperator in excludedOperatorListtoLoad:
            excludedOperatorList.append(excludedOperator)
        excludedOperatorList = list(set(excludedOperatorList))
        excludedOperatorListFile.close()
    except Exception as e:
        global_logger.exception("config_loadExcludedOperatorList()错误")
        excludedOperatorList = copy.deepcopy(defaultExcludedOperatorList)
        excludedOperatorListFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "excludedOperatorList.json"),'r',encoding='utf-8')
        json.dump(excludedOperatorList,excludedOperatorListFile,ensure_ascii=False)
        excludedOperatorListFile.close()
    return excludedOperatorList

def config_loadStrategyListDict():
    try:
        strategyListDictFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "strategyListDict.json"),'r',encoding='utf-8')
        strategyListDicttoLoad = json.load(strategyListDictFile)
        strategyListDict = copy.deepcopy(defaultStrategyListDict)
        for key in list(strategyListDicttoLoad.keys()):
            strategyListDict[key] = strategyListDicttoLoad[key]
        strategyListDictFile.close()
    except Exception as e:
        global_logger.exception("config_loadStrategyListDict()错误")
        strategyListDict = copy.deepcopy(defaultStrategyListDict)
        strategyListDictFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "strategyListDict.json"),'w',encoding='utf-8')
        json.dump(strategyListDict,strategyListDictFile,ensure_ascii=False)
        strategyListDictFile.close()
    return strategyListDict


def loadDataDict():
    dataDict = {}
    try:
        dataJSONFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "characterData.json"),'r',encoding='utf-8')
        dataDict = json.load(dataJSONFile)
    except Exception as e:
        global_logger.warning("loadDataDict失败。%s" % e)
    finally:
        return dataDict

def generateStrategyListDict():
    gachaTableContent = requests.get("https://github.91chifun.workers.dev//https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/gacha_table.json").content
    gachaTagList = json.loads(gachaTableContent.decode())['gachaTags']
    tagList = [tag['tagName'] for tag in gachaTagList]
    combinationListOfTwo = list(combinations(tagList, 2))
    dataJSONFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "characterData.json"),'r',encoding='utf-8')
    dataDict = json.load(dataJSONFile)
    professionMapperDict = {
        "PIONEER" : "先锋干员",
        "TANK": "重装干员",
        "WARRIOR": "近卫干员",
        "SNIPER": "狙击干员",
        "CASTER": "术师干员",
        "SPECIAL": "特种干员",
        "MEDIC": "医疗干员",
        "SUPPORT": "辅助干员"
    }
    def dataDictEntryTrimmer(dataDictEntry):
        excludedOperatorList = config_loadExcludedOperatorList()
        flag = True
        if not dataDictEntry['itemObtainApproach'] in ['招募寻访', "限时礼包"]:
            flag = False
        if dataDictEntry['rarity'] < 2:
            flag = False
        if dataDictEntry['rarity'] == 5:
            flag = False
        if dataDictEntry['name'] in excludedOperatorList:
            flag = False
        return flag
    dataDictKeyList = list(dataDict.keys())
    trimmedDictKeyList = list(filter(lambda dataDictEntryKey: dataDictEntryTrimmer(dataDict[dataDictEntryKey]), dataDictKeyList))
    trimmedDataDict = {validKey: dataDict[validKey] for validKey in trimmedDictKeyList}
    dataDict = copy.deepcopy(trimmedDataDict)
    candidateSingleTagStrategyList = []
    candidateCombinationListOfTwoStrategyList = []
    for i in range(len(tagList)):
        plausibleList = []
        for key in list(dataDict.keys()):
            processedTagList = copy.deepcopy(dataDict[key]["tagList"])
            if dataDict[key]['position'] == "RANGED":
                processedTagList.append("远程位")
            else:
                processedTagList.append("近战位")
            processedTagList.append(professionMapperDict[dataDict[key]['profession']])
            tagListSet = set(processedTagList)
            plausible = tagList[i] in tagListSet
            if plausible:
                plausibleList.append({'name':dataDict[key]['name'], 'rarity': dataDict[key]['rarity']})
        if len(plausibleList) != 0:
            plausibleThreeList = copy.deepcopy(plausibleList)
            plausibleThreeList = list(filter(lambda operator: operator['rarity']< 3, plausibleThreeList))
            if len(plausibleThreeList) == 0:
                candidateSingleTagStrategyList.append({'tag': tagList[i], 'plausibleList': plausibleList})
    for i in range(len(combinationListOfTwo)):
        plausibleList = []
        for key in list(dataDict.keys()):
            try:
                processedTagList = copy.deepcopy(dataDict[key]["tagList"])
                if dataDict[key]['position'] == "RANGED":
                    processedTagList.append("远程位")
                else:
                    processedTagList.append("近战位")
                processedTagList.append(professionMapperDict[dataDict[key]['profession']])
                tagListSet = set(processedTagList)
                combinationSet = set(combinationListOfTwo[i])
                plausible = combinationSet.issubset(tagListSet)
                if plausible:
                    plausibleList.append({'name':dataDict[key]['name'], 'rarity': dataDict[key]['rarity']})
            except Exception as e:
                print(e)
        if len(plausibleList) != 0:
            plausibleThreeList = copy.deepcopy(plausibleList)
            plausibleThreeList = list(filter(lambda operator: operator['rarity']< 3, plausibleThreeList))
            if len(plausibleThreeList) == 0:
                candidateCombinationListOfTwoStrategyList.append({'tagCombination': combinationListOfTwo[i], 'plausibleList': plausibleList})
    print("singleTag", candidateSingleTagStrategyList)
    print("combinationOfTwo", candidateCombinationListOfTwoStrategyList)
    trimmedcandidateCombinationListOfTwoStrategy = []
    for strategy in candidateCombinationListOfTwoStrategyList:
        flag = True
        for singleTag in [strategy['tag'] for strategy in candidateSingleTagStrategyList]:
            if singleTag in strategy['tagCombination']:
                flag = False
        if flag:
            trimmedcandidateCombinationListOfTwoStrategy.append(strategy)
    strategyListDict = {'singleTagStrategyList': candidateSingleTagStrategyList, 'doubleTagStrategyList': trimmedcandidateCombinationListOfTwoStrategy}
    return strategyListDict

    

def devMain():
    generateStrategyListDict()
    
if __name__ == "__main__":
    # 直接执行则为开发模式入口
        devMain()
