import wx
import sys

sys.path.insert(0, 'model')
from EClass import EClass

from RosterItemPanel import RosterItemPanel
from RosterStaticPanel import RosterStaticPanel
from Person.Roster import Roster
from Person.Student import Student

class RosterWindow(wx.Frame):
   def __init__(self, parent):
      super(RosterWindow, self).__init__(None, -1, 'Roster')

      self.rosterModel = EClass.GetInstance().roster
      self.rosterModel.setView(self)

      self.SetClientSizeWH(300, 700)
      self.parent = parent

      self.presentLabel = wx.TextCtrl(self, size = (300, 20), style = wx.TE_CENTRE | wx.TE_READONLY)
      self.presentLabel.SetValue("Present: ")
      self.presentLabel.SetForegroundColour(wx.WHITE)
      self.presentLabel.SetBackgroundColour('#0041C2')

      self.absentLabel = wx.TextCtrl(self, size = (300, 20), style = wx.TE_CENTRE | wx.TE_READONLY)
      self.absentLabel.SetValue("Absent: ")
      self.absentLabel.SetForegroundColour(wx.WHITE)
      self.absentLabel.SetBackgroundColour('#0041C2')
      
      self.classText = wx.TextCtrl(self, size = (300, 30), style = wx.TE_CENTRE | wx.TE_READONLY)
      self.classText.SetValue("")
      self.classText.SetBackgroundColour('#5CB3FF')

      self.rosterListBox = wx.ListBox(choices=[], name='listBox1', parent=self, pos=wx.Point(8, 48), style=0)
      self.rosterListBox.Bind(wx.EVT_LISTBOX, self.ShowStudentPanel)

      self.rosterListBoxAbsent = wx.ListBox(choices=[], name='listBox2', parent=self, pos=wx.Point(8, 48), style=0)

      self.rosterStaticPanel = RosterStaticPanel(self)
      self.rosterStaticPanel.SetSizer(self.rosterStaticPanel.sizer)
      self.rosterStaticPanel.sizer.Clear()

      rosterVertSizer = wx.BoxSizer(wx.VERTICAL)
      rosterVertSizer.Add(self.classText, 1, wx.EXPAND)
      rosterVertSizer.Add(self.presentLabel, 1, wx.EXPAND)
      rosterVertSizer.Add(self.rosterListBox, 7, wx.EXPAND)
      rosterVertSizer.Add(self.absentLabel, 1, wx.EXPAND)
      rosterVertSizer.Add(self.rosterListBoxAbsent, 2, wx.EXPAND)
      rosterVertSizer.Add(self.rosterStaticPanel, 4, wx.EXPAND)

      self.Bind(wx.EVT_CLOSE, self.onClose)
      self.SetSizer(rosterVertSizer)
      self.SendSizeEvent()
      
      EClass.GetInstance().rosterModel = self.rosterModel

   def redraw(self):
      self.rosterListBox.Clear()
      for student in self.rosterModel.studentsPresent:
         self.rosterListBox.Append(student.firstName + ' ' + student.lastName)
      self.rosterListBoxAbsent.Clear()
      for student in self.rosterModel.studentsAbsent:
         self.rosterListBoxAbsent.Append(student.firstName + ' ' + student.lastName)
      self.presentLabel.SetValue("Present: " + str(len(self.rosterModel.studentsPresent)))
      self.absentLabel.SetValue("Absent: " + str(len(self.rosterModel.studentsAbsent)))

   def onClose(self, event):
      self.parent.showRosterMenuItem.Check(False)
      self.rosterStaticPanel.sizer.Clear()
      self.Hide()

   def ShowStudentPanel(self, event):
      selName = self.rosterListBox.GetStringSelection()
      self.rosterStaticPanel.sizer.Clear()
      self.rosterStaticPanel.sizer.Add(RosterItemPanel(self.rosterStaticPanel, self.rosterModel.studentsPresent[self.rosterListBox.GetSelection()]), 1, wx.EXPAND)
      self.rosterStaticPanel.Refresh()
      self.SendSizeEvent()
