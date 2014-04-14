import wx

class RosterItem(wx.Panel):
   def __init__(self, parent):
      super(RosterItem, self).__init__(parent)
      self.parent = parent

      self.name = wx.StaticText(self, -1, label = 'FirstName LastName')

      self.handButton = wx.Button(self, label = 'Hand', size = (70, 30))
      self.modeButton = wx.Button(self, label = 'Mode', size = (70, 30))
      self.permissionsButton = wx.Button(self, label = 'Permissions', size = (70, 30))

      rosterItemHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterItemHoriSizer.AddStretchSpacer(1)
      rosterItemHoriSizer.Add(name)
      rosterItemHoriSizer.Add(handButton)
      rosterItemHoriSizer.Add(modeButton)
      rosterItemHoriSizer.Add(permissionsButton)
      rosterItemHoriSizer.AddStretchSpacer(1)