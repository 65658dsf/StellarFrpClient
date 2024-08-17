#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import get_vip_cmd
import get_vip_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  get_vip:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=get_vip_cmd
        Fun.Register(uiName,'root',root)
        style = get_vip_sty.SetupStyle()
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,398,186)
            root.wm_attributes("-topmost",1)
            root['background'] = '#FFFFFF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 398)
        Form_1.configure(height = 186)
        Form_1.configure(bg = "#FFFFFF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetCanvasBGImage(uiName,'Form_1',"Resources/Card.png",'Zoom')
        Fun.G_RootSize=[398,186]
        #Create the elements of root 
        Entry_3= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_3',Entry_3,'code')
        Entry_3.SetBGColor("#FFFFFF")
        Entry_3.SetFGColor("#000000")
        Entry_3_Font=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_3.SetFont(Entry_3_Font)
        Entry_3.SetTipText("请输入兑换码")
        Entry_3.SetTipFGColor("#888888")
        Entry_3.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_3',0.007537688442211055,0.26881720430107525,0.9874371859296482,0.25806451612903225)
        Label_2 = tkinter.Label(Form_1,text="会员兑换")
        Fun.Register(uiName,'Label_2',Label_2)
        Fun.SetControlPlace(uiName,'Label_2',0.007537688442211055,0.0,0.25125628140703515,0.25806451612903225)
        Label_2.configure(bg = "#FFFFFF")
        Label_2.configure(fg = "SystemButtonText")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        LabelButton_4= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_4',LabelButton_4,'LabelButton_1')
        LabelButton_4.SetText("兑换会员")
        LabelButton_4.SetBGColor("#efefef")
        LabelButton_4.SetFGColor("#000000")
        LabelButton_4_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_4.SetFont(LabelButton_4_TitleFont)
        LabelButton_4.SetBGImage("Button.png")
        LabelButton_4.SetBGColor_Hover("#AAAAAA")
        LabelButton_4.SetFGColor_Hover("#000000")
        LabelButton_4.SetBGColor_Click("#AAAAAA")
        LabelButton_4.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'LabelButton_4',0.007537688442211055,0.6290322580645161,0.4824120603015075,0.25806451612903225)
        LabelButton_4.Redraw()
        LabelButton_4.SetCommandFunction(get_vip_cmd.LabelButton_1_onCommand,self.uiName,"LabelButton_1")
        LabelButton_5= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_5',LabelButton_5,'LabelButton_2')
        LabelButton_5.SetText("获取兑换码")
        LabelButton_5.SetBGColor("#efefef")
        LabelButton_5.SetFGColor("#000000")
        LabelButton_5_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_5.SetFont(LabelButton_5_TitleFont)
        LabelButton_5.SetBGImage("Button.png")
        LabelButton_5.SetBGColor_Hover("#AAAAAA")
        LabelButton_5.SetFGColor_Hover("#000000")
        LabelButton_5.SetBGColor_Click("#AAAAAA")
        LabelButton_5.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'LabelButton_5',0.5050251256281407,0.6290322580645161,0.4824120603015075,0.25806451612903225)
        LabelButton_5.Redraw()
        LabelButton_5.SetCommandFunction(get_vip_cmd.LabelButton_2_onCommand,self.uiName,"LabelButton_2")
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
    Fun.RunApplication(get_vip)
