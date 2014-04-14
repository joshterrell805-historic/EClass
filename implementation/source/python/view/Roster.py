import wx

from RosterItem import RosterItem

class Roster(wx.Frame):
   def __init__(self):
      super(Roster, self).__init__(None, -1, 'Roster')

      self.rosterItem1 = RosterItem(self)
      self.rosterItem2 = RosterItem(self)
      self.rosterItem3 = RosterItem(self)
      self.rosterItem4 = RosterItem(self)
      self.rosterItem5 = RosterItem(self)
      self.rosterItem6 = RosterItem(self)

      self.SetClientSizeWH(300, 675)

      attendance = wx.TextCtrl(self, size = (300, 80), style = wx.TE_CENTRE | wx.TE_READONLY)
      attendance.SetValue('Attendance \n\n Present: 3\n Absent: 11')
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

      testButton = wx.Button(self, label = 'Test', size = (100, 30))
      testButton.Bind(wx.EVT_BUTTON, self.Test)

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
      rosterVertSizer.Add(testButton, 1, wx.CENTER)
      rosterVertSizer.AddStretchSpacer(1)

      self.SetSizer(rosterVertSizer)
      self.Show()

   def Test(self, event):
      EClass.GetInstance().RosterModel.Test()