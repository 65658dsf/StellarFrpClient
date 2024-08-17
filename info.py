#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import info_cmd
import info_sty
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
class  info:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=info_cmd
        Fun.Register(uiName,'root',root)
        style = info_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,200,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#FFFFFF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 200)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#FFFFFF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetCanvasBGImage(uiName,'Form_1',"Resources/Card.png",'Zoom')
        Fun.G_RootSize=[200,900]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="主权限组")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.03015075376884422,0.0,0.5025125628140703,0.12903225806451613,'nw',True,True)
        Label_2.configure(bg = "#FFFFFF")
        Label_2.configure(fg = "#7B7B7B")
        Label_2.configure(anchor = "w")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="test")
        Fun.Register(uiName,'PyMe_Label_3',Label_3,'type')
        Fun.SetControlPlace(uiName,'PyMe_Label_3',0.03015075376884422,0.13978494623655913,0.5025125628140703,0.12903225806451613,'nw',True,True)
        Label_3.configure(bg = "#FFFFFF")
        Label_3.configure(fg = "SystemButtonText")
        Label_3.configure(anchor = "w")
        Label_3_Ft=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)
        Label_4 = tkinter.Label(Form_1,text="注册邮箱")
        Fun.Register(uiName,'PyMe_Label_4',Label_4,'Label_3')
        Fun.SetControlPlace(uiName,'PyMe_Label_4',0.03015075376884422,0.3655913978494624,0.5025125628140703,0.12903225806451613,'nw',True,True)
        Label_4.configure(bg = "#FFFFFF")
        Label_4.configure(fg = "#7B7B7B")
        Label_4.configure(anchor = "w")
        Label_4_Ft=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Label_5 = tkinter.Label(Form_1,text="test@qq.com")
        Fun.Register(uiName,'PyMe_Label_5',Label_5,'mail')
        Fun.SetControlPlace(uiName,'PyMe_Label_5',0.032663316582914576,0.5053763440860215,0.964824120603015,0.12903225806451613,'nw',True,True)
        Label_5.configure(bg = "#FFFFFF")
        Label_5.configure(fg = "SystemButtonText")
        Label_5.configure(anchor = "w")
        Label_5_Ft=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)
        Label_6 = tkinter.Label(Form_1,text="会员到期时间")
        Fun.Register(uiName,'PyMe_Label_6',Label_6,'Label_5')
        Fun.SetControlPlace(uiName,'PyMe_Label_6',0.03015075376884422,0.7311827956989247,0.5025125628140703,0.12903225806451613,'nw',True,True)
        Label_6.configure(bg = "#FFFFFF")
        Label_6.configure(fg = "#7B7B7B")
        Label_6.configure(anchor = "w")
        Label_6_Ft=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_6.configure(font = Label_6_Ft)
        Label_8 = tkinter.Label(Form_1,text="test")
        Fun.Register(uiName,'PyMe_Label_8',Label_8,'time')
        Fun.SetControlPlace(uiName,'PyMe_Label_8',0.032663316582914576,0.8709677419354839,0.964824120603015,0.12903225806451613,'nw',True,True)
        Label_8.configure(bg = "#FFFFFF")
        Label_8.configure(fg = "SystemButtonText")
        Label_8.configure(anchor = "w")
        Label_8_Ft=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_8.configure(font = Label_8_Ft)
        Label_9 = tkinter.Label(Form_1,text="Label")
        Fun.Register(uiName,'PyMe_Label_9',Label_9,'username')
        Fun.SetControlPlace(uiName,'PyMe_Label_9',0.6432160804020101,0.1989247311827957,0.25125628140703515,0.25806451612903225,'nw',False,True)
        Label_9.place_forget()
        Label_9.configure(bg = "#FFFFFF")
        Label_9.configure(fg = "SystemButtonText")
        Label_10 = tkinter.Label(Form_1,text="Label")
        Fun.Register(uiName,'PyMe_Label_10',Label_10,'password')
        Fun.SetControlPlace(uiName,'PyMe_Label_10',0.6432160804020101,0.1989247311827957,0.25125628140703515,0.25806451612903225,'nw',False,True)
        Label_10.place_forget()
        Label_10.configure(bg = "#FFFFFF")
        Label_10.configure(fg = "SystemButtonText")
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
            Fun.SetCanvasBGImage(self.uiName,'Form_1',"Resources/Card.png",'Zoom')
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    Fun.RunApplication(info)
