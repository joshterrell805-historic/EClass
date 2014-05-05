import  wx
from Roster import Roster
from RosterItemPanel import RosterItemPanel
from Person.Student import Student
import  wx.lib.scrolledpanel as scrolled
import wx.lib.agw.foldpanelbar as fpb

class RosterScrollPanel(scrolled.ScrolledPanel):
   def __init__(self, parent):
      scrolled.ScrolledPanel.__init__(self, parent, -1, size = (300, 50))
      self.rosterModel = Roster()
      vbox = wx.BoxSizer(wx.VERTICAL)
      self.SetBackgroundColour(wx.RED)
        
      self.foldPanelBar = fpb.FoldPanelBar(self, size = (300, 200), style = fpb.FPB_VERTICAL, agwStyle = fpb.FPB_SINGLE_FOLD)
      for i in range(0, len(self.rosterModel.students)):
         self.AddRosterItem(self.foldPanelBar, self.rosterModel.students[i])

      vbox.Add(self.foldPanelBar, 0, wx.EXPAND)
      
      self.SetSizer(vbox)
      self.SetAutoLayout(1)
      self.SetupScrolling(scroll_x = False)

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