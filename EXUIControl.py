# 版权声明：日历控件参考CSDN博主「我的眼_001」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原作者出处链接及声明
# 原文链接：https://blog.csdn.net/wodeyan001/article/details/86703034
# -*- coding: utf-8 -*- 
import os
import tkinter
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
from   functools import partial
import win32gui
G_ExeDir = None
G_ResDir = None
FunLib = None
SCALE_FACTOR = 1.5
def EventFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(event, **params)
#图片按钮
class LabelButton:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.MenuArray = []
        self.Text = 'LabelButton'
        self.BGColor = '#333333'
        self.FGColor = '#FFFFFF'
        self.Font = None 
        self.Image = None
        self.ImageFile = None
        self.BGColor_Hover = None
        self.FGColor_Hover = None
        self.Font_Hover = None 
        self.Image_Hover = None
        self.ImageFile_Hover = None
        self.BGColor_Click = None
        self.FGColor_Click = None
        self.Font_Click = None 
        self.Image_Click = None
        self.ImageFile_Click = None
        self.LabelWidth = 100
        self.LabelHeight = 24
        self.commandFunction = None
        self.uiName = None
        self.widgetName = None
        self.Anchor = "center"
        self.State = "normal"
        self.Relief = "flat"
        self.Label = tkinter.Label(self.ParentWidget,text=self.Text,width=self.LabelWidth,height=self.LabelHeight,bg = self.BGColor,highlightthickness=0,bd=0)
        self.Label.place(x=0, y=0,width=self.LabelWidth,height=self.LabelHeight)
        self.Label.bind('<Configure>',self.Configure)
        self.Label.bind('<Enter>',self.onEnter)
        self.Label.bind('<Leave>',self.onLeave)
        self.Label.bind('<Button-1>',self.onClick)
        self.Label.bind('<ButtonRelease-1>',self.onEnter)
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Label.pack_forget()
        elif layout == "grid":
            self.Label.grid_forget()
        else:
            self.Label.place_forget()
    #鼠标进入时的处理
    def onEnter(self,event):
        if self.State == "normal":
            event.widget.configure(cursor='hand2')
            if self.Image_Hover:
                event.widget.configure(image = self.Image_Hover,compound='center')
            if self.BGColor_Hover:
                event.widget.configure(bg = self.BGColor_Hover)
            if self.FGColor_Hover:
                event.widget.configure(fg = self.FGColor_Hover)
            if self.Font_Hover:
                event.widget.configure(font = self.Font_Hover)
            event.widget.update()
    #鼠标离开时的处理
    def onLeave(self,event):
        if self.State == "normal":
            event.widget.configure(cursor='arrow')
            if self.Image:
                event.widget.configure(image = self.Image,compound='center')
            if self.BGColor:
                event.widget.configure(bg = self.BGColor)
            if self.FGColor:
                event.widget.configure(fg = self.FGColor)
            if self.Font:
                event.widget.configure(font = self.Font)
            event.widget.update()
    #鼠标按下时的处理
    def onClick(self,event):
        if self.State == "normal":
            event.widget.configure(cursor='hand2')
            if self.Image_Click:
                event.widget.configure(image = self.Image_Click,compound='center')
            if self.BGColor_Click:
                event.widget.configure(bg = self.BGColor_Click)
            if self.FGColor_Click:
                event.widget.configure(fg = self.FGColor_Click)
            if self.Font_Click:
                event.widget.configure(font = self.Font_Click)
            event.widget.update()
            if self.commandFunction:
                self.commandFunction(self.uiName,self.widgetName)
    #设置点击事件回调处理
    def SetCommandFunction(self,Func,uiName,widgetName):
        self.commandFunction = Func
        self.uiName = uiName
        self.widgetName = widgetName
    #取得当前画布
    def GetWidget(self):
        return self.Label
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Label:
            self.Label.bind(EventName,callBack)
    #窗口大小变化
    def Configure(self,event):
        self.Redraw()
    #设置属性
    def configure(self,**kw):
        try:
           self.Label.configure(kw)
        except:
           pass
    #隐藏(兼容原Text控件)
    def pack_forget(self):
        return self.Label.pack_forget()
    #隐藏(兼容原Text控件)
    def grid_forget(self):
        return self.Label.grid_forget()
    #隐藏(兼容原Text控件)
    def place_forget(self):
        return self.Label.place_forget()
    #设置文字内容
    def SetText(self,text):
        self.Text = text
        if self.Label:
            self.Label.configure(text = self.Text)
    #取得文字内容
    def GetText(self):
        return self.Text
    #设置文字对齐
    def SetAnchor(self,anchor):
        self.Anchor = anchor
        if self.Label:
            self.Label.configure(anchor = self.Anchor)
    #取得文字对齐
    def GetAnchor(self):
        return self.Anchor
    #设置当前是否可用
    def SetState(self,state):
        self.State = state
        if self.Label:
            self.Label.configure(state = self.State)
    #取得是否可用
    def GetState(self):
        return self.State
    #设置边框样式
    def SetRelief(self,relief):
        self.Relief = relief
        if self.Label:
            self.Label.configure(relief = self.Relief)
    #取得边框样式
    def GetRelief(self):
        return self.Relief
    #设置当前画布的背景色
    def SetBGColor(self,color):
        self.BGColor = color
        if self.Label:
            self.Label.configure(bg = self.BGColor)
    #取得当前画布的背景色
    def GetBGColor(self):
        return self.BGColor
    #设置标题栏的文字色
    def SetFGColor(self,color):
        self.FGColor = color
        if self.Label:
            self.Label.configure(fg = self.FGColor)
    #取得标题栏的文字色
    def GetFGColor(self):
        return self.FGColor
    #设置标题栏的字体
    def SetFont(self,font):
        self.Font = font
        if self.Label:
            self.Label.configure(font = self.Font)
    #取得标题栏的字体
    def GetFont(self):
        return self.Font
    #设置标题栏的字体
    def SetBGImage(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.Image = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile = filePath
                if self.Label:
                    self.Label.configure(image = self.Image,compound='center')
            except:
                self.Image = None
    #取得标题栏的图片文件
    def GetBGImageFile(self):
        return self.ImageFile
    #设置鼠标悬停在标题栏时的背景色
    def SetBGColor_Hover(self,color):
        self.BGColor_Hover = color
    #取得鼠标悬停在标题栏时背景色
    def GetBGColor_Hover(self):
        return self.BGColor_Hover
    #设置鼠标悬停在标题栏时的文字色
    def SetFGColor_Hover(self,color):
        self.FGColor_Hover = color
    #取得鼠标悬停在标题栏时文字色
    def GetFGColor_Hover(self):
        return self.FGColor_Hover
    #设置标题栏的字体
    def SetFont_Hover(self,font):
        self.Font_Hover = font
    #取得标题栏的字体
    def GetFont_Hover(self):
        return self.Font_Hover
    #设置标题栏的字体
    def SetBGImage_Hover(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ImageFile_Hover = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image_Hover = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile_Hover = filePath
            except:
                self.Image_Hover = None
    #取得标题栏的图片文件
    def GetBGImageFile_Hover(self):
        return self.ImageFile_Hover
    #设置鼠标按下标题栏时的背景色
    def SetBGColor_Click(self,color):
        self.BGColor_Click = color
        for subMenu in self.MenuArray:
            Button = subMenu[4]
            Button.configure(activebackground = self.BGColor_Click)
    #取得鼠标按下标题栏时背景色
    def GetBGColor_Click(self):
        return self.BGColor_Click
    #设置鼠标按下标题栏时的文字色
    def SetFGColor_Click(self,color):
        self.FGColor_Click = color
        for subMenu in self.MenuArray:
            Button = subMenu[4]
            Button.configure(activeforeground = self.FGColor_Click)
    #取得鼠标按下标题栏时文字色
    def GetFGColor_Click(self):
        return self.FGColor_Click
    #设置鼠标按下标题栏时字体
    def SetFont_Click(self,font):
        self.Font_Click = font
    #取得鼠标按下标题栏时字体
    def GetFont_Click(self):
        return self.Font_Click
    #设置标题栏的字体
    def SetBGImage_Click(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ImageFile_Click = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image_Click = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile_Click = filePath
            except:
                self.Image_Click = None
    #取得标题栏的图片文件
    def GetBGImageFile_Click(self):
        return self.ImageFile_Click
    #展开
    def Redraw(self):
        self.LabelWidth = self.Label.winfo_width()
        self.LabelHeight = self.Label.winfo_height()
        if self.LabelWidth == 1 and self.LabelHeight == 1:
            self.LabelHeight = 100
            self.LabelHeight = 24
        if self.ImageFile and os.path.exists(self.ImageFile) == True:
            if self.Image.width() != self.LabelWidth or self.Image.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image = ImageTk.PhotoImage(Image_Resize)
                    if self.Label:
                        self.Label.configure(image = self.Image)
                except:
                    self.Image = None
        if self.ImageFile_Hover and os.path.exists(self.ImageFile_Hover) == True:
            if self.Image_Hover.width() != self.LabelWidth or self.Image_Hover.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile_Hover).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image_Hover = ImageTk.PhotoImage(Image_Resize)
                except:
                    self.Image_Hover = None
        if self.ImageFile_Click and os.path.exists(self.ImageFile_Click) == True:
            if self.Image_Click.width() != self.LabelWidth or self.Image_Click.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile_Click).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image_Click = ImageTk.PhotoImage(Image_Resize)
                except:
                    self.Image_Click = None
        if self.Label:
            self.Label.configure(fg = self.FGColor)
#圆角编辑框 
class CustomEntry:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.EntryValue = tkinter.StringVar()
        self.EntryValue.set('')
        self.Canvas_width = 100
        self.Canvas_height = 24
        self.Canvas = tkinter.Canvas(self.ParentWidget,width=self.Canvas_width,height=self.Canvas_height,bg = '#FFFFFF',highlightthickness=0,bd=0)
        self.Entry = tkinter.Entry(self.Canvas,textvariable=self.EntryValue,background='#FFFFFF')
        self.Font = tkinter.font.Font(font='TkDefaultFont')
        self.TipText = ''
        self.TipTextColor = '#777777'
        self.TipLabel = tkinter.Label(self.Entry, text = '', justify = 'left',anchor=tkinter.W,bg='#FFFFFF')
        self.TipLabel.configure(fg = self.TipTextColor)
        self.TipLabel.bind('<Button-1>',self.onLeftClickTip)
        self.TipLabel.bind('<B1-Motion>',self.onLeftMotionTip)
        self.TipLabel.bind('<ButtonRelease-1>',self.onLeftReleaseTip)
        self.TipLabel.bind('<Double-1>',self.onDoubleClickTip)
        self.TipLabel.bind('<Button-3>',self.onRightClickTip)
        self.Entry.bind('<FocusOut>',self.onResetTip)
        self.Canvas.bind('<Configure>',self.Configure)
        self.LeftIconImage = None
        self.LeftPhotoIconImage = None
        self.LeftIconImageFile = None
        self.LeftIconClickedFunction = None
        self.RightIconImage = None
        self.RightPhotoIconImage = None
        self.RightIconImageFile = None
        self.RightIconClickedFunction = None
        self.TextChangedFunction = None
        self.uiName = None
        self.widgetName = None
        self.RoundRadius = 0
        self.Restriction = ''
        self.InnerSpacingX = 0
        self.InnerSpacingY = 0
    #取得当前编辑框宽度
    def GetWidth(self):
        return self.Canvas.winfo_width()
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Entry:
            self.Entry.bind(EventName,callBack)
    #取得当前编辑框高度
    def GetHeight(self):
        return self.Canvas.winfo_height()
    #取得Canvas
    def GetWidget(self):
        return self.Canvas
    #取得Entry
    def GetEntry(self):
        return self.Entry
    #窗口大小变化
    def Configure(self,event):
        self.Rebuild()
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Canvas.pack_forget()
        elif layout == "grid":
            self.Canvas.grid_forget()
        else:
            self.Canvas.place_forget()
    #重载一下cget
    def cget(self,attrib):
        return self.Entry.cget(attrib)
    #设置属性
    def configure(self,**kw):
        if 'text' in kw:
            self.SetText(kw['text'])
        else:
            try:
               self.Entry.configure(kw)
            except:
               pass
    #设置焦点
    def focus_set(self):
        return self.Entry.focus_set()
    #隐藏(兼容原Text控件)
    def pack_forget(self):
        return self.Canvas.pack_forget()
    #隐藏(兼容原Text控件)
    def grid_forget(self):
        return self.Canvas.grid_forget()
    #隐藏(兼容原Text控件)
    def place_forget(self):
        return self.Canvas.place_forget()
    #鼠标进入和离开图标时的处理
    def onIconEnter(self,event):
        event.widget.configure(cursor='hand2')
    def onIconLeave(self,event):    
        event.widget.configure(cursor='arrow')
    def onIconClick(self,event,tagName):  
        print("Click " + tagName)
        if tagName == "left_icon":
            if self.LeftIconClickedFunction:
                self.LeftIconClickedFunction(self.uiName,self.widgetName)
        else:
            if self.RightIconClickedFunction:
                self.RightIconClickedFunction(self.uiName,self.widgetName)
    #鼠标左键单击
    def onLeftClickTip(self,event):
        self.TipLabel.place_forget()
        self.Entry.focus_set()
    #鼠标左键拖动Tip
    def onLeftMotionTip(self,event):
        self.TipLabel.place_forget()
        self.Entry.focus_set()
    #鼠标左键松开Tip
    def onLeftReleaseTip(self,event):
        self.TipLabel.place_forget()
        self.Entry.focus_set()
    #鼠标左键双击Tip
    def onDoubleClickTip(self,event):
        pass
    #鼠标右键单击
    def onRightClickTip(self,event):
        self.TipLabel.place_forget()
        self.Entry.focus_set()
        self.Entry.event_generate("<Button-3>",x = event.x,y = event.y)
    #点击Tiip
    def onResetTip(self,event):
        text =  self.EntryValue.get()
        if text == '':
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
    #设置左边的图标按钮
    def SetLeftIcon(self,IconFile):
        global G_ExeDir
        global G_ResDir
        filePath = IconFile
        if IconFile:
            if filePath and os.path.exists(filePath) == False:
                 filePath = "Resources\\" + IconFile
                 if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,IconFile)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,IconFile)
            if filePath and os.path.exists(filePath) == True:
                imagePath,imageFile = os.path.split(filePath)
                try:
                    self.LeftIconImage = Image.open(filePath).convert('RGBA')
                    IconSize = self.GetHeight() - 2 * self.InnerSpacingY
                    Image_Resize = self.LeftIconImage.resize((IconSize, IconSize),Image.LANCZOS)
                    self.LeftPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
                    self.LeftIconImageFile = imageFile
                except:
                    self.LeftIconImage = None
                    self.LeftPhotoIconImage = None
                    self.LeftIconImageFile = None
        self.Redraw()
    #设置左边的图标按钮回调函数
    def SetLeftIconClickFunction(self,callBackFunc,uiName,widgetName):
        self.LeftIconClickedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.Canvas.tag_bind('left_icon','<Enter>',self.onIconEnter)
        self.Canvas.tag_bind('left_icon','<Leave>',self.onIconLeave)
        self.Canvas.tag_bind('left_icon','<ButtonRelease-1>',EventFunction_Adaptor(self.onIconClick,tagName='left_icon'))
    #设置右边的图标按钮
    def SetRightIcon(self,IconFile):
        global G_ExeDir
        global G_ResDir
        filePath = IconFile
        if IconFile:
            if filePath and os.path.exists(filePath) == False:
                filePath = "Resources\\" + IconFile
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,IconFile)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,IconFile)
            if filePath and os.path.exists(filePath) == True:
                imagePath,imageFile = os.path.split(filePath)
                try:
                    self.RightIconImage = Image.open(filePath).convert('RGBA')
                    IconSize = self.GetHeight() - 2 * self.InnerSpacingY
                    Image_Resize = self.RightIconImage.resize((IconSize, IconSize),Image.LANCZOS)
                    self.RightPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
                    self.RightIconImageFile = imageFile
                except:
                    self.RightIconImage = None
                    self.RightPhotoIconImage = None
                    self.RightIconImageFile = None
        self.Redraw()
    #设置左边的图标按钮回调函数
    def SetRightIconClickFunction(self,callBackFunc,uiName,widgetName):
        self.RightIconClickedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.Canvas.tag_bind('right_icon','<Enter>',self.onIconEnter)
        self.Canvas.tag_bind('right_icon','<Leave>',self.onIconLeave)
        self.Canvas.tag_bind('right_icon','<ButtonRelease-1>',EventFunction_Adaptor(self.onIconClick,tagName='right_icon'))
    #内置的输入文本被修改时的回调函数
    def onTextChangedCallBack(self,*args):
        if self.TextChangedFunction:
            Text = self.EntryValue.get()
            print("TextChanged:"+Text)
            self.TextChangedFunction(self.uiName,self.widgetName,Text)
    #设置输入文本被修改时的回调函数
    def SetTextChangedFunction(self,callBackFunc,uiName,widgetName):
        self.TextChangedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.EntryValue.trace('w',self.onTextChangedCallBack)
    #设置边角半径
    def SetRoundRadius(self,radius):
        self.RoundRadius = radius
        w = self.GetWidth()
        h = self.GetHeight()
        if radius > 0 and w > 1 and h > 1:
            HRGN = win32gui.CreateRoundRectRgn(0,0,w,h,radius,radius)
            win32gui.SetWindowRgn(self.Canvas.winfo_id(), HRGN,1)
    #取得边角半径
    def GetRoundRadius(self):
        return self.RoundRadius
    #设置类型限制
    def SetRestriction(self,restriction):
        self.Restriction = restriction
    #取得类型限制
    def GetRestriction(self):
        return self.Restriction
    #设置横向间距
    def SetInnerSpacingX(self,InnerSpacingX):
        self.InnerSpacingX = InnerSpacingX
    #取得横向间距
    def GetInnerSpacingX(self):
        return self.InnerSpacingX
    #设置纵向间距
    def SetInnerSpacingY(self,InnerSpacingY):
        self.InnerSpacingY = InnerSpacingY
    #取得纵向间距
    def GetInnerSpacingY(self):
        return self.InnerSpacingY
    #设置文字
    def SetText(self,text):
        if text != "":
            self.TipLabel.place_forget()
        else:
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
        self.EntryValue.set(text)
    #取得文字
    def GetText(self):
        text =  self.EntryValue.get()
        if text != "":
            if hasattr(FunLib,"GetElementName") == True:
                uiName,elementName = FunLib.GetElementName(self)
                if self.Restriction == "letter":
                    if text.isalpha() == False:
                        FunLib.MessageBox(elementName+"请输入字母","类型限制")
                        return None
                if self.Restriction == "number":
                    if FunLib.IsNumeric(text) == False:
                        FunLib.MessageBox(elementName+"请输入数字","类型限制")
                        return None
                if self.Restriction == "integer":
                    if FunLib.IsInt(text) == False:
                        FunLib.MessageBox(elementName+"请输入整数","类型限制")
                        return None
                if self.Restriction == "phone":
                    if FunLib.IsMobilePhone(text) == False:
                        FunLib.MessageBox(elementName+"请输入手机号码","类型限制")
                        return None
                if self.Restriction == "email":
                    if FunLib.IsEmail(text) == False:
                        FunLib.MessageBox(elementName+"请输入电子邮件","类型限制")
                        return None
        return text
    #设置字体
    def SetFont(self,font):
        self.Font = font
        self.Entry.configure(font = self.Font)
        self.TipLabel.configure(font = self.Font)
    #取得字体
    def GetFont(self):
        return self.Font
    #设置提示文字
    def SetTipText(self,text):
        self.TipText = text
        if text != '':
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
            self.TipLabel.configure(bg = self.GetBGColor())
            self.TipLabel.configure(fg = self.TipTextColor)
            self.TipLabel.configure(text = self.TipText)
        else:
            self.TipLabel.place_forget()
    #取得提示文字
    def GetTipText(self):
        return self.TipText
    #设置提示文字颜色
    def SetTipFGColor(self,color):
        self.TipTextColor = color
        self.TipLabel.configure(fg=color)
    #取得提示文字颜色
    def GetTipFGColor(self):
        return self.TipTextColor
    #设置背景色
    def SetBGColor(self,bgColor):
        self.Entry.configure(bg = bgColor)
        self.TipLabel.configure(bg = bgColor)
    #取得背景色
    def GetBGColor(self):
        return self.Entry.cget('bg')
    #设置文字色
    def SetFGColor(self,fgColor):
        self.Entry.configure(fg = fgColor)
    #取得文字色
    def GetFGColor(self):
        return self.Entry.cget('fg')
    #设置只读状态的背景色
    def SetBGColor_ReadOnly(self,bgColor):
        self.Entry.configure(readonlybackground = bgColor)
    #取得只读状态的背景色
    def GetBGColor_ReadOnly(self):
        return self.Entry.cget('readonlybackground')
    #设置替代符
    def SetShowChar(self,showChar):
        self.Entry.configure(show = showChar)
    #取得替代符
    def GetShowChar(self):
        return self.Entry.cget('show')
    #设置对齐方式
    def SetJustify(self,justify):
        self.Entry.configure(justify = justify)
    #取得对齐方式
    def GetJustify(self):
        return self.Entry.cget('justify')
    #设置样式
    def SetRelief(self,relief):
        self.Entry.configure(relief = relief)
    #取得样式
    def GetRelief(self):
        return self.Entry.cget('relief')
    #设置状态
    def SetState(self,state):
        self.Entry.configure(state = state)
    #取得状态
    def GetState(self):
        return self.Entry.cget('state')
    #重置
    def Rebuild(self):
        if self.RoundRadius > 0:
            self.SetRoundRadius(self.RoundRadius)
        IconSize = self.GetHeight()
        if self.LeftIconImage:
            Image_Resize = self.LeftIconImage.resize((IconSize, IconSize),Image.LANCZOS)
            self.LeftPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
        if self.RightIconImage:
            Image_Resize = self.RightIconImage.resize((IconSize, IconSize),Image.LANCZOS)
            self.RightPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
        self.Redraw()
    #重绘
    def Redraw(self):
        AllWidth = self.GetWidth()
        IconWidth = self.GetHeight()
        if AllWidth == 1 or IconWidth == 1:
            AllWidth = 160
            IconWidth = 24
        EntryWidth = AllWidth
        EntryLeft = 0
        #左图标
        if self.LeftPhotoIconImage:
            self.Canvas.create_image(self.InnerSpacingX,self.InnerSpacingY,anchor=tkinter.NW,image=self.LeftPhotoIconImage,tag="left_icon")
            EntryWidth = EntryWidth - 2 * self.InnerSpacingX - IconWidth
            EntryLeft = 2 * self.InnerSpacingX + IconWidth
        #左图标
        if self.RightPhotoIconImage:
            self.Canvas.create_image(AllWidth - self.InnerSpacingX,self.InnerSpacingY,anchor=tkinter.NE,image=self.RightPhotoIconImage,tag="right_icon")
            EntryWidth = EntryWidth - 2 * self.InnerSpacingX - IconWidth
        self.Entry.place(x = EntryLeft , y = 0 , width = EntryWidth ,height=IconWidth)
        if self.GetText() == '' and self.TipText != '':
            self.TipLabel.place(x=0,y=0,width=EntryWidth,height=IconWidth)
