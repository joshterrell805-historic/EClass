import wx

class ImportPresentation(wx.Frame):
   
   def __init__(self, SelectPresentation, CancelSelectPresentation):

      no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | 
         wx.RESIZE_BOX | 
         wx.MAXIMIZE_BOX
      )

      super(ImportPresentation, self).__init__(None, -1, 'Presentation Import',
         style = no_resize      
      )

      self.presentationList = wx.GenericDirCtrl(self, -1, style = wx.LC_REPORT,
         size = self.GetSize()
      )

      select = wx.Button(self, -1, 'Select', size = (200, 20))
      select.Bind(wx.EVT_BUTTON, SelectPresentation)

      cancel = wx.Button(self, -1, 'Cancel', size = (200, 20))
      cancel.Bind(wx.EVT_BUTTON, CancelSelectPresentation)

      sizer = wx.BoxSizer(wx.VERTICAL)
      horiSizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.Add(self.presentationList, 1, wx.ALIGN_CENTER)
      horiSizer.AddStretchSpacer(3)
      horiSizer.Add(select, 1)
      horiSizer.Add(cancel, 1)
      horiSizer.AddStretchSpacer(3)
      sizer.Add(horiSizer)
      self.SetSizer(sizer)

   def GetPresentationPath(self):
      return self.presentationList.GetFilePath()
