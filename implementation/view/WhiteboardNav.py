import wx
from Student import Student

class WhiteboardNav(wx.Panel):
   
   def __init__(self, parent, presentation, userType):
      super(WhiteboardNav, self).__init__(parent)
      self.presentation = presentation

      self.whiteboard = wx.TextCtrl(self, style = wx.TE_MULTILINE)
      self.whiteboard.SetEditable(False)
      
      previousSlideButton = wx.Button(self, label = '<< Previous',
         size = (100, 100)
      )
      previousSlideButton.Bind(wx.EVT_BUTTON, MoveToPreviousSlide)

      nextSlideButton = wx.Button(self, label = 'Next >>', size = (100, 100))
      nextSlideButton.Bind(wx.EVT_BUTTON, MoveToNextSlide)

      syncButton = wx.Button(self, label = 'SYNC', size = (100, 100))
      syncButton.Bind(wx.EVT_BUTTON, SyncWithPresenter)
      
      self.slideTextbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
      self.slideTextbox.Bind(wx.EVT_TEXT_ENTER, MoveToSlide)
      self.slideTextbox.SetHint('Slide Number')

      currSlideText = wx.StaticText(self, -1, label = '1')

      navVertSizer = wx.BoxSizer(wx.VERTICAL)
      navVertSizer.AddStretchSpacer(1)
      navVertSizer.Add(currSlideText, 1, wx.CENTER)
      navVertSizer.Add(self.slideTextbox, 1, wx.CENTER)
      
      #if isinstance(userType, Student):
      navVertSizer.Add(syncButton, 1, wx.CENTER)
      navVertSizer.AddStretchSpacer(1)

      navHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      navHoriSizer.AddStretchSpacer(1)
      navHoriSizer.Add(previousSlideButton, 1, wx.CENTER)
      navHoriSizer.Add(navVertSizer, 1, wx.CENTER)
      navHoriSizer.Add(nextSlideButton, 1, wx.CENTER)
      navHoriSizer.AddStretchSpacer(1)

      mainSizer = wx.BoxSizer(wx.VERTICAL)
      mainSizer.AddStretchSpacer(1)
      mainSizer.Add(self.whiteboard, 1, wx.CENTER)
      mainSizer.Add(navHoriSizer, 1, wx.CENTER)
      mainSizer.AddStretchSpacer(1)
      
      self.SetSizer(mainSizer)

def MoveToPreviousSlide(self, event):
   self.presentation.MoveToPreviousSlide()

def MoveToNextSlide(self, event):
   self.presentation.MoveToNextSlide()

def SyncWithPresenter(self, event):
   self.presentation.SyncWithPresenter()

def MoveToSlide(self, event):
   self.presentation.MoveToSlide(self.slideTextbox.GetValue())
