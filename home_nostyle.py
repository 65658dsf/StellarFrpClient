#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import home_cmd
import home_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import proxy_info
import get_vip
import user_tunnel
import info
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  home:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=home_cmd
        Fun.Register(uiName,'root',root)
        style = home_sty.SetupStyle()
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
        Label_2 = tkinter.Label(Form_1,text="你好，NingMeng123",autostyle=False)
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'title')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.01935483870967742,0.02666666666666667,0.4645161290322581,0.04777777777777778,'nw',True,True)
        Label_2.configure(bg = "#FFFFFF")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(anchor = "sw")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=28,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Frame_4 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_4',Frame_4,'proxy_info')
        Fun.SetControlPlace(uiName,'PyMe_Frame_4',0.6903225806451613,0.0,0.2839,1.0,'nw',True,True)
        Frame_4.configure(bg = "#CCCCCC")
        proxy_info_4 = proxy_info.proxy_info(Frame_4,False)
        Fun.Register(uiName,'proxy_info_4',proxy_info_4)
        Frame_5 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_5',Frame_5,'code')
        Fun.SetControlPlace(uiName,'PyMe_Frame_5',0.35,0.10444444444444445,0.3209677419354839,0.20666666666666667,'nw',True,True)
        Frame_5.configure(bg = "#CCCCCC")
        get_vip_5 = get_vip.get_vip(Frame_5,False)
        Fun.Register(uiName,'get_vip_5',get_vip_5)
        Frame_6 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_6',Frame_6,'user_tunnel')
        Fun.SetControlPlace(uiName,'PyMe_Frame_6',0.01935483870967742,0.3244444444444444,0.646,0.6489,'nw',True,True)
        Frame_6.configure(bg = "#CCCCCC")
        user_tunnel_6 = user_tunnel.user_tunnel(Frame_6,False)
        Fun.Register(uiName,'user_tunnel_6',user_tunnel_6)
        Frame_7 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_7',Frame_7,'user_info')
        Fun.SetControlPlace(uiName,'PyMe_Frame_7',0.01935483870967742,0.10444444444444445,0.3209677419354839,0.20666666666666667,'nw',True,True)
        Frame_7.configure(bg = "#CCCCCC")
        info_7 = info.info(Frame_7,False)
        Fun.Register(uiName,'info_7',info_7)
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
    Fun.RunApplication(home)
