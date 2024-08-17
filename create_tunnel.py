#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import create_tunnel_cmd
import create_tunnel_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import VIP
import FREE
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  create_tunnel:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=create_tunnel_cmd
        Fun.Register(uiName,'root',root)
        style = create_tunnel_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,1240,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#FFFFFF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1240)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#FFFFFF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1240,900]
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="创建隧道")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'title')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.03870967741935484,0.07,0.8064516129032258,0.05555555555555555,'nw',True,True)
        Label_2.configure(bg = "#FFFFFF")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(anchor = "w")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=36,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Frame_20 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_20',Frame_20,'VIP')
        Fun.SetControlPlace(uiName,'PyMe_Frame_20',0.03870967741935484,0.44333333333333336,0.9225806451612903,0.2388888888888889,'nw',True,True)
        Frame_20.configure(bg = "#CCCCCC")
        VIP_20 = VIP.VIP(Frame_20,False)
        Fun.Register(uiName,'VIP_20',VIP_20)
        Frame_21 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'PyMe_Frame_21',Frame_21,'free')
        Fun.SetControlPlace(uiName,'PyMe_Frame_21',0.03870967741935484,0.17777777777777778,0.9225806451612903,0.2388888888888889,'nw',True,True)
        Frame_21.configure(bg = "#CCCCCC")
        FREE_21 = FREE.FREE(Frame_21,False)
        Fun.Register(uiName,'FREE_21',FREE_21)
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
    Fun.RunApplication(create_tunnel)
