import wx
import sys
from datetime import datetime

sys.path.insert(0, 'model/Forum')
from EClass import EClass

from Forum import Forum

class ForumWindow(wx.Frame):
   def __init__(self):
      super(ForumWindow, self).__init__(None, -1, 'Forum')

      self.forum = Forum()

      self.SetClientSizeWH(500, 600)

      self.messagesArea = wx.TextCtrl(self, size = (500, 500), style = wx.TE_READONLY | wx.TE_MULTILINE)
      self.messageEntry = wx.TextCtrl(self, size = (500, 50), style = wx.TE_MULTILINE)
      self.messageEntry.SetValue('Enter message here')

      sendButton = wx.Button(self, label = 'Send', size = (100, 100))
      sendButton.Bind(wx.EVT_BUTTON, self.SendMessage)
      closeButton = wx.Button(self, label = 'Close', size = (100, 100))
      closeButton.Bind(wx.EVT_BUTTON, self.CloseForum)

      forumVertSizer = wx.BoxSizer(wx.VERTICAL)
      buttonHoriSizer = wx.BoxSizer(wx.HORIZONTAL)

      forumVertSizer.AddStretchSpacer(1)
      forumVertSizer.Add(self.messagesArea, 1, wx.CENTER)
      forumVertSizer.Add(self.messageEntry, 1, wx.CENTER)
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
      user = EClass.GetInstance().user
      #dateTime = datetime(2014, 4, 21)
      #datetime.strftime('%m/%d/%Y')
      #currentDateTime = time.strftime('%c')
      currentDateTime = datetime.now()
      self.forum.AddMessage(user.username, currentDateTime.strftime('%m/%d/%Y %I:%M %p'), self.messageEntry.GetValue())
      currentText = self.messagesArea.GetValue()
      self.messagesArea.SetValue(currentText + self.forum.messagesStack.pop().ToString() + "\n")
      self.messageEntry.SetValue("")

   def CloseForum(self, event):
      self.Close()

   def Refresh(self):
      self.forum.Refresh()