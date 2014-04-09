import wx

class ImportPresentation(wx.Frame):
   
   def __init__(self, SelectPresentation, CancelSelectPresentation):
      super(ImportPresentation, self).__init__(None, -1, 'Presentation Import')

      self.presentationList = wx.GenericDirCtrl(self, -1, style = wx.LC_REPORT,
         size = self.GetSize()
      )

      select = wx.Button(self, -1, 'Select')
      select.Bind(wx.EVT_BUTTON, SelectPresentation)

      cancel = wx.Button(self, -1, 'Cancel')
      cancel.Bind(wx.EVT_BUTTON, CancelSelectPresentation)

      sizer = wx.BoxSizer(wx.VERTICAL)
      horiSizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.Add(self.presentationList, 2, wx.CENTER)
      horiSizer.AddStretchSpacer(2)
      horiSizer.Add(select, 1, wx.CENTER)
      horiSizer.Add(cancel, 1, wx.CENTER)
      horiSizer.AddStretchSpacer(2)
      sizer.Add(horiSizer)
      self.SetSizer(sizer)

   def GetPresentationPath(self):
      return self.presentationList.GetFilePath()
