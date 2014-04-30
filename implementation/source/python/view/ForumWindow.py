import wx
import sys
from datetime import datetime

sys.path.insert(0, 'model/Forum')
from EClass import EClass

from Forum import Forum

class ForumWindow(wx.Frame):
   def __init__(self, parent):
      super(ForumWindow, self).__init__(None, -1, 'Forum')

      self.forum = Forum()
      self.parent = parent

      self.SetClientSizeWH(500, 600)

      self.messagesArea = wx.TextCtrl(self, style = wx.TE_READONLY | wx.TE_MULTILINE)
      self.messageEntry = wx.TextCtrl(self, style = wx.TE_MULTILINE)
      self.messageEntry.SetValue('Enter message here')

      sendButton = wx.Button(self, label = 'Send', size = (100, 100))
      sendButton.Bind(wx.EVT_BUTTON, self.SendMessage)
      closeButton = wx.Button(self, label = 'Close', size = (100, 100))
      closeButton.Bind(wx.EVT_BUTTON, self.CloseForum)

      forumVertSizer = wx.BoxSizer(wx.VERTICAL)
      buttonHoriSizer = wx.BoxSizer(wx.HORIZONTAL)

      forumVertSizer.Add(self.messagesArea, 1, wx.CENTER | wx.EXPAND)
      forumVertSizer.Add(self.messageEntry, 1, wx.CENTER | wx.EXPAND)
      forumVertSizer.Add(buttonHoriSizer, 1, wx.CENTER)

      buttonHoriSizer.Add(sendButton, 1, wx.CENTER)
      buttonHoriSizer.Add(closeButton, 1, wx.CENTER)

      self.SetSizer(forumVertSizer)

      self.Refresh()

      self.Bind(wx.EVT_CLOSE, self.onClose)

   def SendMessage(self, event):
      if self.messageEntry.GetValue() != "":
         user = EClass.GetInstance().user
         currentDateTime = datetime.now()
         self.forum.AddMessage(user.username, currentDateTime.strftime('%m/%d/%Y %I:%M %p'), self.messageEntry.GetValue())
         currentText = self.messagesArea.GetValue()
         self.messagesArea.SetValue(currentText + self.forum.messagesStack.pop().ToString() + "\n")
         self.messageEntry.SetValue("")
      else:
         pass


   def CloseForum(self, event):
      self.Close()

   def Refresh(self):
      self.forum.Refresh()

   def onClose(self, event):
      self.parent.showForumMenuItem.Check(False)
      self.Hide()
