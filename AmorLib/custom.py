# -*- encoding: utf-8 -*-
"""
@File      :    AmorLib/custom.py
@Author    :    lianqingyuYuri恋倾雨
@Contact   :    xinghu2408@foxmail.com
@License   :    AGPLv3
@Copyright :    (C) 2026 AmorLib
@Desc      :    None
"""

import OlivOS  # type: ignore
import OlivaDiceCore  # type: ignore

import copy
import os
import json

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
        Plugin.custom.dictConsoleSwitchTemplate["unity"] = copy.deepcopy(
            Plugin.custom.dictConsoleSwitchTemplate[templateName]
        )
    bot_info_dict = list(Proc.Proc_data["bot_info_dict"]) + ["unity"]
    for bot_hash in bot_info_dict:
        releaseDir(Plugin.config.dataDirRoot + "/" + bot_hash)
        # 模板回复词载入
        Plugin.custom.dictStrCustom[bot_hash] = {}
        Plugin.custom.dictStrCustom[bot_hash] = copy.deepcopy(
            Plugin.custom.dictStrCustomTemplate[templateName]
        )
        # 模板帮助文档载入
        Plugin.custom.dictHelpDoc[bot_hash] = {}
        Plugin.custom.dictHelpDoc[bot_hash] = copy.deepcopy(
            Plugin.custom.dictHelpDocTemplate[templateName]
        )
        # 模板配置项载入
        Plugin.custom.dictConsoleSwitch[bot_hash] = {}
        Plugin.custom.dictConsoleSwitch[bot_hash] = copy.deepcopy(
            Plugin.custom.dictConsoleSwitchTemplate[templateName]
        )
        # 自定义回复词载入
        customBotDir = Plugin.config.dataDirRoot + "/" + bot_hash
        customReplyFile = "customReply.json"
        customReplyPath = customBotDir + "/" + customReplyFile
        try:
            with open(customReplyPath, "r", encoding="utf-8") as customReplyPath_f:
                Plugin.custom.dictStrCustomUpdate[bot_hash] = json.loads(
                    customReplyPath_f.read()
                )
                Plugin.custom.dictStrCustom[bot_hash].update(
                    Plugin.custom.dictStrCustomUpdate[bot_hash]
                )
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
            Plugin.custom.dictStrCustomUpdate[bot_hash].update(
                json.loads(customReplyPath_f.read())
            )
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
        helpDocPath_f.write(
            json.dumps(
                Plugin.custom.dictHelpDoc[bot_hash], ensure_ascii=False, indent=4
            )
        )
    # 本地配置项保存
    switchFile = "switch.json"
    switchPath = customBotDir + "/" + switchFile
    if bot_hash not in Plugin.custom.dictConsoleSwitch:
        Plugin.custom.dictConsoleSwitch[bot_hash] = {}
    with open(switchPath, "w", encoding="utf-8") as switchPath_f:
        switchPath_f.write(
            json.dumps(
                Plugin.custom.dictConsoleSwitch[bot_hash], ensure_ascii=False, indent=4
            )
        )


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


