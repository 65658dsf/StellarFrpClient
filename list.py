#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import list_cmd
import list_sty
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
class  list:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=list_cmd
        Fun.Register(uiName,'root',root)
        style = list_sty.SetupStyle(isTKroot)
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,200,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 200)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,200,900)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="恒星穿透")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'title')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.125,0.05333333333333334,0.75,0.05333333333333334,'nw',True,True)
        Label_2.configure(bg = "#efefef")
        Label_2.configure(fg = "SystemButtonText")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=28,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        LabelButton_3= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_3',LabelButton_3,'home')
        LabelButton_3.SetText("首页")
        LabelButton_3.SetBGColor("#efefef")
        LabelButton_3.SetFGColor("#000000")
        LabelButton_3_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_3.SetFont(LabelButton_3_TitleFont)
        LabelButton_3.SetBGColor_Hover("#AAAAAA")
        LabelButton_3.SetFGColor_Hover("#AAAAAA")
        LabelButton_3.SetBGColor_Click("#AAAAAA")
        LabelButton_3.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_3',0.16,0.1711111111111111,0.705,0.0356,'nw',True,True)
        LabelButton_3.Redraw()
        LabelButton_3.SetCommandFunction(list_cmd.home_onCommand,self.uiName,"home")
        LabelButton_4= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_4',LabelButton_4,'create')
        LabelButton_4.SetText("创建隧道")
        LabelButton_4.SetBGColor("#efefef")
        LabelButton_4.SetFGColor("#000000")
        LabelButton_4_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_4.SetFont(LabelButton_4_TitleFont)
        LabelButton_4.SetBGColor_Hover("#AAAAAA")
        LabelButton_4.SetFGColor_Hover("#000000")
        LabelButton_4.SetBGColor_Click("#AAAAAA")
        LabelButton_4.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_4',0.16,0.22,0.705,0.0356,'nw',True,True)
        LabelButton_4.Redraw()
        LabelButton_4.SetCommandFunction(list_cmd.create_onCommand,self.uiName,"create")
        LabelButton_5= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_5',LabelButton_5,'manage')
        LabelButton_5.SetText("管理隧道")
        LabelButton_5.SetBGColor("#efefef")
        LabelButton_5.SetFGColor("#000000")
        LabelButton_5_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_5.SetFont(LabelButton_5_TitleFont)
        LabelButton_5.SetBGColor_Hover("#AAAAAA")
        LabelButton_5.SetFGColor_Hover("#000000")
        LabelButton_5.SetBGColor_Click("#AAAAAA")
        LabelButton_5.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_5',0.16,0.2733333333333333,0.705,0.0356,'nw',True,True)
        LabelButton_5.Redraw()
        LabelButton_5.SetCommandFunction(list_cmd.manage_onCommand,self.uiName,"manage")
        LabelButton_7= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_7',LabelButton_7,'log')
        LabelButton_7.SetText("隧道日志")
        LabelButton_7.SetBGColor("#efefef")
        LabelButton_7.SetFGColor("#000000")
        LabelButton_7_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_7.SetFont(LabelButton_7_TitleFont)
        LabelButton_7.SetBGColor_Hover("#AAAAAA")
        LabelButton_7.SetFGColor_Hover("#000000")
        LabelButton_7.SetBGColor_Click("#AAAAAA")
        LabelButton_7.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_7',0.16,0.32666666666666666,0.705,0.0356,'nw',True,True)
        LabelButton_7.Redraw()
        LabelButton_7.SetCommandFunction(list_cmd.log_onCommand,self.uiName,"log")
        LabelButton_8= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_8',LabelButton_8,'setting')
        LabelButton_8.SetText("设置")
        LabelButton_8.SetBGColor("#efefef")
        LabelButton_8.SetFGColor("#000000")
        LabelButton_8_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_8.SetFont(LabelButton_8_TitleFont)
        LabelButton_8.SetBGColor_Hover("#AAAAAA")
        LabelButton_8.SetFGColor_Hover("#000000")
        LabelButton_8.SetBGColor_Click("#AAAAAA")
        LabelButton_8.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_8',0.16,0.8666666666666667,0.705,0.0356,'nw',True,True)
        LabelButton_8.Redraw()
        LabelButton_8.SetCommandFunction(list_cmd.setting_onCommand,self.uiName,"setting")
        LabelButton_9= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_9',LabelButton_9,'exit')
        LabelButton_9.SetText("登出")
        LabelButton_9.SetBGColor("#EFEFEF")
        LabelButton_9.SetFGColor("#000000")
        LabelButton_9_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_9.SetFont(LabelButton_9_TitleFont)
        LabelButton_9.SetBGColor_Hover("#AAAAAA")
        LabelButton_9.SetFGColor_Hover("#AAAAAA")
        LabelButton_9.SetBGColor_Click("#AAAAAA")
        LabelButton_9.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_9',0.16,0.92,0.705,0.0356,'nw',True,True)
        LabelButton_9.Redraw()
        LabelButton_9.SetCommandFunction(list_cmd.exit_onCommand,self.uiName,"exit")
        LabelButton_10= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_10',LabelButton_10,'LabelButton_8')
        LabelButton_10.SetText("退出软件")
        LabelButton_10.SetBGColor("#EFEFEF")
        LabelButton_10.SetFGColor("#000000")
        LabelButton_10_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_10.SetFont(LabelButton_10_TitleFont)
        LabelButton_10.SetBGColor_Hover("#AAAAAA")
        LabelButton_10.SetFGColor_Hover("#000000")
        LabelButton_10.SetBGColor_Click("#AAAAAA")
        LabelButton_10.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_10',0.16,0.7966666666666666,0.705,0.0356,'nw',True,True)
        LabelButton_10.Redraw()
        LabelButton_10.SetCommandFunction(list_cmd.LabelButton_8_onCommand,self.uiName,"LabelButton_8")
        LabelButton_11= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_11',LabelButton_11,'server')
        LabelButton_11.SetText("游戏管理")
        LabelButton_11.SetBGColor("#efefef")
        LabelButton_11.SetFGColor("#000000")
        LabelButton_11_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_11.SetFont(LabelButton_11_TitleFont)
        LabelButton_11.SetBGColor_Hover("#AAAAAA")
        LabelButton_11.SetFGColor_Hover("#000000")
        LabelButton_11.SetBGColor_Click("#AAAAAA")
        LabelButton_11.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_11',0.16,0.38,0.705,0.03556,'nw',True,True)
        LabelButton_11.Redraw()
        LabelButton_11.SetCommandFunction(list_cmd.server_onCommand,self.uiName,"server")
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
    Fun.RunApplication(list)
