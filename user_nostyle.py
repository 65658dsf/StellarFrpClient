#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
sys.path.insert(0,"tunnel_list")
sys.path.insert(0,"tunnel")
import user_cmd
import user_sty
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
class  user:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=user_cmd
        Fun.Register(uiName,'root',root)
        style = user_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,1240,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#F0F0F0'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1240)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#F0F0F0")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1240,900]
        #Create the elements of root 
        Frame_3 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_3',Frame_3,'Frame_1')
        Fun.SetControlPlace(uiName,'PyMe_Frame_3',0.0,0.05333333333333334,1.0,0.08888888888888889,'nw',False,True)
        Frame_3.place_forget()
        Frame_3.configure(bg = "#CCCCCC")
        Frame_8 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_8',Frame_8,'Frame_2')
        Fun.SetControlPlace(uiName,'PyMe_Frame_8',0.0,0.14777777777777779,1.0,0.08888888888888889,'nw',False,True)
        Frame_8.place_forget()
        Frame_8.configure(bg = "#CCCCCC")
        Frame_9 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_9',Frame_9,'Frame_3')
        Fun.SetControlPlace(uiName,'PyMe_Frame_9',0.0,0.2477777777777778,1.0,0.08888888888888889,'nw',False,True)
        Frame_9.place_forget()
        Frame_9.configure(bg = "#CCCCCC")
        Frame_10 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_10',Frame_10,'Frame_4')
        Fun.SetControlPlace(uiName,'PyMe_Frame_10',0.0,0.3477777777777778,1.0,0.08888888888888889,'nw',False,True)
        Frame_10.place_forget()
        Frame_10.configure(bg = "#CCCCCC")
        Frame_11 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_11',Frame_11,'Frame_5')
        Fun.SetControlPlace(uiName,'PyMe_Frame_11',0.0,0.4477777777777778,1.0,0.08888888888888889,'nw',False,True)
        Frame_11.place_forget()
        Frame_11.configure(bg = "#CCCCCC")
        Frame_12 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_12',Frame_12,'Frame_6')
        Fun.SetControlPlace(uiName,'PyMe_Frame_12',0.0,0.5488888888888889,1.0,0.08888888888888889,'nw',False,True)
        Frame_12.place_forget()
        Frame_12.configure(bg = "#CCCCCC")
        Frame_13 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_13',Frame_13,'Frame_7')
        Fun.SetControlPlace(uiName,'PyMe_Frame_13',0.0,0.6477777777777778,1.0,0.08888888888888889,'nw',False,True)
        Frame_13.place_forget()
        Frame_13.configure(bg = "#CCCCCC")
        Frame_14 = tkinter.Frame(Form_1,autostyle=False)
        Fun.Register(uiName,'PyMe_Frame_14',Frame_14,'Frame_8')
        Fun.SetControlPlace(uiName,'PyMe_Frame_14',0.0,0.7477777777777778,1.0,0.08888888888888889,'nw',False,True)
        Frame_14.place_forget()
        Frame_14.configure(bg = "#CCCCCC")
        Label_4 = tkinter.Label(Form_1,text="ID-隧道名",autostyle=False)
        Fun.Register(uiName,'PyMe_Label_4',Label_4,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_4',0.012903225806451613,0.0,0.20161290322580644,0.05333333333333334,'nw',True,True)
        Label_4.configure(bg = "#F0F0F0")
        Label_4.configure(fg = "SystemButtonText")
        Label_4_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Label_5 = tkinter.Label(Form_1,text="隧道类型",autostyle=False)
        Fun.Register(uiName,'PyMe_Label_5',Label_5,'Label_2')
        Fun.SetControlPlace(uiName,'PyMe_Label_5',0.2903225806451613,0.0,0.08064516129032258,0.05333333333333334,'nw',True,True)
        Label_5.configure(bg = "#F0F0F0")
        Label_5.configure(fg = "SystemButtonText")
        Label_5_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)
        Label_6 = tkinter.Label(Form_1,text="远程端口",autostyle=False)
        Fun.Register(uiName,'PyMe_Label_6',Label_6,'Label_3')
        Fun.SetControlPlace(uiName,'PyMe_Label_6',0.38387096774193546,0.0,0.08064516129032258,0.052222222222222225,'nw',True,True)
        Label_6.configure(bg = "#F0F0F0")
        Label_6.configure(fg = "SystemButtonText")
        Label_6_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_6.configure(font = Label_6_Ft)
        Label_7 = tkinter.Label(Form_1,text="所属节点",autostyle=False)
        Fun.Register(uiName,'PyMe_Label_7',Label_7,'Label_4')
        Fun.SetControlPlace(uiName,'PyMe_Label_7',0.5177419354838709,0.0,0.08064516129032258,0.05333333333333334,'nw',True,True)
        Label_7.configure(bg = "#F0F0F0")
        Label_7.configure(fg = "SystemButtonText")
        Label_7_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_7.configure(font = Label_7_Ft)
        LabelButton_17= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_17',LabelButton_17,'LabelButton_1')
        LabelButton_17.SetText("刷新节点列表")
        LabelButton_17.SetBGColor("#FFFFFF")
        LabelButton_17.SetFGColor("#000000")
        LabelButton_17_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_17.SetFont(LabelButton_17_TitleFont)
        LabelButton_17.SetBGColor_Hover("#AAAAAA")
        LabelButton_17.SetFGColor_Hover("#000000")
        LabelButton_17.SetBGColor_Click("#AAAAAA")
        LabelButton_17.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_17',0.6669354838709678,0.0,0.15,0.05333333333333334,'nw',True,True)
        LabelButton_17.Redraw()
        #Timer_18.xy(1059,0)
        Fun.Register(uiName,'PyMe_Timer_18',Timer_18,'Timer_1')
        Timer_18.SetWidget(Form_1)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
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
    Fun.RunApplication(user)
