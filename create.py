#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import create_cmd
import create_sty
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
class  create:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=create_cmd
        Fun.Register(uiName,'root',root)
        style = create_sty.SetupStyle(isTKroot)
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
        Fun.SetUIRootSize(uiName,1240,900)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="隧道设置\r")
        Fun.Register(uiName,'PyMe_Label_2',Label_2,'title')
        Fun.SetControlPlace(uiName,'PyMe_Label_2',0.03870967741935484,0.03222222222222222,0.15725806451612903,0.03111111111111111,'nw',True,True)
        Label_2.configure(bg = "#FFFFFF")
        Label_2.configure(fg = "SystemButtonText")
        Label_2.configure(anchor = "w")
        Label_2_Ft=tkinter.font.Font(family='微软雅黑', size=24,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_5 = tkinter.Label(Form_1,text="隧道名称")
        Fun.Register(uiName,'PyMe_Label_5',Label_5,'Label_2')
        Fun.SetControlPlace(uiName,'PyMe_Label_5',0.03870967741935484,0.24444444444444444,0.12903225806451613,0.02,'nw',True,True)
        Label_5.configure(bg = "#FFFFFF")
        Label_5.configure(fg = "SystemButtonText")
        Label_5.configure(anchor = "w")
        Label_5_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)
        Label_8 = tkinter.Label(Form_1,text="隧道类型")
        Fun.Register(uiName,'PyMe_Label_8',Label_8,'Label_4')
        Fun.SetControlPlace(uiName,'PyMe_Label_8',0.2709677419354839,0.24444444444444444,0.12903225806451613,0.02,'nw',True,True)
        Label_8.configure(bg = "#FFFFFF")
        Label_8.configure(fg = "SystemButtonText")
        Label_8.configure(anchor = "w")
        Label_8_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_8.configure(font = Label_8_Ft)
        Label_10 = tkinter.Label(Form_1,text="本地IP")
        Fun.Register(uiName,'PyMe_Label_10',Label_10,'Label_5')
        Fun.SetControlPlace(uiName,'PyMe_Label_10',0.03870967741935484,0.38,0.12903225806451613,0.02,'nw',True,True)
        Label_10.configure(bg = "#FFFFFF")
        Label_10.configure(fg = "SystemButtonText")
        Label_10.configure(anchor = "w")
        Label_10_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_10.configure(font = Label_10_Ft)
        Label_12 = tkinter.Label(Form_1,text="本地端口")
        Fun.Register(uiName,'PyMe_Label_12',Label_12,'Label_6')
        Fun.SetControlPlace(uiName,'PyMe_Label_12',0.2709677419354839,0.35555555555555557,0.08064516129032258,0.05333333333333334,'nw',True,True)
        Label_12.configure(bg = "#FFFFFF")
        Label_12.configure(fg = "SystemButtonText")
        Label_12.configure(anchor = "w")
        Label_12_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_12.configure(font = Label_12_Ft)
        Label_14 = tkinter.Label(Form_1,text="编辑隧道")
        Fun.Register(uiName,'PyMe_Label_14',Label_14,'title_type')
        Fun.SetControlPlace(uiName,'PyMe_Label_14',0.03870967741935484,0.12333333333333334,0.1620967741935484,0.05333333333333334,'nw',True,True)
        Label_14.configure(bg = "#FFFFFF")
        Label_14.configure(fg = "SystemButtonText")
        Label_14.configure(anchor = "w")
        Label_14_Ft=tkinter.font.Font(family='微软雅黑', size=24,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_14.configure(font = Label_14_Ft)
        Label_16 = tkinter.Label(Form_1,text="远程IP")
        Fun.Register(uiName,'PyMe_Label_16',Label_16,'Label_7')
        Fun.SetControlPlace(uiName,'PyMe_Label_16',0.03870967741935484,0.5155555555555555,0.12903225806451613,0.02,'nw',True,True)
        Label_16.configure(bg = "#FFFFFF")
        Label_16.configure(fg = "SystemButtonText")
        Label_16.configure(anchor = "w")
        Label_16_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_16.configure(font = Label_16_Ft)
        Label_18 = tkinter.Label(Form_1,text="远程端口")
        Fun.Register(uiName,'PyMe_Label_18',Label_18,'Label_8')
        Fun.SetControlPlace(uiName,'PyMe_Label_18',0.2709677419354839,0.5155555555555555,0.12903225806451613,0.02,'nw',True,True)
        Label_18.configure(bg = "#FFFFFF")
        Label_18.configure(fg = "SystemButtonText")
        Label_18.configure(anchor = "w")
        Label_18_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_18.configure(font = Label_18_Ft)
        Entry_6= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_6',Entry_6,'name')
        Entry_6.SetBGColor("#FFFFFF")
        Entry_6.SetFGColor("#000000")
        Entry_6_Font=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_6.SetFont(Entry_6_Font)
        Entry_6.SetTipText("留空则随机")
        Entry_6.SetTipFGColor("#888888")
        Entry_6.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_6',0.037096774193548385,0.2733333333333333,0.2161290322580645,0.05333333333333334,'nw',True,True)
        Entry_11= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_11',Entry_11,'local_ip')
        Entry_11.SetBGColor("#FFFFFF")
        Entry_11.SetFGColor("#000000")
        Entry_11_Font=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_11.SetFont(Entry_11_Font)
        Entry_11.SetTipText("不填默认127.0.0.1")
        Entry_11.SetTipFGColor("#888888")
        Entry_11.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_11',0.03870967741935484,0.4088888888888889,0.2161290322580645,0.05333333333333334,'nw',True,True)
        Entry_15= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_15',Entry_15,'local_port')
        Entry_15.SetBGColor("#FFFFFF")
        Entry_15.SetFGColor("#000000")
        Entry_15_Font=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_15.SetFont(Entry_15_Font)
        Entry_15.SetTipText("必填")
        Entry_15.SetTipFGColor("#888888")
        Entry_15.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_15',0.2709677419354839,0.4088888888888889,0.2161290322580645,0.05333333333333334,'nw',True,True)
        Entry_19= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'PyMe_Entry_19',Entry_19,'remote_port')
        Entry_19.SetBGColor("#FFFFFF")
        Entry_19.SetFGColor("#000000")
        Entry_19_Font=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_19.SetFont(Entry_19_Font)
        Entry_19.SetTipText("不填则默认随机")
        Entry_19.SetTipFGColor("#888888")
        Entry_19.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'PyMe_Entry_19',0.2701612903225806,0.5477777777777778,0.2161290322580645,0.05333333333333334,'nw',True,True)
        LabelButton_20= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_20',LabelButton_20,'create')
        LabelButton_20.SetText("创建隧道")
        LabelButton_20.SetBGColor("#FFFFFF")
        LabelButton_20.SetFGColor("#000000")
        LabelButton_20_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_20.SetFont(LabelButton_20_TitleFont)
        LabelButton_20.SetBGImage("Button.png")
        LabelButton_20.SetBGColor_Hover("#AAAAAA")
        LabelButton_20.SetFGColor_Hover("#4FC1E9")
        LabelButton_20.SetBGColor_Click("#AAAAAA")
        LabelButton_20.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_20',0.03870967741935484,0.6333333333333333,0.2161290322580645,0.05333333333333334,'nw',True,True)
        LabelButton_20.Redraw()
        LabelButton_20.SetCommandFunction(create_cmd.create_onCommand,self.uiName,"create")
        LabelButton_21= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_21',LabelButton_21,'range')
        LabelButton_21.SetText("随机远程端口")
        LabelButton_21.SetBGColor("#FFFFFF")
        LabelButton_21.SetFGColor("#000000")
        LabelButton_21_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_21.SetFont(LabelButton_21_TitleFont)
        LabelButton_21.SetBGImage("Button.png")
        LabelButton_21.SetBGColor_Hover("#AAAAAA")
        LabelButton_21.SetFGColor_Hover("#4FC1E9")
        LabelButton_21.SetBGColor_Click("#AAAAAA")
        LabelButton_21.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_21',0.2701612903225806,0.6333333333333333,0.2161290322580645,0.05333333333333334,'nw',True,True)
        LabelButton_21.Redraw()
        LabelButton_21.SetCommandFunction(create_cmd.range_onCommand,self.uiName,"range")
        LabelButton_22= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_22',LabelButton_22,'return')
        LabelButton_22.SetText("返回创建隧道界面")
        LabelButton_22.SetBGColor("#FFFFFF")
        LabelButton_22.SetFGColor("#000000")
        LabelButton_22_TitleFont=tkinter.font.Font(family='微软雅黑', size=24,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_22.SetFont(LabelButton_22_TitleFont)
        LabelButton_22.SetBGImage("Button.png")
        LabelButton_22.SetBGColor_Hover("#AAAAAA")
        LabelButton_22.SetFGColor_Hover("#4FC1E9")
        LabelButton_22.SetBGColor_Click("#AAAAAA")
        LabelButton_22.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_22',0.03951612903225806,0.8,0.4476,0.05333,'nw',True,True)
        LabelButton_22.Redraw()
        LabelButton_22.SetCommandFunction(create_cmd.return_onCommand,self.uiName,"return")
        LabelButton_24= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_24',LabelButton_24,'edit')
        LabelButton_24.SetText("修改隧道")
        LabelButton_24.SetBGColor("#FFFFFF")
        LabelButton_24.SetFGColor("#000000")
        LabelButton_24_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_24.SetFont(LabelButton_24_TitleFont)
        LabelButton_24.SetBGImage("Button.png")
        LabelButton_24.SetBGColor_Hover("#AAAAAA")
        LabelButton_24.SetFGColor_Hover("#000000")
        LabelButton_24.SetBGColor_Click("#AAAAAA")
        LabelButton_24.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_24',0.03870967741935484,0.6333333333333333,0.2161290322580645,0.05333333333333334,'nw',True,True)
        LabelButton_24.Redraw()
        LabelButton_24.SetCommandFunction(create_cmd.edit_onCommand,self.uiName,"edit")
        LabelButton_25= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_25',LabelButton_25,'delete')
        LabelButton_25.SetText("删除该隧道")
        LabelButton_25.SetBGColor("#FFFFFF")
        LabelButton_25.SetFGColor("#DA4453")
        LabelButton_25_TitleFont=tkinter.font.Font(family='微软雅黑', size=24,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_25.SetFont(LabelButton_25_TitleFont)
        LabelButton_25.SetBGImage("Button.png")
        LabelButton_25.SetBGColor_Hover("#AAAAAA")
        LabelButton_25.SetFGColor_Hover("#4FC1E9")
        LabelButton_25.SetBGColor_Click("#AAAAAA")
        LabelButton_25.SetFGColor_Click("#000000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_25',0.03951612903225806,0.7188888888888889,0.4475806451612903,0.05333333333333334,'nw',True,True)
        LabelButton_25.Redraw()
        LabelButton_25.SetCommandFunction(create_cmd.delete_onCommand,self.uiName,"delete")
        LabelButton_27= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_27',LabelButton_27,'select_port')
        LabelButton_27.SetText("选取本地端口")
        LabelButton_27.SetBGColor("#FFFFFF")
        LabelButton_27.SetFGColor("#000000")
        LabelButton_27_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_27.SetFont(LabelButton_27_TitleFont)
        LabelButton_27.SetBGImage("Button.png")
        LabelButton_27.SetBGColor_Hover("#AAAAAA")
        LabelButton_27.SetFGColor_Hover("#000000")
        LabelButton_27.SetBGColor_Click("#AAAAAA")
        LabelButton_27.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_27',0.4975806451612903,0.4811111111111111,0.125,0.05333333333333334,'nw',True,True)
        LabelButton_27.Redraw()
        LabelButton_27.SetCommandFunction(create_cmd.select_port_onCommand,self.uiName,"select_port")
        LabelButton_28= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'PyMe_LabelButton_28',LabelButton_28,'reload_port')
        LabelButton_28.SetText("刷新端口列表")
        LabelButton_28.SetBGColor("#FFFFFF")
        LabelButton_28.SetFGColor("#000000")
        LabelButton_28_TitleFont=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_28.SetFont(LabelButton_28_TitleFont)
        LabelButton_28.SetBGImage("Button.png")
        LabelButton_28.SetBGColor_Hover("#AAAAAA")
        LabelButton_28.SetFGColor_Hover("#000000")
        LabelButton_28.SetBGColor_Click("#AAAAAA")
        LabelButton_28.SetFGColor_Click("#FF0000")
        Fun.SetControlPlace(uiName,'PyMe_LabelButton_28',0.6306451612903226,0.4811111111111111,0.125,0.05333333333333334,'nw',True,True)
        LabelButton_28.Redraw()
        LabelButton_28.SetCommandFunction(create_cmd.reload_port_onCommand,self.uiName,"reload_port")
        ComboBox_23_Variable = Fun.AddTKVariable(uiName,'PyMe_ComboBox_23')
        ComboBox_23 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_23_Variable, state="normal",style="proxy_type.TCombobox")
        ComboBox_23_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_23.configure(font = ComboBox_23_Ft)
        Fun.Register(uiName,'PyMe_ComboBox_23',ComboBox_23,'proxy_type')
        Fun.SetControlPlace(uiName,'PyMe_ComboBox_23',0.2709677419354839,0.2733333333333333,0.2161290322580645,0.05333333333333334,'nw',True,True)
        ComboBox_23.configure(state = "readonly")
        ComboBox_23["values"]=['tcp','udp']
        ComboBox_23.current(0)
        ComboBox_26_Variable = Fun.AddTKVariable(uiName,'PyMe_ComboBox_26')
        ComboBox_26 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_26_Variable, state="normal",style="ComboBox_2.TCombobox")
        ComboBox_26_Ft=tkinter.font.Font(family='微软雅黑', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_26.configure(font = ComboBox_26_Ft)
        Fun.Register(uiName,'PyMe_ComboBox_26',ComboBox_26,'ComboBox_2')
        Fun.SetControlPlace(uiName,'PyMe_ComboBox_26',0.4975806451612903,0.4066666666666667,0.25806451612903225,0.05333333333333334,'nw',True,True)
        ComboBox_26.configure(state = "readonly")
        ComboBox_29_Variable = Fun.AddTKVariable(uiName,'PyMe_ComboBox_29')
        ComboBox_29 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_29_Variable, state="normal",style="remote_ip.TCombobox")
        ComboBox_29_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_29.configure(font = ComboBox_29_Ft)
        Fun.Register(uiName,'PyMe_ComboBox_29',ComboBox_29,'remote_ip')
        Fun.SetControlPlace(uiName,'PyMe_ComboBox_29',0.038700000000000005,0.5478000000000001,0.2161,0.05333333333333334,'nw',True,True)
        ComboBox_29.configure(state = "readonly")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",create_cmd.Form_1_onLoad)
        #Add Some Logic Code Here: (Keep This Line of comments)
        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
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
    Fun.RunApplication(create)