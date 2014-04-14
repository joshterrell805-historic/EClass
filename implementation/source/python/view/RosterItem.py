import wx

class RosterItem(wx.Panel):
   def __init__(self, parent):
      super(RosterItem, self).__init__(parent, -1, size = (300, 40))

      self.name = wx.StaticText(self, -1, label = 'First Last')

      self.SetBackgroundColour('#FFFFFF')

      self.handButton = wx.Button(self, label = 'Hand', size = (50, 30))
      self.modeButton = wx.Button(self, label = 'Mode', size = (50, 30))
      self.permissionsButton = wx.Button(self, label = 'Permissions', size = (90, 30))

      rosterItemHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      rosterItemHoriSizer.AddStretchSpacer(1)
      rosterItemHoriSizer.Add(self.name)
      rosterItemHoriSizer.AddStretchSpacer(1)
      rosterItemHoriSizer.Add(self.handButton)
      rosterItemHoriSizer.Add(self.modeButton)
      rosterItemHoriSizer.Add(self.permissionsButton)
      rosterItemHoriSizer.AddStretchSpacer(1)

      self.SetSizer(rosterItemHoriSizer)