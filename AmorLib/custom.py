# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/custom.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    xinghu2408@foxmail.com
@License   :    AGPLv3
@Copyright :    (C) 2026 AmorLib
@Desc      :    None
"""

import copy
import json
import os

import OlivaDiceCore  # type: ignore

try:
    import OlivaDiceNativeGUI  # type: ignore

    has_NativeGUI = True
except ImportError:
    has_NativeGUI = False


def releaseDir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def initCustom(Plugin, Proc, templateName="default"):
    releaseDir(Plugin.config.dataDirRoot)
    # 全局配置项模板载入
    if "unity" not in Plugin.custom.dictConsoleSwitchTemplate:
        Plugin.custom.dictConsoleSwitchTemplate["unity"] = {}
        Plugin.custom.dictConsoleSwitchTemplate["unity"] = copy.deepcopy(Plugin.custom.dictConsoleSwitchTemplate[templateName])
    bot_info_list = list(Proc.Proc_data["bot_info_dict"]) + ["unity"]
    for bot_hash in bot_info_list:
        releaseDir(Plugin.config.dataDirRoot + "/" + bot_hash)
        # 模板回复词载入
        Plugin.custom.dictStrCustom[bot_hash] = {}
        Plugin.custom.dictStrCustom[bot_hash] = copy.deepcopy(Plugin.custom.dictStrCustomTemplate[templateName])
        # 模板帮助文档载入
        Plugin.custom.dictHelpDoc[bot_hash] = {}
        Plugin.custom.dictHelpDoc[bot_hash] = copy.deepcopy(Plugin.custom.dictHelpDocTemplate[templateName])
        # 模板配置项载入
        Plugin.custom.dictConsoleSwitch[bot_hash] = {}
        Plugin.custom.dictConsoleSwitch[bot_hash] = copy.deepcopy(Plugin.custom.dictConsoleSwitchTemplate[templateName])
        # 自定义回复词载入
        customBotDir = Plugin.config.dataDirRoot + "/" + bot_hash
        customReplyFile = "customReply.json"
        customReplyPath = customBotDir + "/" + customReplyFile
        try:
            with open(customReplyPath, "r", encoding="utf-8") as customReplyPath_f:
                Plugin.custom.dictStrCustomUpdate[bot_hash] = json.loads(customReplyPath_f.read())
                Plugin.custom.dictStrCustom[bot_hash].update(Plugin.custom.dictStrCustomUpdate[bot_hash])
        except:
            pass
        # 本地help文档载入
        helpDocFile = "helpdoc.json"
        helpDocPath = customBotDir + "/" + helpDocFile
        try:
            with open(helpDocPath, "r", encoding="utf-8") as helpDocPath_f:
                helpDoc_this = json.loads(helpDocPath_f.read())
                Plugin.custom.dictHelpDoc[bot_hash].update(helpDoc_this)
        except:
            pass
        # 本地配置项载入
        switchFile = "switch.json"
        switchPath = customBotDir + "/" + switchFile
        try:
            with open(switchPath, "r", encoding="utf-8") as switchPath_f:
                switch_this = json.loads(switchPath_f.read())
                Plugin.custom.dictConsoleSwitch[bot_hash].update(switch_this)
        except:
            pass


def readCustom(Plugin, Proc):
    bot_info_dict = list(Proc.Proc_data["bot_info_dict"]) + ["unity"]
    for bot_hash in bot_info_dict:
        readCustomByBotHash(Plugin, bot_hash)


def readCustomByBotHash(Plugin, bot_hash):
    releaseDir(Plugin.config.dataDirRoot + "/" + bot_hash)
    customBotDir = Plugin.config.dataDirRoot + "/" + bot_hash
    # 自定义回复词载入
    customReplyFile = "customReply.json"
    customReplyPath = customBotDir + "/" + customReplyFile
    try:
        with open(customReplyPath, "r", encoding="utf-8") as customReplyPath_f:
            Plugin.custom.dictStrCustomUpdate[bot_hash].update(json.loads(customReplyPath_f.read()))
    except:
        pass
    # 本地help文档载入
    helpDocFile = "helpdoc.json"
    helpDocPath = customBotDir + "/" + helpDocFile
    try:
        with open(helpDocPath, "r", encoding="utf-8") as helpDocPath_f:
            helpDoc_this = json.loads(helpDocPath_f.read())
            Plugin.custom.dictHelpDoc[bot_hash].update(helpDoc_this)
    except:
        pass
    # 本地配置项载入
    switchFile = "switch.json"
    switchPath = customBotDir + "/" + switchFile
    try:
        with open(switchPath, "r", encoding="utf-8") as switchPath_f:
            switch_this = json.loads(switchPath_f.read())
            Plugin.custom.dictConsoleSwitch[bot_hash].update(switch_this)
    except:
        pass


def saveCustom(Plugin, Proc):
    bot_info_dict = list(Proc.Proc_data["bot_info_dict"]) + ["unity"]
    for bot_hash in bot_info_dict:
        saveCustomByBotHash(Plugin, bot_hash)


def saveCustomByBotHash(Plugin, bot_hash):
    releaseDir(Plugin.config.dataDirRoot + "/" + bot_hash)
    customBotDir = Plugin.config.dataDirRoot + "/" + bot_hash
    # 自定义回复词保存
    customReplyFile = "customReply.json"
    customReplyPath = customBotDir + "/" + customReplyFile
    if bot_hash not in Plugin.custom.dictStrCustomUpdate:
        Plugin.custom.dictStrCustomUpdate[bot_hash] = {}
    with open(customReplyPath, "w", encoding="utf-8") as customReplyPath_f:
        customReplyPath_f.write(
            json.dumps(
                Plugin.custom.dictStrCustomUpdate[bot_hash],
                ensure_ascii=False,
                indent=4,
            )
        )
    # 本地help文档保存
    helpDocFile = "helpdoc.json"
    helpDocPath = customBotDir + "/" + helpDocFile
    if bot_hash not in Plugin.custom.dictHelpDoc:
        Plugin.custom.dictHelpDoc[bot_hash] = {}
    with open(helpDocPath, "w", encoding="utf-8") as helpDocPath_f:
        helpDocPath_f.write(json.dumps(Plugin.custom.dictHelpDoc[bot_hash], ensure_ascii=False, indent=4))
    # 本地配置项保存
    switchFile = "switch.json"
    switchPath = customBotDir + "/" + switchFile
    if bot_hash not in Plugin.custom.dictConsoleSwitch:
        Plugin.custom.dictConsoleSwitch[bot_hash] = {}
    with open(switchPath, "w", encoding="utf-8") as switchPath_f:
        switchPath_f.write(json.dumps(Plugin.custom.dictConsoleSwitch[bot_hash], ensure_ascii=False, indent=4))


def loadCustomInto(Plugin, Proc):
    bot_info_dict = Proc.Proc_data["bot_info_dict"]
    for bot_hash in bot_info_dict:
        # 回复词
        if bot_hash not in OlivaDiceCore.msgCustom.dictStrCustomDict:
            OlivaDiceCore.msgCustom.dictStrCustomDict[bot_hash] = {}
        for key, value in Plugin.custom.dictStrCustom[bot_hash].items():
            if key not in OlivaDiceCore.msgCustom.dictStrCustomDict[bot_hash]:
                OlivaDiceCore.msgCustom.dictStrCustomDict[bot_hash][key] = value
        # 帮助文档
        for key, value in Plugin.custom.dictHelpDoc[bot_hash].items():
            if key not in OlivaDiceCore.helpDocData.dictHelpDoc[bot_hash]:
                OlivaDiceCore.helpDocData.dictHelpDoc[bot_hash][key] = value
        # 配置项
        for key, value in Plugin.custom.dictConsoleSwitch[bot_hash].items():
            if key not in OlivaDiceCore.console.dictConsoleSwitch[bot_hash]:
                OlivaDiceCore.console.dictConsoleSwitch[bot_hash][key] = value
    # 全局配置项和默认配置项
    for key, value in Plugin.custom.dictConsoleSwitch["unity"].items():
        if key not in OlivaDiceCore.console.dictConsoleSwitch["unity"]:
            OlivaDiceCore.console.dictConsoleSwitch["unity"][key] = value
    for key, value in Plugin.custom.dictConsoleSwitchTemplate["default"].items():
        if key not in OlivaDiceCore.console.dictConsoleSwitchTemplate["default"]:
            OlivaDiceCore.console.dictConsoleSwitchTemplate["default"][key] = value
    if has_NativeGUI:
        # 回复词说明
        for key, value in Plugin.custom.dictStrCustomNote.items():
            if key not in OlivaDiceNativeGUI.msgCustom.dictStrCustomNote:
                OlivaDiceNativeGUI.msgCustom.dictStrCustomNote[key] = value
        # 配置项说明
        for key, value in Plugin.custom.dictConsoleSwitchNote.items():
            if key not in OlivaDiceNativeGUI.msgCustom.dictConsoleSwitchNote:
                OlivaDiceNativeGUI.msgCustom.dictConsoleSwitchNote[key] = value
    OlivaDiceCore.msgCustom.dictStrConst.update(Plugin.custom.dictStrConst)
    OlivaDiceCore.msgCustom.dictGValue.update(Plugin.custom.dictGValue)
    OlivaDiceCore.msgCustom.dictTValue.update(Plugin.custom.dictTValue)
