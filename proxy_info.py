#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import proxy_info_cmd
import proxy_info_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  proxy_info:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=proxy_info_cmd
        Fun.Register(uiName,'root',root)
        style = proxy_info_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,352,900)
            root.wm_attributes("-topmost",1)
            root['background'] = '#F0F0F0'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 352)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#F0F0F0")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[352,900]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="正在运行的隧道:")
        Fun.Register(uiName,'Label_2',Label_2,'Label_1')
        Fun.SetControlPlace(uiName,'Label_2',0.06818181818181818,0.03333333333333333,0.8409090909090909,0.028888888888888888)
        Label_2.configure(bg = "#F0F0F0")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(anchor = "w")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="隧道管理")
        Fun.Register(uiName,'Label_3',Label_3,'Label_2')
        Fun.SetControlPlace(uiName,'Label_3',0.06818181818181818,0.42444444444444446,0.8409090909090909,0.028888888888888888)
        Label_3.configure(bg = "#F0F0F0")
        Label_3.configure(fg = "SystemButtonText")
        Label_3.configure(anchor = "w")
        Label_3_Ft=tkinter.font.Font(family='微软雅黑', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)
        Label_4 = tkinter.Label(Form_1,text="软件公告")
        Fun.Register(uiName,'Label_4',Label_4,'Label_3')
        Fun.SetControlPlace(uiName,'Label_4',0.06818181818181818,0.7911111111111111,0.8409090909090909,0.028888888888888888)
        Label_4.configure(bg = "#F0F0F0")
        Label_4.configure(fg = "SystemButtonText")
        Label_4.configure(anchor = "w")
        Label_4_Ft=tkinter.font.Font(family='微软雅黑', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
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
    Fun.RunApplication(proxy_info)
