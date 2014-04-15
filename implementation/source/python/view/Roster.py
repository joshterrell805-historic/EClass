import wx
import sys

sys.path.insert(0, 'model/Person')
from EClass import EClass

from RosterItem import RosterItem
from RosterModel import RosterModel

class Roster(wx.Frame):
   def __init__(self):
      super(Roster, self).__init__(None, -1, 'Roster')

      self.rosterModel = RosterModel()

      self.rosterItem1 = RosterItem(self)
      self.rosterItem2 = RosterItem(self)
      self.rosterItem3 = RosterItem(self)
      self.rosterItem4 = RosterItem(self)
      self.rosterItem5 = RosterItem(self)
      self.rosterItem6 = RosterItem(self)

      self.SetClientSizeWH(300, 700)

      attendance = wx.TextCtrl(self, size = (300, 80), style = wx.TE_CENTRE | wx.TE_READONLY)
      attendance.SetValue('Attendance \n\n Present: 3\n Absent: 11')
      attendance.SetForegroundColour('#FFFFFF')
      attendance.SetBackgroundColour('#0041C2')
      
      inClassText = wx.TextCtrl(self, size = (300, 30), style = wx.TE_CENTRE | wx.TE_READONLY)
      inClassText.SetValue('In Class')
      inClassText.SetBackgroundColour('#5CB3FF')

      studentListPanel = wx.Panel(self, size = (300, 220), style = wx.TE_CENTRE)
      studentListPanel.SetBackgroundColour('#FEEECC')

      remoteAccessText = wx.TextCtrl(self, size = (300, 30), style = wx.TE_CENTRE | wx.TE_READONLY)
      remoteAccessText.SetValue('Remote Access')
      remoteAccessText.SetBackgroundColour('#5CB3FF')

      remoteAccessPanel = wx.Panel(self, size = (300, 50), style = wx.TE_CENTRE)
      remoteAccessPanel.SetBackgroundColour('#FEEECC')

      addButton = wx.Button(self, label = 'Add Student', size = (150, 30))
      addButton.Bind(wx.EVT_BUTTON, self.AddStudent)

      removeButton = wx.Button(self, label = 'Remove Student', size = (150, 30))
      removeButton.Bind(wx.EVT_BUTTON, self.Remove)

      rosterVertSizer = wx.BoxSizer(wx.VERTICAL)
      rosterVertSizer.AddStretchSpacer(1)
      rosterVertSizer.Add(attendance, 1, wx.CENTER)
      rosterVertSizer.Add(inClassText, 1, wx.CENTER)

      rosterVertSizer.Add(self.rosterItem1, 1, wx.CENTER)
      rosterVertSizer.Add(self.rosterItem2, 1, wx.CENTER)
      rosterVertSizer.Add(self.rosterItem3, 1, wx.CENTER)
      rosterVertSizer.Add(self.rosterItem4, 1, wx.CENTER)
      
      rosterVertSizer.Add(studentListPanel, 1, wx.CENTER)
      rosterVertSizer.Add(remoteAccessText, 1, wx.CENTER)

      rosterVertSizer.Add(self.rosterItem5, 1, wx.CENTER)
      rosterVertSizer.Add(self.rosterItem6, 1, wx.CENTER)

      rosterVertSizer.Add(remoteAccessPanel, 1, wx.CENTER)

      rosterHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterHoriSizer.AddStretchSpacer(1)
      rosterHoriSizer.Add(addButton, 1, wx.CENTER)
      rosterHoriSizer.Add(removeButton, 1, wx.CENTER)
      rosterHoriSizer.AddStretchSpacer(1)
      rosterVertSizer.Add(rosterHoriSizer, 1, wx.CENTER)

      rosterVertSizer.AddStretchSpacer(1)

      self.SetSizer(rosterVertSizer)
      self.SendSizeEvent()
      self.Show()

   def AddStudent(self, event):
      self.rosterModel.AddNewStudent()

   def Remove(self, event):
      self.rosterModel.RemoveStudent()