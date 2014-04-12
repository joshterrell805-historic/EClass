import wx
from ImportPresentation import ImportPresentation

# This is the initial **presenter** prompt
# TODO We need to open up a different prompt for students

class InitialPrompt(wx.Panel):
   
   def __init__(self, parent):
      super(InitialPrompt, self).__init__(parent)
      self.parent = parent
      
      ## For now, the WYSIWYG editor is thrown on the back burner so we can
      ##  implement more important features

      # createPresentationButton = wx.Button(self, label = 'Create New Presentation',
      #    size = (100, 100)
      # )
      # createPresentationButton.Bind(wx.EVT_BUTTON, self.CreatePresentation) 

      importPresentationButton = wx.Button(self, label = 'Open Presentation', 
         size = (100, 100)
      )
      importPresentationButton.Bind(wx.EVT_BUTTON, self.UsePresentation)

      sizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.AddStretchSpacer(1)
      # sizer.Add(createPresentationButton, 1, wx.CENTER)
      sizer.Add(importPresentationButton, 1, wx.CENTER)
      sizer.AddStretchSpacer(1)
      self.SetSizer(sizer)

   def CreatePresentation(self, event):
      self.parent.initialPrompt.Hide()

   def UsePresentation(self, event):
      self.parent.initialPrompt.Hide()
      self.parent.importPresentation.Show()
      
