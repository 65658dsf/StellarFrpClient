#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import reset_pw_cmd
import reset_pw_sty
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
class  reset_pw:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=reset_pw_cmd
        Fun.Register(uiName,'root',root)
        style = reset_pw_sty.SetupStyle(isTKroot)
        if isTKroot == True:
            Fun.SetTitleBar(root,titleText='Form1',isDarkMode=False)
            Fun.CenterDlg(uiName,root,1440,900)
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-topmost",1)
            root['background'] = '#FFFFFF'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1440)
        Form_1.configure(height = 900)
        Form_1.configure(bg = "#FFFFFF")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetUIRootSize(uiName,1440,900)
        #Create the elements of root 
        LabelButton_2= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_2',LabelButton_2,'login')
        LabelButton_2.SetText("登录")
        LabelButton_2.SetBGColor("#FFFFFF")
        LabelButton_2.SetFGColor("#000000")
        LabelButton_2_TitleFont=tkinter.font.Font(family='微软雅黑', size=26,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_2.SetFont(LabelButton_2_TitleFont)
        LabelButton_2.SetBGColor_Hover("#AAAAAA")
        LabelButton_2.SetFGColor_Hover("#000000")
        LabelButton_2.SetBGColor_Click("#AAAAAA")
        LabelButton_2.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_2',0.5944444444444444,0.21777777777777776,0.13541666666666666,0.05333333333333334,'nw',True,True)
        LabelButton_2.Redraw()
        LabelButton_2.SetCommandFunction(reset_pw_cmd.login_onCommand,self.uiName,"login")
        LabelButton_3= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_3',LabelButton_3,'reg')
        LabelButton_3.SetText("改密")
        LabelButton_3.SetBGColor("#FFFFFF")
        LabelButton_3.SetFGColor("#2468F2")
        LabelButton_3_TitleFont=tkinter.font.Font(family='微软雅黑', size=26,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_3.SetFont(LabelButton_3_TitleFont)
        LabelButton_3.SetBGColor_Hover("#FFFFFF")
        LabelButton_3.SetFGColor_Hover("#2468F2")
        LabelButton_3.SetBGColor_Click("#FFFFFF")
        LabelButton_3.SetFGColor_Click("#2468F2")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_3',0.7049,0.2233,0.1354,0.05333,'nw',True,True)
        LabelButton_3.Redraw()
        LabelButton_11= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_11',LabelButton_11,'LabelButton_3')
        LabelButton_11.SetText("发送验证码")
        LabelButton_11.SetBGColor("#FFFFFF")
        LabelButton_11.SetFGColor("#000000")
        LabelButton_11_TitleFont=tkinter.font.Font(family='微软雅黑', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_11.SetFont(LabelButton_11_TitleFont)
        LabelButton_11.SetBGColor_Hover("#AAAAAA")
        LabelButton_11.SetFGColor_Hover("#000000")
        LabelButton_11.SetBGColor_Click("#AAAAAA")
        LabelButton_11.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_11',0.7194444444444444,0.5233333333333333,0.10069444444444445,0.05333333333333334,'nw',True,True)
        LabelButton_11.Redraw()
        LabelButton_11.SetCommandFunction(reset_pw_cmd.LabelButton_3_onCommand,self.uiName,"LabelButton_3")
        LabelButton_13= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_13',LabelButton_13,'LabelButton_4')
        LabelButton_13.SetText("《风林水起用户协议》")
        LabelButton_13.SetBGColor("#FFFFFF")
        LabelButton_13.SetFGColor("#2468F2")
        LabelButton_13_TitleFont=tkinter.font.Font(family='微软雅黑', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_13.SetFont(LabelButton_13_TitleFont)
        LabelButton_13.SetBGColor_Hover("#FFFFFF")
        LabelButton_13.SetFGColor_Hover("#000000")
        LabelButton_13.SetBGColor_Click("#FFFFFF")
        LabelButton_13.SetFGColor_Click("#FF0000")
        LabelButton_13.SetAnchor("w")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_13',0.7118055555555556,0.58,0.11944444444444445,0.05333333333333334,'nw',True,True)
        LabelButton_13.Redraw()
        LabelButton_14= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_14',LabelButton_14,'reg_bt')
        LabelButton_14.SetText("修改密码")
        LabelButton_14.SetBGColor("#FFFFFF")
        LabelButton_14.SetFGColor("#FFFFFF")
        LabelButton_14_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_14.SetFont(LabelButton_14_TitleFont)
        LabelButton_14.SetBGImage("an.png")
        LabelButton_14.SetBGColor_Hover("#AAAAAA")
        LabelButton_14.SetFGColor_Hover("#000000")
        LabelButton_14.SetBGImage_Hover("an1.png")
        LabelButton_14.SetBGColor_Click("#AAAAAA")
        LabelButton_14.SetFGColor_Click("#FF0000")
        LabelButton_14.SetBGImage_Click("an2.png")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_14',0.6271,0.6378,0.1931,0.05333,'nw',True,True)
        LabelButton_14.Redraw()
        LabelButton_14.SetCommandFunction(reset_pw_cmd.reg_bt_onCommand,self.uiName,"reg_bt")
        Entry_4= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_4',Entry_4,'mail')
        Entry_4.SetBGColor("#FFFFFF")
        Entry_4.SetBGColor_ReadOnly("#EFEFEF")
        Entry_4.SetFGColor("#000000")
        Entry_4_Font=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_4.SetFont(Entry_4_Font)
        Entry_4.SetTipText("请输入邮箱")
        Entry_4.SetTipFGColor("#888888")
        Entry_4.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_4',0.6277777777777778,0.30666666666666664,0.1909722222222222,0.05333333333333334,'nw',True,True)
        Entry_5= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_5',Entry_5,'username')
        Entry_5.SetBGColor("#FFFFFF")
        Entry_5.SetBGColor_ReadOnly("#EFEFEF")
        Entry_5.SetFGColor("#000000")
        Entry_5_Font=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_5.SetFont(Entry_5_Font)
        Entry_5.SetTipText("请输入用户名(需和前用户名相同)")
        Entry_5.SetTipFGColor("#888888")
        Entry_5.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_5',0.6291666666666667,0.3788888888888889,0.1909722222222222,0.05333333333333334,'nw',True,True)
        Entry_6= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_6',Entry_6,'password')
        Entry_6.SetBGColor("#FFFFFF")
        Entry_6.SetBGColor_ReadOnly("#EFEFEF")
        Entry_6.SetFGColor("#000000")
        Entry_6_Font=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_6.SetFont(Entry_6_Font)
        Entry_6.SetTipText("请输入密码")
        Entry_6.SetTipFGColor("#888888")
        Entry_6.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_6',0.6291666666666667,0.45111111111111113,0.1909722222222222,0.05333333333333334,'nw',True,True)
        Entry_7= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_7',Entry_7,'mail_key')
        Entry_7.SetBGColor("#FFFFFF")
        Entry_7.SetBGColor_ReadOnly("#EFEFEF")
        Entry_7.SetFGColor("#000000")
        Entry_7_Font=tkinter.font.Font(family='微软雅黑', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_7.SetFont(Entry_7_Font)
        Entry_7.SetTipText("请输入验证码")
        Entry_7.SetTipFGColor("#888888")
        Entry_7.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_7',0.6291666666666667,0.5233333333333333,0.09236111111111112,0.05333333333333334,'nw',True,True)
        CheckButton_12_Variable = Fun.AddTKVariable(uiName,'PyMe_CheckButton_12')
        CheckButton_12_Variable.set(False)
        CheckButton_12 = tkinter.Checkbutton(Form_1,variable=CheckButton_12_Variable,text="请阅读并同意",anchor=tkinter.W)
        Fun.Register(uiName,'PyMe_CheckButton_12',CheckButton_12,'check')
        Fun.SetControlPlace(uiName,'PyMe_CheckButton_12',0.6277777777777778,0.5844444444444444,0.09166666666666666,0.044444444444444446,'nw',True,True)
        CheckButton_12.configure(bg = "#FFFFFF")
        CheckButton_12.configure(fg = "#000000")
        CheckButton_12.configure(activebackground = "#FFFFFF")
        CheckButton_12.configure(activeforeground = "#000000")
        CheckButton_12.configure(selectcolor = "#FFFFFF")
        Fun.SetCheckButtonSelectedColor(uiName,'PyMe_CheckButton_12','#FFFFFF','#000000')
        CheckButton_12_Ft=tkinter.font.Font(family='微软雅黑', size=13,weight='normal',slant='roman',underline=0,overstrike=0)
        CheckButton_12.configure(font = CheckButton_12_Ft)
        Fun.SetElementLayer(uiName,'check',direction='lift')
        Label_16 = tkinter.Label(Form_1,text="")
        Fun.Register(uiName,'PyMe_Label_16',Label_16,'Label_1')
        Fun.SetControlPlace(uiName,'PyMe_Label_16',0.5958333333333333,0.15555555555555556,0.2708,0.5822,'nw',True,True)
        Label_16.configure(bg = "#FFFFFF")
        Label_16.configure(fg = "SystemButtonText")
        Fun.SetElementLayer(uiName,'Label_1',direction='lower')
        Label_18 = tkinter.Label(Form_1,text="")
        Fun.Register(uiName,'PyMe_Label_18',Label_18,'Label_2')
        Fun.SetControlPlace(uiName,'PyMe_Label_18',0.7188,0.0,0.28125,1.0,'nw',True,True)
        Label_18.configure(bg = "#2468F2")
        Label_18.configure(fg = "SystemButtonText")
        Fun.SetElementLayer(uiName,'Label_2',direction='lower')
        Timer_17 = Fun.Timer(1000,lambda:reset_pw_cmd.Timer_1_onTimer(uiName,"Form_1"))
        #Timer_17.xy(899,80)
        Fun.Register(uiName,'PyMe_Timer_17',Timer_17,'Timer_1')
        Timer_17.SetWidget(Form_1)
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
    Fun.RunApplication(reset_pw)
