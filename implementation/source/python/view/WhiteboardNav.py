import wx, wx.html
import sys

sys.path.insert(0, 'model')
from EClass import EClass

class WhiteboardNav(wx.Panel):
   
   def __init__(self, parent):
      super(WhiteboardNav, self).__init__(parent)

      self.presentation = EClass.GetInstance().presentation
      self.whiteboard = wx.html.HtmlWindow(self, -1, style = wx.DOUBLE_BORDER)
      self.whiteboard.Layout()
      self.whiteboard.LoadFile(self.presentation.GetPath())
      self.whiteboard.SetBackgroundColour('#FEEECC')
      
      previousSlideButton = wx.Button(self, label = '<< Previous',
         size = (70, 30)
      )
      previousSlideButton.Bind(wx.EVT_BUTTON, self.MoveToPreviousSlide)

      nextSlideButton = wx.Button(self, label = 'Next >>', size = (70, 30))
      nextSlideButton.Bind(wx.EVT_BUTTON, self.MoveToNextSlide)

      syncButton = wx.Button(self, label = 'SYNC', size = (120, 15))
      syncButton.Bind(wx.EVT_BUTTON, self.SyncWithPresenter)
      
      self.slideTextbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
      self.slideTextbox.Bind(wx.EVT_TEXT_ENTER, self.MoveToSlide)
      self.slideTextbox.SetHint('Slide Number')

      currSlideText = wx.StaticText(self, -1, label = '1')

      navVertSizer = wx.BoxSizer(wx.VERTICAL)
      navVertSizer.AddStretchSpacer(1)
      navVertSizer.Add(currSlideText, 5, wx.CENTER)
      navVertSizer.Add(self.slideTextbox, 5, flag = wx.BOTTOM|wx.CENTER,
         border = 20
      )
      
      #if isinstance(EClass.GetInstance().user, Student):
      navVertSizer.Add(syncButton, 3, wx.CENTER)
      navVertSizer.AddStretchSpacer(1)

      navHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      navHoriSizer.AddStretchSpacer(1)
      navHoriSizer.Add(previousSlideButton, 1, wx.CENTER)
      navHoriSizer.Add(navVertSizer, 1, flag = wx.LEFT|wx.RIGHT|wx.CENTER,
         border = 20
      )
      navHoriSizer.Add(nextSlideButton, 1, wx.CENTER)
      navHoriSizer.AddStretchSpacer(1)

      boardHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      boardHoriSizer.AddStretchSpacer(1)
      boardHoriSizer.AddWindow(self.whiteboard, 5, wx.EXPAND)
      boardHoriSizer.AddStretchSpacer(1)

      mainSizer = wx.BoxSizer(wx.VERTICAL)
      mainSizer.Add(boardHoriSizer, 10, wx.EXPAND)
      mainSizer.Add(navHoriSizer, 1, wx.CENTER)
      
      self.SetSizer(mainSizer)

   def MoveToPreviousSlide(self, event):
      self.presentation.MoveToPreviousSlide()

   def MoveToNextSlide(self, event):
      self.presentation.MoveToNextSlide()

   def SyncWithPresenter(self, event):
      self.presentation.SyncWithPresenter()

   def MoveToSlide(self, event):
      self.presentation.MoveToSlide(self.slideTextbox.GetValue())
