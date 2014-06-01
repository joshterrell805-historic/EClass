import wx
import sys

sys.path.insert(0, 'model')
from EClass import EClass

from RosterItemPanel import RosterItemPanel
from RosterStaticPanel import RosterStaticPanel
from Person.Roster import Roster
from Person.Student import Student
import wx.lib.agw.foldpanelbar as fpb
import wx.lib.scrolledpanel as scrolled

class RosterWindow(wx.Frame):
   def __init__(self, parent):
      super(RosterWindow, self).__init__(None, -1, 'Roster')

      self.rosterModel = EClass.GetInstance().roster
      self.rosterModel.setView(self)

      self.studentPanels = []

      self.SetClientSizeWH(300, 700)
      self.parent = parent

      attendance = wx.TextCtrl(self, size = (300, 80), style = wx.TE_CENTRE | wx.TE_READONLY)
      attendance.SetValue('Attendance \n\n Present: 3\n Absent: 11')
      attendance.SetForegroundColour(wx.WHITE)
      attendance.SetBackgroundColour('#0041C2')
      
      inClassText = wx.TextCtrl(self, size = (300, 30), style = wx.TE_CENTRE | wx.TE_READONLY)
      inClassText.SetValue('In Class')
      inClassText.SetBackgroundColour('#5CB3FF')

      self.rosterListBox = wx.ListBox(choices=[], name='listBox1', parent=self, pos=wx.Point(8, 48), style=0)
      self.rosterListBox.Bind(wx.EVT_LISTBOX, self.ShowStudentPanel)

      self.redraw()


      self.rosterStaticPanel = RosterStaticPanel(self)
      #self.staticPanel = wx.Panel(self, size = (300, 50), style = wx.TE_CENTRE)
      #self.staticPanel.SetBackgroundColour('#FEEECC')
      

      addButton = wx.Button(self, label = 'Add Student', size = (150, 30))
      addButton.Bind(wx.EVT_BUTTON, self.AddStudent)

      removeButton = wx.Button(self, label = 'Remove Student', size = (150, 30))
      removeButton.Bind(wx.EVT_BUTTON, self.Remove)

      rosterVertSizer = wx.BoxSizer(wx.VERTICAL)
      rosterVertSizer.AddStretchSpacer(1)
      rosterVertSizer.Add(attendance, 1, wx.EXPAND)
      rosterVertSizer.Add(inClassText, 1, wx.EXPAND)

      rosterVertSizer.Add(self.rosterListBox, 9, wx.EXPAND)

      rosterVertSizer.Add(self.rosterStaticPanel, 4, wx.EXPAND)
      #rosterVertSizer.Add(self.staticPanel, 4, wx.EXPAND)

      rosterHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterHoriSizer.AddStretchSpacer(1)
      rosterHoriSizer.Add(addButton, 1, wx.EXPAND)
      rosterHoriSizer.Add(removeButton, 1, wx.EXPAND)
      rosterHoriSizer.AddStretchSpacer(1)
      rosterVertSizer.Add(rosterHoriSizer, 1, wx.EXPAND)
      rosterVertSizer.AddStretchSpacer(1)

      self.Bind(wx.EVT_CLOSE, self.onClose)
      self.SetSizer(rosterVertSizer)
      self.SendSizeEvent()
      
      EClass.GetInstance().rosterModel = self.rosterModel

   def redraw(self):
      self.rosterListBox.Clear()
      counter = 0
      for student in self.rosterModel.students:
         self.rosterListBox.Append(student.firstName + ' ' + student.lastName)
         if student.present == False:
            self.rosterListBox.SetItemForegroundColour(counter, wx.RED)
            counter = counter + 1
      for i in range(0, len(self.studentPanels)):
         self.studentPanels[i].destroy()
      del self.studentPanels[0:len(self.studentPanels)]
      self.SyncPanels()

   def AddStudent(self, event):
      self.rosterModel.AddNewStudent()

   def Remove(self, event):
      self.rosterModel.RemoveStudent()

   def onClose(self, event):
      self.parent.showRosterMenuItem.Check(False)
      self.rosterStaticPanel.sizer.Clear()
      self.Hide()

   def SyncPanels(self):
      for i in range(0, len(self.rosterModel.students)):
         self.studentPanels.append(RosterItemPanel(self.rosterStaticPanel, self.rosterModel.students[i]))

      print("Students: " + str(len(self.rosterModel.students)))

   def ShowStudentPanel(self, event):
      #fix this call to SyncPanels, panels keep getting added to the list and never stops
      print("Panels: " + str(len(self.studentPanels)))
      selName = self.rosterListBox.GetStringSelection()
      self.rosterStaticPanel.sizer.Clear()
      self.rosterStaticPanel.sizer.Add(self.studentPanels[self.rosterListBox.GetSelection()], 1, wx.EXPAND)
      self.rosterStaticPanel.SetSizer(self.rosterStaticPanel.sizer)
      self.SendSizeEvent()
