#coding=utf-8
#import libs 
import sys
import login_main_cmd
import login_main_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  login_main:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=login_main_cmd
        Fun.Register(uiName,'root',root)
        style = login_main_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            Fun.CenterDlg(uiName,root,390,524)
            root.wm_attributes("-topmost",1)
            root['background'] = '#FFFFFF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 390)
        Form_1.configure(height = 524)
        Form_1.configure(bg = "#FFFFFF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[390,524]
        #Create the elements of root 
        LabelButton_2= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_2',LabelButton_2,'login')
        LabelButton_2.SetText("登录")
        LabelButton_2.SetBGColor("#FFFFFF")
        LabelButton_2.SetFGColor("#2468F2")
        LabelButton_2_TitleFont=tkinter.font.Font(family='微软雅黑', size=26,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_2.SetFont(LabelButton_2_TitleFont)
        LabelButton_2.SetBGColor_Hover("#FFFFFF")
        LabelButton_2.SetFGColor_Hover("#2468F2")
        LabelButton_2.SetBGColor_Click("#FFFFFF")
        LabelButton_2.SetFGColor_Click("#2468F2")
        Fun.SetControlPlace(uiName,'LabelButton_2',0,50,195,48)
        LabelButton_2.Redraw()
        LabelButton_3= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_3',LabelButton_3,'reg')
        LabelButton_3.SetText("注册")
        LabelButton_3.SetBGColor("#FFFFFF")
        LabelButton_3.SetFGColor("#000000")
        LabelButton_3_TitleFont=tkinter.font.Font(family='微软雅黑', size=26,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_3.SetFont(LabelButton_3_TitleFont)
        LabelButton_3.SetBGColor_Hover("#AAAAAA")
        LabelButton_3.SetFGColor_Hover("#000000")
        LabelButton_3.SetBGColor_Click("#AAAAAA")
        LabelButton_3.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'LabelButton_3',195,50,195,48)
        LabelButton_3.Redraw()
        LabelButton_6= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_6',LabelButton_6,'login_bt')
        LabelButton_6.SetText("登录")
        LabelButton_6.SetBGColor("#efefef")
        LabelButton_6.SetFGColor("#FFFFFF")
        LabelButton_6_TitleFont=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_6.SetFont(LabelButton_6_TitleFont)
        LabelButton_6.SetBGImage("an.png")
        LabelButton_6.SetBGColor_Hover("#AAAAAA")
        LabelButton_6.SetFGColor_Hover("#000000")
        LabelButton_6.SetBGImage_Hover("an1.png")
        LabelButton_6.SetBGColor_Click("#AAAAAA")
        LabelButton_6.SetFGColor_Click("#FF0000")
        LabelButton_6.SetBGImage_Click("an2.png")
        Fun.SetControlPlace(uiName,'LabelButton_6',46,325,300,48)
        LabelButton_6.Redraw()
        Entry_5= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_5',Entry_5,'password')
        Entry_5.SetBGColor("#FFFFFF")
        Entry_5.SetFGColor("#000000")
        Entry_5_Font=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_5.SetFont(Entry_5_Font)
        Entry_5.SetShowChar("●")
        Entry_5.SetTipText("密码")
        Entry_5.SetTipFGColor("#888888")
        Entry_5.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_5',53,226,286,48)
        Entry_9= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_9',Entry_9,'username')
        Entry_9.SetBGColor("#FFFFFF")
        Entry_9.SetFGColor("#000000")
        Entry_9_Font=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_9.SetFont(Entry_9_Font)
        Entry_9.SetTipText("用户名或邮箱")
        Entry_9.SetTipFGColor("#888888")
        Entry_9.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_9',50,136,286,48)
        Label_7 = tkinter.Label(Form_1,text="温馨提示",autostyle=False)
        Fun.Register(uiName,'Label_7',Label_7,'wxts')
        Fun.SetControlPlace(uiName,'Label_7',53,403,100,48)
        Label_7.configure(bg = "#FFFFFF")
        Label_7.configure(fg = "#878787")
        Label_7.configure(relief = "flat")
        Label_7_Ft=tkinter.font.Font(family='微软雅黑', size=17,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_7.configure(font = Label_7_Ft)
        Label_8 = tkinter.Label(Form_1,text="密码需要数字+字母的组合哦~",autostyle=False)
        Fun.Register(uiName,'Label_8',Label_8,'Label_2')
        Fun.SetControlPlace(uiName,'Label_8',53,448,322,48)
        Label_8.configure(bg = "#FFFFFF")
        Label_8.configure(fg = "#878787")
        Label_8.configure(anchor = "w")
        Label_8.configure(relief = "flat")
        Label_8_Ft=tkinter.font.Font(family='微软雅黑', size=17,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_8.configure(font = Label_8_Ft)
        Label_11 = tkinter.Label(Form_1,text="记住密码",autostyle=False)
        Fun.Register(uiName,'Label_11',Label_11,'Label_3')
        Fun.SetControlPlace(uiName,'Label_11',168,412,90,30)
        Label_11.configure(bg = "#FFFFFF")
        Label_11.configure(fg = "#878787")
        Label_11.configure(anchor = "w")
        Label_11.configure(relief = "flat")
        Label_11_Ft=tkinter.font.Font(family='微软雅黑', size=17,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_11.configure(font = Label_11_Ft)
        Label_11.lift()
        SwitchButton_10= EXUIControl.SwitchButton(Form_1)
        Fun.Register(uiName,'SwitchButton_10',SwitchButton_10,'SwitchButton_1')
        SwitchButton_10.SetShape('circular')
        SwitchButton_10.SetOffStateBGColor("#333333")
        SwitchButton_10.SetOffStateText("开启")
        SwitchButton_10.SetOffStateTextColor("#FFFFFF")
        SwitchButton_10.SetOffStateButtonColor("#FFFFFF")
        SwitchButton_10.SetOnStateBGColor("#2F9F00")
        SwitchButton_10.SetOnStateText("关闭")
        SwitchButton_10.SetOnStateTextColor("#FFFFFF")
        SwitchButton_10.SetOnStateButtonColor("#FFFFFF")
        SwitchButton_10_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=9,weight='normal',slant='roman',underline=0,overstrike=0)
        SwitchButton_10.SetFont(SwitchButton_10_Font)
        SwitchButton_10.SetSwitchMode(1)
        Fun.SetControlPlace(uiName,'SwitchButton_10',258,412,78,30)
        SwitchButton_10.Redraw()
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
    root = tkinter.Tk()
    MyDlg = login_main(root)
    root.mainloop()
