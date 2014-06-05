import wx
import sys

sys.path.insert(0, '../model')
from EClass import EClass
from Person.RosterItem import RosterItem

from Person.Student import Student
from PermissionsWindow import PermissionsWindow
from KickWindow import KickWindow

class RosterItemPanel(wx.Panel):
   # TODO Update doc
   def __init__(self, parent, student):
      super(RosterItemPanel, self).__init__(parent, -1)
      self.student = student

      self.rosterItemModel = RosterItem(student)
      self.SetBackgroundColour('#FEEECC')

      usernameLabel = wx.StaticText(self, -1, label = 'Cal Poly Username: ')
      usernameStaticText = wx.StaticText(self, -1, label = student.username)

      self.handButton = wx.Button(self, label = 'Hand', size = (50, 30))
      self.handButton.Bind(wx.EVT_BUTTON, self.HandButton)
      self.layersButton = wx.Button(self, label = 'Layers', size = (60, 30))
      self.layersButton.Bind(wx.EVT_BUTTON, self.LayersButton)
      self.permissionsButton = wx.Button(self, label = 'Permissions', size = (90, 30))
      self.permissionsButton.Bind(wx.EVT_BUTTON, self.OpenPermissions)
      kickButton = wx.Button(self, label = 'Kick', size = (50, 30))
      kickButton.Bind(wx.EVT_BUTTON, self.OpenKickWindow)

      rosterItemButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterItemButtonSizer.AddStretchSpacer(1)
      rosterItemButtonSizer.Add(self.handButton, 1, wx.CENTER)
      rosterItemButtonSizer.Add(self.layersButton, 1, wx.CENTER)
      rosterItemButtonSizer.Add(self.permissionsButton, 1, wx.CENTER)
      rosterItemButtonSizer.Add(kickButton, 1, wx.CENTER)
      rosterItemButtonSizer.AddStretchSpacer(1)

      usernameSizer = wx.BoxSizer(wx.HORIZONTAL)
      usernameSizer.AddStretchSpacer(1)
      usernameSizer.Add(usernameLabel, 1, wx.CENTER)
      usernameSizer.Add(usernameStaticText, 1, wx.CENTER)
      usernameSizer.AddStretchSpacer(1)

      rosterItemMainSizer = wx.BoxSizer(wx.VERTICAL)
      rosterItemMainSizer.AddStretchSpacer(1)
      rosterItemMainSizer.Add(rosterItemButtonSizer, 1, wx.CENTER)
      rosterItemMainSizer.AddStretchSpacer(1)
      rosterItemMainSizer.Add(usernameSizer, 1, wx.CENTER)
      rosterItemMainSizer.AddStretchSpacer(1)

      self.SetSizer(rosterItemMainSizer)
      self.SendSizeEvent()

   def HandButton(self, event):
      self.rosterItemModel.Hand()

   def LayersButton(self, event):
      self.rosterItemModel.Layers()

   def OpenPermissions(self, event):
      PermissionsWindow(self.rosterItemModel.student)
      
   def OpenKickWindow(self, event):
      KickWindow(self.rosterItemModel.student)
