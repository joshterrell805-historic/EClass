import wx
import sys

sys.path.insert(0, 'model/Forum')
from EClass import EClass

from Forum import Forum

class ForumWindow(wx.Frame):
   def __init__(self):
      super(ForumWindow, self).__init__(None, -1, 'Forum')

      self.forumModel = Forum()

      self.SetClientSizeWH(500, 600)

      messagesArea = wx.TextCtrl(self, size = (500, 500), style = wx.TE_READONLY)
      messageEntry = wx.TextCtrl(self, size = (500, 50), style = wx.TE_MULTILINE)
      messageEntry.SetValue('Enter message here')

      sendButton = wx.Button(self, label = 'Send', size = (100, 100))
      sendButton.Bind(wx.EVT_BUTTON, self.SendMessage)
      closeButton = wx.Button(self, label = 'Close', size = (100, 100))
      closeButton.Bind(wx.EVT_BUTTON, self.CloseForum)

      forumVertSizer = wx.BoxSizer(wx.VERTICAL)
      buttonHoriSizer = wx.BoxSizer(wx.HORIZONTAL)

      forumVertSizer.AddStretchSpacer(1)
      forumVertSizer.Add(messagesArea, 1, wx.CENTER)
      forumVertSizer.Add(messageEntry, 1, wx.CENTER)
      forumVertSizer.Add(buttonHoriSizer, 1, wx.CENTER)
      forumVertSizer.AddStretchSpacer(1)

      buttonHoriSizer.AddStretchSpacer(1)
      buttonHoriSizer.Add(sendButton, 1, wx.CENTER)
      buttonHoriSizer.Add(closeButton, 1, wx.CENTER)
      buttonHoriSizer.AddStretchSpacer(1)

      self.SetSizer(forumVertSizer)

      self.Refresh()

      self.Show()

   def SendMessage(self, event):
      self.forumModel.SendMessage()

   def CloseForum(self, event):
      self.Close()

   def Refresh(self):
      self.forumModel.Refresh()