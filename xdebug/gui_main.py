# -*- coding:utf-8 -*- 
# Author: bobby

import wx
import re
from xdebug.opcode_parse import *
from xdebug.opcode_handler import *
from xdebug.variable import *
from xdebug.model.index import *


class MyFrame(wx.Frame):
    panel = None
    listBox = None
    text_stack = None
    text_memory = None
    text_storage = None
    indexDict = {}
    handlerObj = None
    flag = False

    def __init__(self, **kwargs):
        super().__init__(parent=None, title="solidity assembly debug V0.1 by bobby", size=(1400, 750))
        # self.SetMaxSize((1400, 750))
        # self.SetMinSize((1400, 750))
        self.Center()  # 设置窗口居中
        self.panel = wx.Panel(parent=self)
        self.list_len = len(kwargs.get("list"))
        # 添加控件
        self.listBox = wx.ListBox(self.panel, -1, pos=(20, 20), size=(700, 200), choices=kwargs.get("list"), style=wx.LB_SINGLE)
        self.listBox.SetSelection(0)

        next_button = wx.Button(self.panel, label="下一步", pos=(40, 230), size=(55, 30))
        last_button = wx.Button(self.panel, label="上一步", pos=(100, 230), size=(55, 30))
        wx.StaticText(self.panel, pos=(730, 0), size=(650, 25)).SetLabelText("Stack")
        self.text_stack = wx.TextCtrl(self.panel, pos=(730, 20), size=(650, 200))
        wx.StaticText(self.panel, pos=(730, 230), size=(650, 25)).SetLabelText("Memory")
        self.text_memory = wx.TextCtrl(self.panel, pos=(730, 250), size=(650, 200))
        wx.StaticText(self.panel, pos=(730, 460), size=(650, 25)).SetLabelText("Storage")
        self.text_storage = wx.TextCtrl(self.panel, pos=(730, 480), size=(650, 200))
        # 添加事件处理
        self.Bind(wx.EVT_LISTBOX, self.on_listbox, self.listBox)
        self.Bind(wx.EVT_BUTTON, self.on_nextbutton, next_button)
        self.Bind(wx.EVT_BUTTON, self.on_lastbutton, last_button)

        # 初始化HandlerOpCode
        self.init()


    # 事件处理函数
    def on_listbox(self, event):
        listbox = event.GetEventObject()
        listbox.SetScrollbar(wx.VERTICAL, 0, 1, 50, refresh=True)
        print("选择{0}".format(listbox.GetStringSelection()))

    def on_nextbutton(self, event):
        self.need_input()
        if self.listBox.GetSelection() == 0:
            self.indexDict[0] = Index(0, 0, [], {}, {})
            self.run(0)
            self.indexDict[dict_index["index_dict"]] = Index(dict_index["index_dict"], dict_index["unit"], dt["stack"],
                                                             dt["memory"], dt["storage"])
            # print(self.indexDict[dict_index["index_dict"]].stack)
            self.handlerObj.clear()
            # print(dict_index["index_dict"])
            self.write(self.indexDict[dict_index["index_dict"]].stack, self.indexDict[dict_index["index_dict"]].memory,
                       self.indexDict[dict_index["index_dict"]].storage)
            self.listBox.SetSelection(dict_index["index_dict"])
            # print("stack=", dt["stack"])
        else:
            dt["stack"] = self.indexDict[dict_index["index_dict"]].stack.copy()
            # print("stack=", dt["stack"])
            dt["memory"] = self.indexDict[dict_index["index_dict"]].memory.copy()
            dt["storage"] = self.indexDict[dict_index["index_dict"]].storage.copy()
            self.run(dict_index["index_dict"])
            self.indexDict[dict_index["index_dict"]] = Index(dict_index["index_dict"], dict_index["unit"], dt["stack"],
                                                             dt["memory"], dt["storage"])
            self.handlerObj.clear()
            self.write(self.indexDict[dict_index["index_dict"]].stack, self.indexDict[dict_index["index_dict"]].memory,
                       self.indexDict[dict_index["index_dict"]].storage)
            self.listBox.SetSelection(dict_index["index_dict"])
            self.listBox.EnsureVisible(dict_index["index_dict"])

    def on_lastbutton(self, event):
        if self.listBox.GetSelection() == 0:
            print("[***]***ERROR***: now the selection is the top")
        else:
            index = self.indexDict[dict_index["index_dict"]]
            self.listBox.SetSelection(dict_index["index_dict"]-index.unit)
            self.listBox.EnsureVisible(dict_index["index_dict"]-index.unit)
            dict_index["index_dict"] = index.index - index.unit
            self.write(self.indexDict[dict_index["index_dict"]].stack, self.indexDict[dict_index["index_dict"]].memory,
                       self.indexDict[dict_index["index_dict"]].storage)

    def need_input(self):
        special = ["CALLDATASIZE", "CALLDATALOAD"]
        _, opcode, _ = parse_string_2_pc_opcode(dict_assembly.get(self.listBox.GetSelection()))
        print(opcode)
        if find(special, opcode):
            title = ""
            if self.flag is False:
                title = TEXT_DIALOG
            elif self.flag is True:
                title = TEXT_DIALOG_ERROR
            dialog = wx.TextEntryDialog(self.panel, title, "Text Entry", "Default Value", style=wx.OK | wx.CANCEL)
            dialog.Center()
            if dialog.ShowModal() == wx.ID_OK:
                print("You entered: %s" % dialog.GetValue())
                if opcode == "CALLDATASIZE":
                    if re.match("^[0-9]*$", dialog.GetValue()) is None:
                        self.flag = True
                        self.need_input()
                elif opcode == "CALLDATALOAD":
                    if re.match("^[A-Fa-f0-9]+$", dialog.GetValue()) is None:
                        self.flag = True
                        self.need_input()
                self.handlerObj.value = dialog.GetValue()
                self.flag = False
                dialog.Destroy()

    def init(self):
        key = 0
        for y in pc_dec2hex(get_assembly(fileEvm, get_bytecode(fileSolc))):
            dict_assembly[key] = y
            key = key + 1
        self.handlerObj = HandlerOpCode()

    def run(self, index):
        assembly = dict_assembly[index]
        pc, opcode, value = parse_string_2_pc_opcode(assembly)
        self.handlerObj.handler_opcode(opcode.lower(), value)

    def write(self, arg0, arg1, arg2):
        i = 0
        text = ""
        # 写入stack的数据
        for x in arg0:
            key = str(i)
            i += 1
            key = input2hexstring(key, 6)
            key = key[2:]
            value = input2hexstring(x, 64)
            text = key + ":" + value + "\n"+text
        self.text_stack.Clear()
        self.text_stack.write(text)
        # 写入memory的数据
        text1 = ""
        for y in arg1:
            value = arg1[y]
            text1 = text1 + y + ":" + value + "\n"
        self.text_memory.Clear()
        self.text_memory.write(text1)
        # 写入storage的数据
        text2 = ""
        for z in arg2:
            value = arg2[z]
            text2 = text2 + z + ":" + value + "\n"
        self.text_storage.Clear()
        self.text_storage.write(text2)


# 自定以一个应用程序类
class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        print("应用程序启动")
        frame = MyFrame(list=pc_dec2hex(get_assembly(fileEvm, get_bytecode(fileSolc))))
        frame.Show()
        return True

    def OnExit(self):
        print("应用程序退出")
        return 0


if __name__ == '__main__':
    app = App()  # 创建自定以对象App
    app.MainLoop()  # 进入事件主循环


