#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import main_cmd
import main_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import home
import create_tunnel
import create
import user
import log
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  main:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=main_cmd
        Fun.Register(uiName,'root',root)
        style = main_sty.SetupStyle(isTKroot)
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,1240,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1240)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,1240,900)
        #Create the elements of root 
        NoteBook_5 = tkinter.ttk.Notebook(Form_1)
        Fun.Register(uiName,'PyMe_NoteBook_5',NoteBook_5,'NoteBook_1')
        Fun.SetControlPlace(uiName,'PyMe_NoteBook_5',0.0,-0.03333333333333333,1.0,1.0333,'nw',True,True)
        NoteBook_5.configure(style ="NoteBook_1.TNotebook")
        PageFrame_1 = tkinter.Frame(NoteBook_5)
        PageFrame_1.place(x = 5,y = 25,width = 1230,height = -29)
        PageFrame_1.configure(bg ='SystemButtonFace')
        home.home(PageFrame_1,False)
        NoteBook_5.add(PageFrame_1,text = "home")
        PageFrame_2 = tkinter.Frame(NoteBook_5)
        PageFrame_2.place(x = 5,y = 25,width = 1230,height = -29)
        PageFrame_2.configure(bg ='SystemButtonFace')
        create_tunnel.create_tunnel(PageFrame_2,False)
        NoteBook_5.add(PageFrame_2,text = "create_tunnel")
        PageFrame_3 = tkinter.Frame(NoteBook_5)
        PageFrame_3.place(x = 5,y = 25,width = 1230,height = -29)
        PageFrame_3.configure(bg ='SystemButtonFace')
        create.create(PageFrame_3,False)
        NoteBook_5.add(PageFrame_3,text = "create")
        PageFrame_4 = tkinter.Frame(NoteBook_5)
        PageFrame_4.place(x = 5,y = 25,width = 1230,height = -29)
        PageFrame_4.configure(bg ='SystemButtonFace')
        user.user(PageFrame_4,False)
        NoteBook_5.add(PageFrame_4,text = "user")
        PageFrame_5 = tkinter.Frame(NoteBook_5)
        PageFrame_5.place(x = 5,y = 25,width = 1230,height = -29)
        PageFrame_5.configure(bg ='SystemButtonFace')
        log.log(PageFrame_5,False)
        NoteBook_5.add(PageFrame_5,text = "log")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
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
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    Fun.RunApplication(main)
