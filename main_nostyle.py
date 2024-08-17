#coding=utf-8
#import libs 
import sys
import main_cmd
import main_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import os
import home
import create_tunnel
import create
import manage
import user
import log
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
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
        style = main_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,1240,900)
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1240)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1240,900]
        #Create the elements of root 
        NoteBook_4 = tkinter.ttk.Notebook(Form_1)
        Fun.Register(uiName,'NoteBook_4',NoteBook_4,'NoteBook_1')
        Fun.SetControlPlace(uiName,'NoteBook_4',0,-30,1240,930)
        PageFrame_1 = tkinter.ttk.Frame(NoteBook_4)
        PageFrame_1.place(x = 5,y = -5,width = 1230,height = 900)
        PageFrame_1.configure(style ="TNotebook")
        home.home(PageFrame_1,False)
        NoteBook_4.add(PageFrame_1,text = "home")
        PageFrame_2 = tkinter.ttk.Frame(NoteBook_4)
        PageFrame_2.place(x = 5,y = -5,width = 1230,height = 900)
        PageFrame_2.configure(style ="TNotebook")
        create_tunnel.create_tunnel(PageFrame_2,False)
        NoteBook_4.add(PageFrame_2,text = "create_tunnel")
        PageFrame_3 = tkinter.ttk.Frame(NoteBook_4)
        PageFrame_3.place(x = 5,y = -5,width = 1230,height = 900)
        PageFrame_3.configure(style ="TNotebook")
        create.create(PageFrame_3,False)
        NoteBook_4.add(PageFrame_3,text = "create")
        PageFrame_4 = tkinter.ttk.Frame(NoteBook_4)
        PageFrame_4.place(x = 5,y = -5,width = 1230,height = 900)
        PageFrame_4.configure(style ="TNotebook")
        manage.manage(PageFrame_4,False)
        NoteBook_4.add(PageFrame_4,text = "manage")
        PageFrame_5 = tkinter.ttk.Frame(NoteBook_4)
        PageFrame_5.place(x = 5,y = -5,width = 1230,height = 900)
        PageFrame_5.configure(style ="TNotebook")
        user.user(PageFrame_5,False)
        NoteBook_4.add(PageFrame_5,text = "user")
        PageFrame_6 = tkinter.ttk.Frame(NoteBook_4)
        PageFrame_6.place(x = 5,y = -5,width = 1230,height = 900)
        PageFrame_6.configure(style ="TNotebook")
        log.log(PageFrame_6,False)
        NoteBook_4.add(PageFrame_6,text = "log")
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
            Fun.SetControlPlace(uiName,'NoteBook_1',0,-30,1240,930)
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = main(root)
    root.mainloop()
