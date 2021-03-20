import logging
import copy
import os
import json
# Prepare Logging
global_logger = logging.getLogger()
hwnd_title = dict()

default_dict = {
    "tagImageParams":
        {
            "widthRatio": 0.1120, 
            "heightRatio": 0.067,
            "tagLocationRatio":
                [
                    {
                        'x': 0.2975,
                        'y': 0.50,
                    },
                    {
                        'x': 0.425,
                        'y': 0.50,
                    },
                    {
                        'x': 0.55625,
                        'y': 0.50,
                    },
                    {
                        'x': 0.2975,
                        'y': 0.60,
                    },
                    {
                        'x': 0.425,
                        'y': 0.60,
                    },
                ]
        }
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

def loadDataDict():
    dataDict = {}
    try:
        dataJSONFile = open(os.path.join(os.path.expanduser('~'), "ArknightsRecruitmentHelper", "characterData.json"),'r',encoding='utf-8')
        dataDict = json.load(dataJSONFile)
    except Exception as e:
        global_logger.warning("loadDataDict失败。%s" % e)
    finally:
        return dataDict
