import wx
import sys

#view
from WhiteboardNav import WhiteboardNav
from LayerManager import LayerManager
from ApprovalTrackerGaget import ApprovalTrackerGaget

#model
sys.path.insert(0, 'model')
from EClass import EClass

class ImportPresentation(wx.Frame):
   
   def __init__(self, parent):

      no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | 
         wx.RESIZE_BOX | wx.MAXIMIZE_BOX | wx.CLOSE_BOX
      )

      super(ImportPresentation, self).__init__(None, -1, 'Presentation Import',
         style = no_resize      
      )
      self.parent = parent

      self.presentationList = wx.GenericDirCtrl(self, -1, style = wx.LC_REPORT,
         size = self.GetSize()
      )

      select = wx.Button(self, -1, 'Select', size = (200, 20))
      select.Bind(wx.EVT_BUTTON, self.SelectPresentation)

      cancel = wx.Button(self, -1, 'Cancel', size = (200, 20))
      cancel.Bind(wx.EVT_BUTTON, self.CancelSelectPresentation)

      sizer = wx.BoxSizer(wx.VERTICAL)
      horiSizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.Add(self.presentationList, 1, wx.ALIGN_CENTER)
      horiSizer.AddStretchSpacer(3)
      horiSizer.Add(select, 1)
      horiSizer.Add(cancel, 1)
      horiSizer.AddStretchSpacer(3)
      sizer.Add(horiSizer)
      self.SetSizer(sizer)

   def SelectPresentation(self, event):
      self.parent.importPresentation.Hide()
      self.parent.initialPrompt.Destroy()
      
      EClass.GetInstance().presentation.SetPath(self.parent.importPresentation
         .GetPresentationPath()
      )

      self.parent.whiteboard = WhiteboardNav(self.parent)
      self.parent.SendSizeEvent()
   
      self.parent.layerManager = LayerManager(self.parent)
      self.parent.layerManager.Show()
      eclass.presentation.ShowPresentation()

      # TODO, this should be opened in the menu
      ApprovalTrackerGaget()

   def CancelSelectPresentation(self, event):
      self.parent.initialPrompt.Show()
      self.parent.importPresentation.Hide()

   def GetPresentationPath(self):
      return self.presentationList.GetFilePath()
