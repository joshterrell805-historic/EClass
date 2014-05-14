import wx
 
########################################################################
class JoinPresentation(wx.Frame):
 
    #----------------------------------------------------------------------
   def __init__(self, parent):
      wx.Frame.__init__(self, None, wx.ID_ANY, "List Control Tutorial")

      # Add a panel so it looks the correct on all platforms
      panel = wx.Panel(self, wx.ID_ANY)
      self.index = 0
      self.parent = parent

      self.list_ctrl = wx.ListCtrl(panel, size=(-1,100),
         style=wx.LC_REPORT
         |wx.BORDER_SUNKEN
      )
      self.list_ctrl.InsertColumn(0, 'Class')
      self.list_ctrl.InsertColumn(1, 'Hosted')

      btn = wx.Button(panel, label="Join Presentation")

      sizer = wx.BoxSizer(wx.VERTICAL)
      sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
      sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
      panel.SetSizer(sizer)
      self.Bind(wx.EVT_CLOSE, self.onClose)

   def onClose(self, event):
      self.parent.showJoinMenuItem.Check(False)
      self.Hide()