class MsgManager:
    def __init__(self, plugin_event):
        force_reply = False  # 是否强制回复
        # region 基本参数
        self.val = {}
        self.flags = {  # 存储各类状态标识
            "is_command": False,  # 是否为命令消息
            "is_host": False,  # 是否来自主机账号
            "is_master": False,  # 是否来自机器人主人
            "is_group": False,  # 是否来自群聊
            "is_group_admin": False,  # 是否来自群管理员
            "is_group_sub_admin": False,  # 是否来自群副管理员
            "is_group_have_admin": False,  # 是否拥有群管理权限
        }
        self.msg = plugin_event.data.message  # 消息
        self.sender = plugin_event.data.sender  # 发送者信息
        self.bot_hash = plugin_event.bot_info.hash  # 机器人哈希
        self.bot_id = str(plugin_event.base_info["self_id"])  # 机器人ID
        self.bot_id_sub = None  # 子账号ID（如果存在）
        if (
            "sub_self_id" in (extend := plugin_event.data.extend)
            and extend["sub_self_id"] is not None
        ):
            self.bot_id_sub = str(extend["sub_self_id"])
        self.at_list = []  # 被艾特的用户ID列表
        self.user_id = plugin_event.data.user_id  # 发送者ID
        self.platform = plugin_event.platform["platform"]  # 平台
        self.group_id = None  # 群号ID
        # endregion 基本参数
        # region 初始化模板变量
        dictTValue = OlivaDiceCore.msgCustom.dictTValue.copy()
        if "name" in plugin_event.data.sender:
            dictTValue["tUserName"] = plugin_event.data.sender["name"]
            dictTValue["tName"] = plugin_event.data.sender["name"]
        dictTValue.update(OlivaDiceCore.msgCustom.dictGValue)
        dictTValue = OlivaDiceCore.msgCustomManager.dictTValueInit(
            plugin_event, dictTValue
        )
        self.dictTValue = dictTValue  # 模板变量
        self.dictStrCustomDict = OlivaDiceCore.msgCustom.dictStrCustomDict[
            self.bot_hash
        ]  # 自定义回复
        # endregion 初始化模板变量
        # region 处理回复
        """处理强制回复标识（@机器人触发）"""
        msg_templet = OlivOS.messageAPI.Message_templet("old_string", self.msg)
        if not msg_templet.data:
            msg_para = msg_templet.data[0]
            if msg_para.type == "at":
                at_id = msg_para.data["id"]
                if at_id in (self.bot_id, self.bot_id_sub):
                    force_reply = True
        """处理at和空文本"""
        for msg_para in msg_templet.data:
            msg_para_cq = msg_para.CQ()
            if msg_para.type == "at":
                self.at_list.append(msg_para_cq)
                self.msg = self.msg.lstrip(msg_para_cq)
            elif msg_para.type == "text" and msg_para_cq.strip(" ") == "":
                self.msg = self.msg.lstrip(msg_para_cq)
            else:
                break
        """检查消息是否为命令"""
        self.msg, self.flags["is_command"] = OlivaDiceCore.msgReply.msgIsCommand(
            self.msg, OlivaDiceCore.crossHook.dictHookList["prefix"]
        )
        # endregion 处理回复
        # region 初始化用户身份相关标识
        self.flags["is_master"] = OlivaDiceCore.ordinaryInviteManager.isInMasterList(
            plugin_event.bot_info.hash,
            OlivaDiceCore.userConfig.getUserHash(
                self.user_id, "user", plugin_event.platform["platform"]
            ),
        )
        """判断消息类型（群/私聊）"""
        func_type = plugin_event.plugin_info["func_type"]
        if func_type == "group_message":
            self.group_id = plugin_event.data.group_id
            self.flags["is_host"] = plugin_event.data.host_id is not None
            self.flags["is_group"] = True
            # 检查群管理员身份
            if "role" in plugin_event.data.sender:
                self.flags["is_group_have_admin"] = True
                role = plugin_event.data.sender["role"]
                if role in ("owner", "admin"):
                    self.flags["is_group_admin"] = True
                elif role == "sub_admin":
                    self.flags["is_group_admin"] = True
                    self.flags["is_group_sub_admin"] = True
        elif func_type == "private_message":
            self.flags["is_group"] = False
        # endregion 初始化用户身份相关标识
        # region 检查权限配置
        if self.flags["is_host"] and self.flags["is_group"]:
            hag_id = (
                f"{str(plugin_event.data.host_id)}|{str(plugin_event.data.group_id)}"
            )
        elif self.flags["is_group"]:
            hag_id = str(plugin_event.data.group_id)
        flags_host_enable = True
        flags_host_local_enable = True
        flags_group_enable = True
        if self.flags["is_host"]:
            """获取频道启用状态"""
            flags_host_enable = OlivaDiceCore.userConfig.getUserConfigByKey(
                userId=plugin_event.data.host_id,
                userType="host",
                platform=self.platform,
                userConfigKey="hostEnable",
                botHash=self.bot_hash,
            )
            """获取频道本地启用状态"""
            flags_host_local_enable = OlivaDiceCore.userConfig.getUserConfigByKey(
                userId=plugin_event.data.host_id,
                userType="host",
                platform=self.platform,
                userConfigKey="hostLocalEnable",
                botHash=self.bot_hash,
            )
        """获取群启用状态"""
        if self.flags["is_group"]:
            if self.flags["is_host"]:
                if flags_host_enable:
                    flags_group_enable = OlivaDiceCore.userConfig.getUserConfigByKey(
                        userId=hag_id,
                        userType="group",
                        platform=plugin_event.platform["platform"],
                        userConfigKey="groupEnable",
                        botHash=plugin_event.bot_info.hash,
                    )
                else:
                    flags_group_enable = OlivaDiceCore.userConfig.getUserConfigByKey(
                        userId=hag_id,
                        userType="group",
                        platform=plugin_event.platform["platform"],
                        userConfigKey="groupWithHostEnable",
                        botHash=plugin_event.bot_info.hash,
                    )
            else:
                flags_group_enable = OlivaDiceCore.userConfig.getUserConfigByKey(
                    userId=hag_id,
                    userType="group",
                    platform=plugin_event.platform["platform"],
                    userConfigKey="groupEnable",
                    botHash=plugin_event.bot_info.hash,
                )
        """判断是否回复"""
        if not flags_host_local_enable and not force_reply:
            self.allow_reply = False
        elif not flags_group_enable and not force_reply:
            self.allow_reply = False
        else:
            self.allow_reply = True

    # endregion

    def msg_format(
        self,
        custom: str,
        t_value: dict = {},
        flagCross: bool = True,
        flagSplit: bool = False,
    ) -> str:
        """格式化"""
        if custom in self.dictStrCustomDict:
            dictTValue = self.dictTValue
            dictTValue.update(t_value)
            return OlivaDiceCore.msgCustomManager.formatReplySTR(
                self.dictStrCustomDict[custom], dictTValue, flagCross, flagSplit
            )
        return custom
