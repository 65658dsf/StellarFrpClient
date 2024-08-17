#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import log_cmd
import log_sty
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
class  log:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=log_cmd
        Fun.Register(uiName,'root',root)
        style = log_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,1440,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1440)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1440,900]
        #Create the elements of root 
        Text_2= EXUIControl.CustomText(Form_1,True)
        Fun.Register(uiName,'PyMe_Text_2',Text_2,'Text_1')
        Text_2.SetBGColor("#FFFFFF")
        Text_2.SetFGColor("SystemWindowText")
        Text_2_Font=tkinter.font.Font(family='微软雅黑', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Text_2.SetFont(Text_2_Font)
        Text_2.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Text_2',0.0,0.0,1.0,0.8889,'nw',True,True)
        Text_2.SetHScrollBar()
        Text_2_Ft=tkinter.font.Font(family='微软雅黑', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Text_2.configure(font = Text_2_Ft)
        Text_2.SetVScrollBar()
        LabelButton_4= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_4',LabelButton_4,'LabelButton_1')
        LabelButton_4.SetText("清空日志")
        LabelButton_4.SetBGColor("#efefef")
        LabelButton_4.SetFGColor("#000000")
        LabelButton_4_TitleFont=tkinter.font.Font(family='微软雅黑', size=30,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_4.SetFont(LabelButton_4_TitleFont)
        LabelButton_4.SetBGImage("Button.png")
        LabelButton_4.SetBGColor_Hover("#AAAAAA")
        LabelButton_4.SetFGColor_Hover("#000000")
        LabelButton_4.SetBGColor_Click("#AAAAAA")
        LabelButton_4.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_4',0.0,0.8888888888888888,1.0,0.1111111111111111,'nw',True,True)
        LabelButton_4.Redraw()
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
    def GetRootSize(self):
        return Fun.G_RootSize[0],Fun.G_RootSize[1]
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
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    Fun.RunApplication(log)
