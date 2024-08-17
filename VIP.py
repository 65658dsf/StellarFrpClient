#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import VIP_cmd
import VIP_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  VIP:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=VIP_cmd
        Fun.Register(uiName,'root',root)
        style = VIP_sty.SetupStyle(isTKroot)
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,1144,215)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#F0F0F0'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1144)
        Form_1.configure(height = 215)
        Form_1.configure(bg = "#F0F0F0")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetCanvasBGImage(uiName,'Form_1',"Resources/Tunnel_Card.png",'Zoom')
        Fun.SetUIRootSize(uiName,1144,215)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="付费隧道")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'title')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.02097902097902098,0.11162790697674418,0.7674825174825175,0.22325581395348837,'nw',True,True)
        Label_2.configure(bg = "#F0F0F0")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(anchor = "w")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=24,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="隧道协议")
        Fun.Register(uiName,'PyMe_Label_3',Label_3,'type_name')
        Fun.SetControlPlace(uiName,'PyMe_Label_3',0.02097902097902098,0.35348837209302325,0.26223776223776224,0.09302325581395349,'nw',True,True)
        Label_3.configure(bg = "#F0F0F0")
        Label_3.configure(fg = "SystemButtonText")
        Label_3.configure(anchor = "w")
        Label_3_Ft=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)
        Label_4 = tkinter.Label(Form_1,text="TCP-UDP")
        Fun.Register(uiName,'PyMe_Label_4',Label_4,'type')
        Fun.SetControlPlace(uiName,'PyMe_Label_4',0.2867132867132867,0.35348837209302325,0.11276223776223776,0.09302325581395349,'nw',True,True)
        Label_4.configure(bg = "#F0F0F0")
        Label_4.configure(fg = "SystemButtonText")
        Label_4_Ft=tkinter.font.Font(family='微软雅黑', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Label_6 = tkinter.Label(Form_1,text="远程端口范围")
        Fun.Register(uiName,'PyMe_Label_6',Label_6,'range_name')
        Fun.SetControlPlace(uiName,'PyMe_Label_6',0.02097902097902098,0.5720930232558139,0.26223776223776224,0.09302325581395349,'nw',True,True)
        Label_6.configure(bg = "#F0F0F0")
        Label_6.configure(fg = "SystemButtonText")
        Label_6.configure(anchor = "w")
        Label_6_Ft=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_6.configure(font = Label_6_Ft)
        Label_7 = tkinter.Label(Form_1,text="10000-59999")
        Fun.Register(uiName,'PyMe_Label_7',Label_7,'range')
        Fun.SetControlPlace(uiName,'PyMe_Label_7',0.2867132867132867,0.5720930232558139,0.11276223776223776,0.09302325581395349,'nw',True,True)
        Label_7.configure(bg = "#F0F0F0")
        Label_7.configure(fg = "SystemButtonText")
        Label_7_Ft=tkinter.font.Font(family='微软雅黑', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_7.configure(font = Label_7_Ft)
        LabelButton_5= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_5',LabelButton_5,'setting')
        LabelButton_5.SetText("创建隧道")
        LabelButton_5.SetBGColor("#F0F0F0")
        LabelButton_5.SetFGColor("#000000")
        LabelButton_5_TitleFont=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_5.SetFont(LabelButton_5_TitleFont)
        LabelButton_5.SetBGImage("button1.png")
        LabelButton_5.SetBGColor_Hover("#AAAAAA")
        LabelButton_5.SetFGColor_Hover("#000000")
        LabelButton_5.SetBGImage_Hover("button1_hover.png")
        LabelButton_5.SetBGColor_Click("#AAAAAA")
        LabelButton_5.SetFGColor_Click("#FF0000")
        LabelButton_5.SetBGImage_Click("button1_click.png")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_5',0.42045454545454547,0.3302325581395349,0.10052447552447552,0.13953488372093023,'nw',True,True)
        LabelButton_5.Redraw()
        LabelButton_5.SetCommandFunction(VIP_cmd.setting_onCommand,self.uiName,"setting")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",VIP_cmd.Form_1_onLoad)
        #Add Some Logic Code Here: (Keep This Line of comments)
        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Configure>', self.Configure)
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)
    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.SetCanvasBGImage(self.uiName,'Form_1',"Resources/Tunnel_Card.png",'Zoom')
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    Fun.RunApplication(VIP)
