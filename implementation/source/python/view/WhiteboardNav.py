import wx, wx.html, wx.html2, wx.lib.intctrl
import sys

sys.path.insert(0, 'model')
from EClass import EClass
from Person.Student import Student

class WhiteboardNav(wx.Panel):

   def __init__(self, parent):
      super(WhiteboardNav, self).__init__(parent)
      
      self.shapes = []
      self.parent = parent
      self.presentation = EClass.GetInstance().presentation
      self.whiteboard = wx.html2.WebView.New(self, -1, style = wx.DOUBLE_BORDER)
      self.whiteboard.Layout()
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent(),
         self.presentation.GetPath()
      )
      self.RunScript()


      previousSlideButton = wx.Button(self, label = '<< Previous',
         size = (70, 30)
      )
      previousSlideButton.Bind(wx.EVT_BUTTON, self.MoveToPreviousSlide)

      nextSlideButton = wx.Button(self, label = 'Next >>', size = (70, 30))
      nextSlideButton.Bind(wx.EVT_BUTTON, self.MoveToNextSlide)
      
      self.slideTextbox = wx.lib.intctrl.IntCtrl(self, 
         style = wx.TE_PROCESS_ENTER | wx.TE_CENTRE
      )
      self.slideTextbox.Bind(wx.EVT_TEXT_ENTER, self.MoveToSlide)
      self.slideTextbox.SetHint('Slide Number')
      self.slideTextbox.Clear()

      self.currSlideText = wx.StaticText(self, -1, label = '1')

      navVertSizer = wx.BoxSizer(wx.VERTICAL)
      navVertSizer.AddStretchSpacer(1)
      navVertSizer.Add(self.currSlideText, 5, wx.CENTER)
      navVertSizer.Add(self.slideTextbox, 5, flag = wx.BOTTOM|wx.CENTER,
         border = 20
      )

      # Only add the Sync button for Students
      if isinstance(EClass.GetInstance().user, Student):
         syncButton = wx.Button(self, label = 'SYNC', size = (120, 15))
         syncButton.Bind(wx.EVT_BUTTON, self.SyncWithPresenter)
         navVertSizer.Add(syncButton, 3, wx.CENTER)
      navVertSizer.AddStretchSpacer(1)

      navHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      navHoriSizer.AddStretchSpacer(1)
      navHoriSizer.Add(previousSlideButton, 1, wx.CENTER)
      navHoriSizer.Add(navVertSizer, 1, flag = wx.LEFT|wx.RIGHT|wx.CENTER,
         border = 20
      )
      navHoriSizer.Add(nextSlideButton, 1, wx.CENTER)
      navHoriSizer.AddStretchSpacer(1)

      boardHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      boardHoriSizer.AddStretchSpacer(1)
      boardHoriSizer.AddWindow(self.whiteboard, 5, wx.EXPAND)
      boardHoriSizer.AddStretchSpacer(1)

      mainSizer = wx.BoxSizer(wx.VERTICAL)
      mainSizer.Add(boardHoriSizer, 10, wx.EXPAND)
      mainSizer.Add(navHoriSizer, 1, wx.CENTER)
      
      self.SetSizer(mainSizer)
      self.whiteboard.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.OnPageNavigation)
      self.parent.Bind(wx.EVT_ICONIZE, self.OnPaint)
      self.Show()

   def OnPageNavigation(self, evt):
      uri = evt.GetURL()

      try:
         dc = wx.WindowDC(self.whiteboard)
         gc = wx.GraphicsContext.Create(dc)
         gc.SetPen(wx.RED_PEN)
      except:
         print('Furq!')

      if "__EVENT__/mousedown" in uri:
         whiteboardMousePos = self.whiteboard.ScreenToClient(wx.GetMousePosition())
         self.shapes.append((whiteboardMousePos.x, whiteboardMousePos.y, 200, 200))
         gc.DrawRectangle(whiteboardMousePos.x, whiteboardMousePos.y, 200, 200)
         print 'paint1'
         evt.Veto()
         return

   def OnPaint(self, evt):
      try:
         dc = wx.WindowDC(self.whiteboard)
         gc = wx.GraphicsContext.Create(dc)
      except:
         print('Furq!')

      gc.SetPen(wx.RED_PEN)
      for shape in self.shapes:
         if gc:
            print 'drawing'
            gc.DrawRectangle(shape[0], shape[1], shape[2], shape[3])
      return
         

   def MoveToPreviousSlide(self, event):
      if self.presentation.MoveToPreviousSlide():
         self.RefreshSlide()

   def MoveToNextSlide(self, event):
      if self.presentation.MoveToNextSlide():
         self.RefreshSlide()

   def SyncWithPresenter(self, event):
      self.presentation.SyncWithPresenter()
      self.RefreshSlide()

   def MoveToSlide(self, event):
      if self.presentation.MoveToSlide(self.slideTextbox.GetValue()):
         self.RefreshSlide()
      self.slideTextbox.Clear()

   def RefreshSlide(self):
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent(),
         self.presentation.GetPath()
      )
      EClass.GetInstance().setUpLayerManager()
      self.parent.menuBar.layerManager.UpdateLayers()
      self.currSlideText.SetLabel(str(self.presentation.GetSlideNum()))
      self.RunScript()

   def RunScript(self):
      self.whiteboard.RunScript("""
         document.body.onmousedown = function() {
            window.location.href = "__EVENT__/mousedown";
         };
      """)