#圆角编辑框 
class CustomText:
    def __init__(self, widget ,autowrap = None):
        self.ParentWidget = widget
        self.Canvas_width = 400
        self.Canvas_height = 200
        self.Canvas = tkinter.Canvas(self.ParentWidget,width=self.Canvas_width,height=self.Canvas_height,bg = '#FFFFFF',highlightthickness=0,bd=0)
        if autowrap is True:
            self.Text = tkinter.Text(self.Canvas,background='#FFFFFF',undo=True,wrap=tkinter.WORD)
        elif autowrap is False:
            self.Text = tkinter.Text(self.Canvas,background='#FFFFFF',undo=True,wrap=tkinter.NONE)
        else:
            self.Text = tkinter.Text(self.ParentWidget,background='#FFFFFF',undo=True)
        self.Text.place(x=0, y=0,width=self.Canvas_width,height=self.Canvas_height)
        self.yview = self.Text.yview
        self.Font = tkinter.font.Font(font='TkDefaultFont')
        self.Canvas.bind('<Configure>',self.Configure)
        self.HScrollbar = None
        self.HScrollbar_Visible = False
        self.VScrollbar = None
        self.VScrollbar_Visible = False
        self.uiName = None
        self.widgetName = None
    #取得当前编辑框宽度
    def GetWidth(self):
        return self.Canvas.winfo_width()
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Text:
            self.Text.bind(EventName,callBack)
    #取得当前编辑框高度
    def GetHeight(self):
        return self.Canvas.winfo_height()
    #取得Canvas
    def GetWidget(self):
        return self.Canvas
    #取得Text
    def GetEntry(self):
        return self.Text
    #窗口大小变化
    def Configure(self,event):
        self.Rebuild()
    #Text移动到相应位置
    def moveto(self,yview):
        if self.Text:
            self.Text.yview.moveto(yview)
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Canvas.pack_forget()
        elif layout == "grid":
            self.Canvas.grid_forget()
        else:
            self.Canvas.place_forget()
    #重载一下cget
    def cget(self,attrib):
        return self.Text.cget(attrib)
    #定位当前光标位置
    def see(self,position):
        return self.Text.see(position)
    #设置当前处于焦点
    def focus_set(self):
        return self.Text.focus_set()
    #清空缓冲(兼容原Text控件)
    def edit_reset(self):
        return self.Text.edit_reset()
    #隐藏(兼容原Text控件)
    def pack_forget(self):
        return self.Canvas.pack_forget()
    #隐藏(兼容原Text控件)
    def grid_forget(self):
        return self.Canvas.grid_forget()
    #隐藏(兼容原Text控件)
    def place_forget(self):
        return self.Canvas.place_forget()
    #清空缓冲
    def ClearCache(self):
        return self.Text.edit_reset()
    #设置属性
    def configure(self,**kw):
        if 'text' in kw:
            self.SetText(kw['text'])
        else:
            try:
               self.Text.configure(kw)
            except:
               pass
    #设置焦点
    def focus_set(self):
        return self.Text.focus_set()
    #设置文字
    def SetText(self,text):
        self.Text.delete('0.0', tkinter.END)
        self.Text.insert(tkinter.END,text)
    #取得文字
    def GetText(self):
        return self.Text.get('0.0', tkinter.END)
    #退格
    def BackSpace(self):
        self.Text.delete('insert-1c', 'insert')
    #设置字体
    def SetFont(self,font):
        self.Font = font
        self.Text.configure(font = self.Font)
    #取得字体
    def GetFont(self):
        return self.Font
    #设置背景色
    def SetBGColor(self,bgColor):
        self.Text.configure(bg = bgColor)
    #取得背景色
    def GetBGColor(self):
        return self.Text.cget('bg')
    #设置文字色
    def SetFGColor(self,fgColor):
        self.Text.configure(fg = fgColor)
    #取得文字色
    def GetFGColor(self):
        return self.Text.cget('fg')
    #设置样式
    def SetRelief(self,relief):
        self.Text.configure(relief = relief)
    #取得样式
    def GetRelief(self):
        return self.Text.cget('relief')
    #设置状态
    def SetState(self,state):
        self.Text.configure(state = state)
    #取得状态
    def GetState(self):
        return self.Text.cget('state')
    #设置标记状态
    def tag_config(self,tag,**kw):
        self.Text.tag_config(tag,kw)
    #取得属性
    def cget(self,attrib):
        return self.Text.cget(attrib)
    #设置属性
    def configure(self,**kw):
        self.Text.configure(kw)
    #使用横向滚动条
    def SetHScrollBar(self):
        if self.HScrollbar is None:
            self.HScrollbar = tkinter.ttk.Scrollbar(self.Canvas,orient=tkinter.HORIZONTAL)
        CanvasWidth = self.GetWidth()
        CanvasHeight = self.GetHeight()
        self.Text.place(height = CanvasHeight-20)
        if self.VScrollbar_Visible:
            self.HScrollbar.place(x = 0,y = CanvasHeight-20,width = CanvasWidth-20,height = 20)
        else:
            self.HScrollbar.place(x = 0,y = CanvasHeight-20,width = CanvasWidth,height = 20)
        self.HScrollbar.config(command = self.Text.xview)
        self.Text.config(xscrollcommand = self.HScrollbar.set)
        self.HScrollbar_Visible = True
    #不使用横向滚动条
    def RemoveHScrollBar(self):
        if self.HScrollbar:
            CanvasWidth = self.GetWidth()
            CanvasHeight = self.GetHeight()
            self.Text.place(height = CanvasHeight)
            self.HScrollbar.place_forget()
            self.HScrollbar.config(command = None)
            self.Text.config(xscrollcommand = None)
            self.HScrollbar_Visible = False
    #使用纵向滚动条
    def SetVScrollBar(self):
        if self.VScrollbar is None:
            self.VScrollbar = tkinter.ttk.Scrollbar(self.Canvas,orient=tkinter.VERTICAL)
        CanvasWidth = self.GetWidth()
        CanvasHeight = self.GetHeight()
        self.Text.place(width = CanvasWidth - 20)
        self.VScrollbar.place(x = CanvasWidth - 20,y = 0,width = 20,height = CanvasHeight)
        self.VScrollbar.config(command = self.Text.yview)
        self.Text.config(yscrollcommand = self.VScrollbar.set)
        self.VScrollbar_Visible = True
    #不使用纵向滚动条
    def RemoveVScrollBar(self):
        if self.VScrollbar:
            CanvasWidth = self.GetWidth()
            CanvasHeight = self.GetHeight()
            self.Text.place(width = CanvasWidth)
            self.VScrollbar.place_forget()
            self.VScrollbar.config(command = None)
            self.Text.config(yscrollcommand = None)
            self.VScrollbar_Visible = False
    #重置
    def Rebuild(self):
        self.Redraw()
    #重绘
    def Redraw(self):
        CanvasWidth = self.GetWidth()
        CanvasHeight = self.GetHeight()
        if self.HScrollbar_Visible and self.VScrollbar_Visible:
            self.SetHScrollBar()
            self.SetVScrollBar()
            CanvasWidth = CanvasWidth - 20
            CanvasHeight = CanvasHeight - 20
        elif self.HScrollbar_Visible:
            self.SetHScrollBar()
            CanvasHeight = CanvasHeight - 20
        elif self.VScrollbar_Visible:
            self.SetVScrollBar()
            CanvasWidth = CanvasWidth - 20
        self.Text.place(x = 0, y = 0,width = CanvasWidth,height=CanvasHeight)
