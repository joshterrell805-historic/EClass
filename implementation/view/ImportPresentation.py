import wx

class ImportPresentation(wx.Frame):
   
   def __init__(self, SelectPresentation, CancelSelectPresentation):
      super(ImportPresentation, self).__init__(None, -1, 'Lecture Import')

      lectureList = wx.ListCtrl(self, -1, style = wx.LC_REPORT,
         size = self.GetSize()
      )
      lectureList.InsertColumn(0, 'Class', width = self.GetSize().width/2)
      lectureList.InsertColumn(1, 'Presentation', width = self.GetSize().width/2)
      lectureList.Append(('308', 'Week 1'))
      lectureList.Append(('308', 'Week 2'))
      lectureList.Append(('308', 'Week 3'))
      lectureList.Append(('308', 'Week 4'))
      lectureList.Append(('308', 'Week 5'))
      lectureList.Append(('308', 'Week 6'))
      lectureList.Append(('308', 'Week 7'))
      lectureList.Append(('308', 'Week 8'))
      lectureList.Append(('308', 'Week 9'))
      lectureList.Append(('308', 'Week 10'))

      select = wx.Button(self, -1, 'Select')
      select.Bind(wx.EVT_BUTTON, SelectPresentation)
      cancel = wx.Button(self, -1, 'Cancel')
      cancel.Bind(wx.EVT_BUTTON, CancelSelectPresentation)

      sizer = wx.BoxSizer(wx.VERTICAL)
      horiSizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.Add(lectureList, 2, wx.CENTER)
      horiSizer.AddStretchSpacer(2)
      horiSizer.Add(select, 1, wx.CENTER)
      horiSizer.Add(cancel, 1, wx.CENTER)
      horiSizer.AddStretchSpacer(2)
      sizer.Add(horiSizer)
      self.SetSizer(sizer)
