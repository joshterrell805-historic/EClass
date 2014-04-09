import wx

class InitialPrompt(wx.Panel):
   
   def __init__(self, parent, CreatePresentation, UsePresentation):
      super(InitialPrompt, self).__init__(parent)
      
      createPresentationButton = wx.Button(self, label = 'Create New Presentation',
         size = (100, 100)
      )
      createPresentationButton.Bind(wx.EVT_BUTTON, CreatePresentation) 

      importPresentationButton = wx.Button(self, label = 'Import Premade Presentation', 
         size = (100, 100)
      )
      importPresentationButton.Bind(wx.EVT_BUTTON, UsePresentation)

      sizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.AddStretchSpacer(1)
      sizer.Add(createPresentationButton, 1, wx.CENTER)
      sizer.Add(importPresentationButton, 1, wx.CENTER)
      sizer.AddStretchSpacer(1)
      self.SetSizer(sizer)
      
