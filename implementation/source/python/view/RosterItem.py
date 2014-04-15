import wx
import sys

sys.path.insert(0, 'model/Person')
from EClass import EClass

from RosterItemModel import RosterItemModel

sys.path.insert(0, '../model')
from Person.Student import Student
from PermissionsWindow import PermissionsWindow

class RosterItem(wx.Panel):
   def __init__(self, parent):
      super(RosterItem, self).__init__(parent, -1, size = (300, 40))

      self.rosterItemModel = RosterItemModel()

      self.name = wx.StaticText(self, -1, label = 'First Last')

      self.SetBackgroundColour('#FFFFFF')

      self.handButton = wx.Button(self, label = 'Hand', size = (50, 30))
      self.handButton.Bind(wx.EVT_BUTTON, self.HandButton)
      self.layersButton = wx.Button(self, label = 'Layers', size = (60, 30))
      self.layersButton.Bind(wx.EVT_BUTTON, self.LayersButton)
      self.permissionsButton = wx.Button(self, label = 'Permissions', size = (90, 30))
      self.permissionsButton.Bind(wx.EVT_BUTTON, self.OpenPermissions)

      rosterItemHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterItemHoriSizer.AddStretchSpacer(1)
      rosterItemHoriSizer.Add(self.name)
      rosterItemHoriSizer.AddStretchSpacer(1)
      rosterItemHoriSizer.Add(self.handButton)
      rosterItemHoriSizer.Add(self.layersButton)
      rosterItemHoriSizer.Add(self.permissionsButton)
      rosterItemHoriSizer.AddStretchSpacer(1)

      self.SetSizer(rosterItemHoriSizer)

   def HandButton(self, event):
      self.rosterItemModel.Hand()

   def LayersButton(self, event):
      self.rosterItemModel.Layers()

   def OpenPermissions(self, event):
      PermissionsWindow(Student("dummy", "ymmud")) # Dummy student for now
