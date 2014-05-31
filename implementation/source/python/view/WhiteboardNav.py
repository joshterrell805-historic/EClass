import wx, wx.html, wx.html2, wx.lib.intctrl
import sys, time

sys.path.insert(0, 'model')
from EClass import EClass
from Person.Student import Student
from Presentation.LayerManagerModel import LayerManagerModel

class WhiteboardNav(wx.Panel):

   # TODO possibly break this up
   def __init__(self, parent):
      super(WhiteboardNav, self).__init__(parent)
      
      self.shapes = []
      self.parent = parent
      self.presentation = EClass.GetInstance().presentation
      self.whiteboard = wx.html.HtmlWindow(self, -1, style = wx.DOUBLE_BORDER)
      self.whiteboard.Layout()
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent())
      
      # TODO add to list of ivars in docs
      self.notesTextbox = None
      self.notesPos = None

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
      self.whiteboard.Bind(wx.EVT_LEFT_DOWN, self.OnClickChange)
      self.Bind(wx.EVT_PAINT, self.DisplayLayers)
      self.Show()

   # TODO documentation
   def OnClickChange(self, evt):
      NOTES_OFFSET = 100
      curTool = EClass.GetInstance().drawingTools.selectedTool
      whiteboardMousePos = self.whiteboard.ScreenToClient(wx.GetMousePosition())
      
      if curTool == 'Pencila':
         pass
      elif curTool == 'Hand':
         pass
      elif curTool == 'Attachment':
         pass
      elif curTool == 'Text':
         # Ensure the user does not create tons of new text boxes
         if self.notesTextbox:
            self.notesTextbox.Destroy()
            self.notesTextbox = None
         
         # new Point because wx doesn't like Points being shared...
         self.notesPos = wx.Point(whiteboardMousePos.x, whiteboardMousePos.y)
         self.notesTextbox = wx.TextCtrl(self, pos = wx.Point(
            self.notesPos.x + NOTES_OFFSET, self.notesPos.y),
            style = wx.TE_PROCESS_ENTER
         )
         self.notesTextbox.Bind(wx.EVT_TEXT_ENTER, self.NotesTextEntered)
         self.notesTextbox.SetHint('Enter some text and hit <enter>')
         self.notesTextbox.SetBackgroundStyle(wx.BG_STYLE_PAINT)
         self.notesTextbox.SetFocus()
      elif curTool == 'Circle Shape':
         pass
      elif curTool == 'Pencil':
         EClass.GetInstance().layerManagerModel.AddObject({'type': 'Square',
            'position': whiteboardMousePos
         })
      elif curTool == 'Triangle Shape':
         pass
      self.Redraw()
      return
   
   # TODO documentation
   def NotesTextEntered(self, event):
      EClass.GetInstance().layerManagerModel.AddObject({'type': 'Text',
         'position': self.notesPos,
         'text': self.notesTextbox.GetValue()
      })
      self.notesTextbox.Destroy()
      self.notesTextbox = None
      self.Redraw()
   
   # TODO documentation
   def DisplayLayers(self, evt = None):
      try:
         dc = wx.ClientDC(self.whiteboard)
         import sys
         if not sys.platform.startswith('darwin'):
            dc = wx.GraphicsContext.Create(dc)
            dc.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL), wx.Colour(0, 0, 0, 255)
            )
         dc.SetBrush(wx.Brush(wx.Colour(100, 100, 100, 100), wx.SOLID))
         layers = EClass.GetInstance().layerManagerModel.layers
         layers.reverse()
         
         for layer in layers:
            dc.SetBrush(wx.Brush(wx.Colour(100, 100, 100, layer.opacity), wx.SOLID))
            if layer.visible:
               for obj in layer.objects:
                  if obj['type'] == 'Text':
                     dc.DrawText(obj['text'], obj['position'].x, obj['position'].y)
                  elif obj['type'] == 'Square':
                     dc.DrawRectangle(obj['position'].x, obj['position'].y, 50, 50)
      except:
         print('Furq!')

   def MoveToPreviousSlide(self, event):
      if self.presentation.MoveToPreviousSlide():
         self.Redraw()

   def MoveToNextSlide(self, event):
      if self.presentation.MoveToNextSlide():
         self.Redraw()
         
   def SyncWithPresenter(self, event):
      self.presentation.SyncWithPresenter()
      self.Redraw()

   def MoveToSlide(self, event):
      if self.presentation.MoveToSlide(self.slideTextbox.GetValue()):
         self.Redraw()
      self.slideTextbox.Clear()

   # TODO documentation
   def Redraw(self):
      self.RefreshSlide()
      wx.CallLater(30, self.DisplayLayers, None)

   def RefreshSlide(self):
      oldCurrLayer = EClass.GetInstance().layerManagerModel.currLayer
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent())
      EClass.GetInstance().setUpLayerManager()
      EClass.GetInstance().layerManagerModel.SetCurrentLayer(oldCurrLayer)
      self.parent.menuBar.layerManager.UpdateLayers()
      self.currSlideText.SetLabel(str(self.presentation.GetSlideNum()))