#导航橱窗
class SwitchPage:
    def __init__(self, canvas):
        self.ParentCanvas = canvas
        self.ItemArray = []
        self.SwitchDelay = 4000
        self.CurrentIndex = -1
        self.BarButtonRadius = 6
        self.BarButtonSpacingX = 6
        self.BarButtonSpacingY = 2
        self.BarCurrButtonWidth = 15
        self.BarLeft = 200
        self.BarTop = -40
        self.TitleFont = tkinter.font.Font(family="Arial", size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        self.TitleLeft = 0
        self.TitleTop = 0
        self.MouseEnter = False
        self.TitleColor = '#FFFFFF'
        self.PageClickCallBackFunction = None
        self.uiName = None
        self.widgetName = None
        self.Canvas_width = 350
        self.Canvas_height = 200
        self.Canvas_BGColor = '#FFFFFF'
        self.Canvas = tkinter.Canvas(self.ParentCanvas,width=self.Canvas_width,height=self.Canvas_height,bg = self.Canvas_BGColor ,highlightthickness=0,bd=0)
        self.Canvas.pack(expand=1, fill='both')
        self.Canvas.bind('<Configure>',self.Configure)
    #取得当前画布
    def GetWidget(self):
        return self.Canvas
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Canvas:
            self.Canvas.bind(EventName,callBack)
    #窗口大小变化
    def Configure(self,event):
        self.Canvas_width = event.width
        self.Canvas_height = event.height
        self.Rebuild()
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Canvas.pack_forget()
        elif layout == "grid":
            self.Canvas.grid_forget()
        else:
            self.Canvas.place_forget()
    #传递pack_forget事件
    def pack_forget(self):
        if self.Canvas:
            self.Canvas.pack_forget()
    #传递grid_forget事件
    def grid_forget(self):
        if self.Canvas:
            self.Canvas.grid_forget()
    #传递place_forget事件
    def place_forget(self):
        if self.Canvas:
            self.Canvas.place_forget()
    #设置当前画布的背景色
    def SetBGColor(self,color):
        self.Canvas_BGColor = color
        self.Canvas.configure(bg = self.Canvas_BGColor)
    #取得当前画布的背景色
    def GetBGColor(self):
        return self.Canvas_BGColor
    #设置当前选中页
    def SetCurrentIndex(self,index):
        PageCount = len(self.ItemArray)
        if PageCount > index and index <= 0:
            self.CurrentIndex = index
        self.Redraw()
    #取得当前选中页
    def GetCurrentIndex(self):
        return self.CurrentIndex
    #鼠标进入和离开时的处理
    def onItemEnter(self,event):
        event.widget.configure(cursor='hand2')
        self.MouseEnter = True
    #鼠标离开时的处理
    def onItemLeave(self,event):    
        event.widget.configure(cursor='arrow')
        self.MouseEnter = False
    #鼠标点击时的处理
    def onItemClick(self,event):    
        ButtonInfo = self.ItemArray[self.CurrentIndex]
        if self.PageClickCallBackFunction:
            self.PageClickCallBackFunction(self.uiName,self.widgetName,self.CurrentIndex,ButtonInfo[0],ButtonInfo[2])
    #鼠标点击圆点时的处理
    def onPointClick(self,event,pageIndex):
        self.CurrentIndex = pageIndex
        self.Redraw()
    #上一页
    def goLast(self,event):
        PageCount = len(self.ItemArray)
        if PageCount > 0:
            self.CurrentIndex = self.CurrentIndex - 1 + PageCount
            self.CurrentIndex = self.CurrentIndex % PageCount
        self.Redraw()
    #下一页
    def goNext(self,event):
        PageCount = len(self.ItemArray)
        if PageCount > 0:
            self.CurrentIndex = self.CurrentIndex + 1
            self.CurrentIndex = self.CurrentIndex % PageCount
        self.Redraw()
    #取得菜单数据数组
    def GetItemArray(self):
        return self.ItemArray
    #取得菜单数据数组的复制
    def GetItemArray_Copy(self):
        ItemArray = []
        for ButtonInfo in self.ItemArray:
            ItemArray.append([ButtonInfo[0],ButtonInfo[1],ButtonInfo[2]])
        return ItemArray
    #清空所有
    def Clear(self):
        self.Canvas.delete("all")
        self.ItemArray.clear()
        self.CurrentIndex = -1
    #设置标题文字的左边位置
    def SetTitleLeft(self,left):
        self.TitleLeft = left
    #取得标题文字的左边位置
    def GetTitleLeft(self):
        return self.TitleLeft
    #设置标题文字的上部位置
    def SetTitleTop(self,top):
        self.TitleTop = top
    #取得标题文字的上部位置
    def GetTitleTop(self):
        return self.TitleTop
    #设置标题文字的颜色
    def SetTitleColor(self,color):
        self.TitleColor = color
    #取得标题文字的颜色
    def GetTitleColor(self):
        return self.TitleColor
    #设置当前进度条的X值
    def SetProgressBarLeft(self,left):
        self.BarLeft = int(left)
    #取得当前进度条的X值
    def GetProgressBarLeft(self):
        return self.BarLeft
    #设置当前进度条的Y值
    def SetProgressBarTop(self,top):
        self.BarTop = int(top)
    #取得当前进度条的Y值
    def GetProgressBarTop(self):
        return self.BarTop
    #设置当前进度栏里按钮圆点的半径
    def SetProgressBarButtonRadius(self,radius):
        self.BarButtonRadius = int(radius)
    #取得当前进度栏里按钮圆点的半径
    def GetProgressBarButtonRadius(self):
        return self.BarButtonRadius
    #设置当前进度栏里按钮之间的横向边距
    def SetProgressBarButtonSpacingX(self,spacingX):
        self.BarButtonSpacingX = int(spacingX)
    #取得当前进度栏里按钮之间的横向边距
    def GetProgressBarButtonSpacingX(self):
        return self.BarButtonSpacingX
    #设置当前进度栏里按钮之间的纵向边距
    def SetProgressBarButtonSpacingY(self,spacingY):
        self.BarButtonSpacingY = int(spacingY)
    #取得当前进度栏里按钮之间的纵向边距
    def GetProgressBarButtonSpacingY(self):
        return self.BarButtonSpacingY
    #设置当前进度栏里当前按钮的宽度
    def SetProgressBarCurrButtonWidth(self,width):
        self.BarCurrButtonWidth = int(width)
    #取得当前进度栏里当前按钮的宽度
    def GetProgressBarCurrButtonWidth(self):
        return self.BarCurrButtonWidth
    #设置点击确定时的回调函数
    def SetPageClickCallBackFunction(self,callBackFun,uiName,widgetName):
        self.PageClickCallBackFunction = callBackFun
        self.uiName = uiName
        self.widgetName = widgetName
    #增加一个页面项
    def AddPage(self,TitleText='',ImageFile='',ItemPage='',ItemIndex='end'):
        PageW = self.Canvas.winfo_width()
        if PageW == 1:
            PageW = 300
        PageH = self.Canvas.winfo_height()
        if PageH == 1:
            PageH = 240
        if ImageFile:
            filePath = ImageFile
            if filePath and os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,ImageFile)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,ImageFile)
            if os.path.exists(filePath) == True:
                try:
                    Image_Temp = Image.open(filePath).convert('RGBA')
                    Image_Resize = Image_Temp.resize((PageW, PageH),Image.LANCZOS)
                    Photo_Image = ImageTk.PhotoImage(Image_Resize)
                    if ItemIndex == "end" or  ItemIndex == -1:
                        self.CurrentIndex = len(self.ItemArray)
                        self.ItemArray.append([TitleText,ImageFile,ItemPage,Photo_Image])
                    else:
                        if type(ItemIndex) == type(""):
                            if ItemIndex.isdigit() == True:
                                ItemIndex = int(ItemIndex)
                            else:
                                ItemIndex = len(self.ItemArray)
                        self.CurrentIndex = ItemIndex
                        self.ItemArray.insert(ItemIndex,[TitleText,ImageFile,ItemPage,Photo_Image])
                except Exception as ex:
                    tkinter.messagebox.showwarning("error",ex)
    #删除指定页面项
    def DelPage(self,index):
        if index < len(self.ItemArray):
            self.ItemArray.pop(index)
        self.Redraw()
    #重建
    def Rebuild(self):
        OldItemArray = self.GetItemArray_Copy()
        self.Clear()
        for ItemInfo in OldItemArray:
            self.AddPage(TitleText=ItemInfo[0],ImageFile=ItemInfo[1],ItemPage=ItemInfo[2])
        self.Redraw()
    #页面播放
    def Play(self,switchDelay = 3000):
        if self.MouseEnter == False:
            PageCount = len(self.ItemArray)
            if PageCount > 0:
                self.CurrentIndex = self.CurrentIndex + 1
                self.CurrentIndex = self.CurrentIndex % PageCount
            self.Redraw()
        self.SwitchDelay = switchDelay
        if self.SwitchDelay > 0:
            self.Canvas.after(self.SwitchDelay,self.Play)
    #展开
    def Redraw(self):
        PageW = self.Canvas.winfo_width()
        if PageW == 1:
            PageW = 300
        PageH = self.Canvas.winfo_height()
        if PageH == 1:
            PageH = 240
        ButtonIndex = 0
        self.Canvas.delete("all")
        for ButtonInfo in self.ItemArray:
            if self.CurrentIndex == ButtonIndex:
                self.Canvas.create_image(0,0,anchor=tkinter.NW,image=ButtonInfo[3],tag='image')
                if ButtonInfo[0] !='':
                    Left = self.TitleLeft
                    if Left < 0 :
                        Left = PageW + Left
                    Top  = self.TitleTop
                    if Top < 0 :
                        Top = PageH + Top
                    self.Canvas.create_text(Left,Top,font=self.TitleFont,anchor=tkinter.NW,fill=self.TitleColor,text=ButtonInfo[0],tag='title')
            ButtonIndex = ButtonIndex + 1
        self.Canvas.tag_bind('image','<Enter>',self.onItemEnter)
        self.Canvas.tag_bind('image','<Leave>',self.onItemLeave)
        self.Canvas.tag_bind('image','<Button-1>',self.onItemClick)
        BarWidth = ButtonIndex * self.BarButtonSpacingX + ButtonIndex * 2 * self.BarButtonRadius + self.BarCurrButtonWidth
        BarHeight = (self.BarButtonRadius + self.BarButtonSpacingY) * 2
        BarLeft = self.BarLeft
        if BarLeft < 0:
            BarLeft = PageW + BarLeft
        BarTop = self.BarTop
        if BarTop < 0:
            BarTop = PageH + BarTop
        BarBGColor = '#333333'
        self.Canvas.create_rectangle(BarLeft,BarTop,BarLeft + BarWidth,BarTop + BarHeight+1,fill=BarBGColor,width=0,tag="bar") 
        self.Canvas.create_oval(BarLeft-self.BarButtonSpacingX,BarTop,BarLeft + self.BarButtonSpacingX,BarTop + BarHeight,fill=BarBGColor,width=0,tag="bar") 
        self.Canvas.create_oval(BarLeft + BarWidth - self.BarButtonSpacingX,BarTop,BarLeft  + BarWidth + self.BarButtonSpacingX,BarTop + BarHeight,fill=BarBGColor,width=0,tag="bar") 
        PointBGColor = '#FFFFFF'
        PointX = BarLeft
        PointY = BarTop + self.BarButtonSpacingY
        PointW = 2 * self.BarButtonRadius
        PointH = 2 * self.BarButtonRadius
        ButtonIndex = 0
        for ButtonInfo in self.ItemArray:
            TagName = str("point_%d"%ButtonIndex)
            self.Canvas.create_oval(PointX,PointY,PointX + PointW ,PointY + PointH,fill=PointBGColor,width=0,tag=TagName) 
            if self.CurrentIndex == ButtonIndex:
                self.Canvas.create_rectangle(PointX + self.BarButtonRadius,PointY,PointX + self.BarButtonRadius + self.BarCurrButtonWidth,PointY + PointH+1,fill=PointBGColor,width=0,tag=TagName) 
                PointX = PointX + self.BarButtonRadius + self.BarCurrButtonWidth
                self.Canvas.create_oval(PointX - self.BarButtonRadius,PointY,PointX + self.BarButtonRadius ,PointY + PointH,fill=PointBGColor,width=0,tag=TagName) 
                PointX = PointX + self.BarButtonRadius + self.BarButtonSpacingX
            else:
                PointX = PointX + PointW + self.BarButtonSpacingX
            #
            self.Canvas.tag_bind(TagName,'<Enter>',self.onItemEnter)
            self.Canvas.tag_bind(TagName,'<Leave>',self.onItemLeave)
            self.Canvas.tag_bind(TagName,'<Button-1>',partial(self.onPointClick,pageIndex=ButtonIndex))
            ButtonIndex = ButtonIndex + 1
        self.Canvas.create_text(30,PageH/2,font=("Arial",36),anchor=tkinter.CENTER,fill="#FFFFFF",text="〈",tag='last')
        self.Canvas.tag_bind('last','<Enter>',self.onItemEnter)
        self.Canvas.tag_bind('last','<Leave>',self.onItemLeave)
        self.Canvas.tag_bind('last','<Button-1>',self.goLast)
        self.Canvas.create_text(PageW-40,PageH/2,font=("Arial",36),anchor=tkinter.CENTER,fill="#FFFFFF",text="〉",tag='next')
        self.Canvas.tag_bind('next','<Enter>',self.onItemEnter)
        self.Canvas.tag_bind('next','<Leave>',self.onItemLeave)
        self.Canvas.tag_bind('next','<Button-1>',self.goNext)
