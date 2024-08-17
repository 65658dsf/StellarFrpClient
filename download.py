#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import download_cmd
import download_sty
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
class  download:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=download_cmd
        Fun.Register(uiName,'root',root)
        style = download_sty.SetupStyle(isTKroot)
        if isTKroot == True:
            root.resizable(False,False)
            Fun.SetTitleBar(root,titleText='下载窗口',isDarkMode=False)
            Fun.CenterDlg(uiName,root,360,248)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.minsize(360, 248)
            if os.path.exists("Resources/ico.ico"):
                root.iconbitmap("Resources/ico.ico")
            root.wm_attributes("-topmost",1)
            root['background'] = '#EFEFEF'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 360)
        Form_1.configure(height = 248)
        Form_1.configure(bg = "#EFEFEF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,360,248)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="下载文件")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.05555555555555555,0.08064516129032258,0.2777777777777778,0.1935483870967742,'nw',True,True)
        Label_2.configure(bg = "#EFEFEF")
        Label_2.configure(fg = "#000000")
        Label_2_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_3 = tkinter.Label(Form_1,text="test文件")
        Fun.Register(uiName,'PyMe_Label_3',Label_3,'file_name')
        Fun.SetControlPlace(uiName,'PyMe_Label_3',0.3888888888888889,0.08064516129032258,0.6111111111111112,0.1935483870967742,'nw',True,True)
        Label_3.configure(bg = "#EFEFEF")
        Label_3.configure(fg = "#000000")
        Label_3.configure(anchor = "w")
        Label_3_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)
        Label_4 = tkinter.Label(Form_1,text="下载进度")
        Fun.Register(uiName,'PyMe_Label_4',Label_4,'Label_3')
        Fun.SetControlPlace(uiName,'PyMe_Label_4',0.05555555555555555,0.3225806451612903,0.2777777777777778,0.1935483870967742,'nw',True,True)
        Label_4.configure(bg = "#EFEFEF")
        Label_4.configure(fg = "#000000")
        Label_4_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Label_10 = tkinter.Label(Form_1,text="Label")
        Fun.Register(uiName,'PyMe_Label_10',Label_10,'file_url')
        Fun.SetControlPlace(uiName,'PyMe_Label_10',142,78,100,48,'nw',False,True)
        Label_10.place_forget()
        Label_10.configure(bg = "#EFEFEF")
        Label_10.configure(fg = "#000000")
        Label_11 = tkinter.Label(Form_1,text="Label")
        Fun.Register(uiName,'PyMe_Label_11',Label_11,'file_path')
        Fun.SetControlPlace(uiName,'PyMe_Label_11',136,75,100,48,'nw',False,True)
        Label_11.place_forget()
        Label_11.configure(bg = "#EFEFEF")
        Label_11.configure(fg = "#000000")
        Label_12 = tkinter.Label(Form_1,text="Label")
        Fun.Register(uiName,'PyMe_Label_12',Label_12,'open_vaule')
        Fun.SetControlPlace(uiName,'PyMe_Label_12',147,80,100,48,'nw',False,True)
        Label_12.configure(bg = "#EFEFEF")
        Label_12.configure(fg = "#000000")
        Progress_7 = tkinter.ttk.Progressbar(Form_1)
        Fun.Register(uiName,'PyMe_Progress_7',Progress_7,'Progress_1')
        Fun.SetControlPlace(uiName,'PyMe_Progress_7',0.05555555555555555,0.5564516129032258,0.8888888888888888,0.08064516129032258,'nw',True,True)
        Progress_7.configure(orient = tkinter.HORIZONTAL)
        Progress_7.configure(mode = "determinate")
        Progress_7.configure(maximum = "100")
        Progress_7.configure(value = "0")
        LabelButton_8= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_8',LabelButton_8,'confirm')
        LabelButton_8.SetText("开始下载")
        LabelButton_8.SetBGColor("#EFEFEF")
        LabelButton_8.SetFGColor("#000000")
        LabelButton_8_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_8.SetFont(LabelButton_8_TitleFont)
        LabelButton_8.SetBGImage("BTN_B_blue.png")
        LabelButton_8.SetBGColor_Hover("#EFEFEF")
        LabelButton_8.SetFGColor_Hover("#000000")
        LabelButton_8.SetBGImage_Hover("BTN_B_blue_hover.png")
        LabelButton_8.SetBGColor_Click("#EFEFEF")
        LabelButton_8.SetFGColor_Click("#FF0000")
        LabelButton_8.SetBGImage_Click("BTN_B_blue_click.png")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_8',0.05555555555555555,0.6895161290322581,0.4444444444444444,0.1935483870967742,'nw',True,True)
        LabelButton_8.Redraw()
        LabelButton_8.SetCommandFunction(download_cmd.confirm_onCommand,self.uiName,"confirm")
        LabelButton_9= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_9',LabelButton_9,'cancel')
        LabelButton_9.SetText("取消下载")
        LabelButton_9.SetBGColor("#EFEFEF")
        LabelButton_9.SetFGColor("#000000")
        LabelButton_9_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_9.SetFont(LabelButton_9_TitleFont)
        LabelButton_9.SetBGImage("BTN_B_red.png")
        LabelButton_9.SetBGColor_Hover("#EFEFEF")
        LabelButton_9.SetFGColor_Hover("#000000")
        LabelButton_9.SetBGImage_Hover("BTN_B_red_hover.png")
        LabelButton_9.SetBGColor_Click("#EFEFEF")
        LabelButton_9.SetFGColor_Click("#FF0000")
        LabelButton_9.SetBGImage_Click("BTN_B_red_click.png")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_9',0.5027777777777778,0.6895161290322581,0.4444444444444444,0.1935483870967742,'nw',True,True)
        LabelButton_9.Redraw()
        LabelButton_9.SetCommandFunction(download_cmd.cancel_onCommand,self.uiName,"cancel")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",download_cmd.Form_1_onLoad)
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
    Fun.RunApplication(download)
