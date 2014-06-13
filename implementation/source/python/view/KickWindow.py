import wx
import sys
sys.path.insert(0, '../model')

import EClass
from Person.Student import Student

class KickWindow(wx.Frame):
   
   def __init__(self, student):

      super(KickWindow, self).__init__(None, -1, 'Kick Confirmation', size=(500,200))
      self.SetBackgroundColour('#FFFFFF')
      
      self.student = student 
      mainSizer = wx.BoxSizer(wx.VERTICAL)
      buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
      
      acceptButton = wx.Button(self, label = 'Yes')
      acceptButton.Bind(wx.EVT_BUTTON, self.OnAccept)
      buttonsSizer.AddStretchSpacer(2)
      buttonsSizer.Add(acceptButton, 1, wx.ALIGN_CENTER)

      cancelButton = wx.Button(self, label = 'Cancel')
      cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
      buttonsSizer.Add(cancelButton, 1, wx.ALIGN_CENTER)
      buttonsSizer.AddStretchSpacer(2)
      
      mainSizer.AddStretchSpacer(1)
      kickPrompt = wx.StaticText(self, 
         label = 'Are you sure you want to kick ' + self.student.username + '?'
      )
      kickPrompt.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
      mainSizer.Add(kickPrompt, 3, wx.ALIGN_CENTER)
      mainSizer.Add(buttonsSizer, flag = wx.ALIGN_CENTER_HORIZONTAL)
      mainSizer.AddStretchSpacer(1)

      self.SetSizer(mainSizer)
      self.Show()

   def OnAccept(self, event):
      self.student.SetKicked(True)
      # Send a kick notification to the student (no message value used)
      EClass.EClass.GetInstance().connection.send(
         'kick notification', {'pickle': 'needs this'}, self.student.username
      )
      EClass.EClass.GetInstance().connection.CloseConnection(self.student.username)
      EClass.EClass.GetInstance().roster.onLeave(self.student.username)
      self.Destroy()
      
   def OnCancel(self, event):
      self.Destroy()

