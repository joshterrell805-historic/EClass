import wx
import sys

sys.path.insert(0, 'model/Person')
from EClass import EClass

from RosterItemPanel import RosterItemPanel
from Roster import Roster
from Person.Student import Student
import wx.lib.agw.foldpanelbar as fpb

class RosterWindow(wx.Frame):
   def __init__(self, parent):
      super(RosterWindow, self).__init__(None, -1, 'Roster')

      self.rosterModel = Roster()

      self.SetClientSizeWH(300, 700)
      self.parent = parent


      self.foldPanelBar = fpb.FoldPanelBar(self, size = (300, 200), style = fpb.FPB_VERTICAL, agwStyle = fpb.FPB_SINGLE_FOLD)
      for i in range(0, len(self.rosterModel.students)):
         self.AddRosterItem(self.foldPanelBar, self.rosterModel.students[i])

      self.foldPanelBarRemote = fpb.FoldPanelBar(self, size = (300, 200), style = fpb.FPB_VERTICAL, agwStyle = fpb.FPB_SINGLE_FOLD)
      for i in range(0, len(self.rosterModel.remoteList)):
         self.AddRosterItem(self.foldPanelBarRemote, self.rosterModel.remoteList[i])

      attendance = wx.TextCtrl(self, size = (300, 80), style = wx.TE_CENTRE | wx.TE_READONLY)
      attendance.SetValue('Attendance \n\n Present: 3\n Absent: 11')
      attendance.SetForegroundColour(wx.WHITE)
      attendance.SetBackgroundColour('#0041C2')
      
      inClassText = wx.TextCtrl(self, size = (300, 30), style = wx.TE_CENTRE | wx.TE_READONLY)
      inClassText.SetValue('In Class')
      inClassText.SetBackgroundColour('#5CB3FF')

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

      rosterVertSizer.Add(self.foldPanelBar, 1, wx.CENTER)
      
      rosterVertSizer.Add(remoteAccessText, 1, wx.CENTER)

      rosterVertSizer.Add(self.foldPanelBarRemote, 1, wx.CENTER)

      rosterVertSizer.Add(remoteAccessPanel, 1, wx.CENTER)

      rosterHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterHoriSizer.AddStretchSpacer(1)
      rosterHoriSizer.Add(addButton, 1, wx.CENTER)
      rosterHoriSizer.Add(removeButton, 1, wx.CENTER)
      rosterHoriSizer.AddStretchSpacer(1)
      rosterVertSizer.Add(rosterHoriSizer, 1, wx.CENTER)
      rosterVertSizer.AddStretchSpacer(1)

      self.Bind(wx.EVT_CLOSE, self.onClose)
      self.SetSizer(rosterVertSizer)
      self.SendSizeEvent()

   def AddRosterItem(self, fpb, username):
      if fpb == self.foldPanelBar:
         foldPanel = self.foldPanelBar.AddFoldPanel(username, collapsed = True)
         # TODO use actual student
         panel = RosterItemPanel(foldPanel, Student('Dummy', 'Ymmud'))
         self.foldPanelBar.AddFoldPanelWindow(foldPanel, panel)
      elif fpb == self.foldPanelBarRemote:
         foldPanel = self.foldPanelBarRemote.AddFoldPanel(username, collapsed = True)
         # TODO use actual student
         panel = RosterItemPanel(foldPanel, Student('Dummy', 'Ymmud'))
         self.foldPanelBarRemote.AddFoldPanelWindow(foldPanel, panel)

   def AddStudent(self, event):
      self.rosterModel.AddNewStudent()

   def Remove(self, event):
      self.rosterModel.RemoveStudent()

   def onClose(self, event):
      self.parent.showRosterMenuItem.Check(False)
      self.Hide()
