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
      self.__lastRedraw = None
      self.__redrawScheduled = False
      
      self.__activeTool = None
      self.shapes = []
      self.parent = parent
      self.selectedObj = None
      self.presentation = EClass.GetInstance().presentation
      self.whiteboard = wx.html.HtmlWindow(self, -1, style = wx.DOUBLE_BORDER)
      self.whiteboard.Layout()
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent())
      
      EClass.GetInstance().RefreshSlide = self.RefreshSlide
      EClass.GetInstance().Redraw = self.Redraw
      
      # TODO add to list of ivars in docs
      self.notesTextbox = None
      self.notesPos = None

      self.previousSlideButton = wx.Button(self, label = '<< Previous',
         size = (70, 30)
      )
      self.previousSlideButton.Bind(wx.EVT_BUTTON, self.MoveToPreviousSlide)

      self.nextSlideButton = wx.Button(self, label = 'Next >>', size = (70, 30))
      self.nextSlideButton.Bind(wx.EVT_BUTTON, self.MoveToNextSlide)

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
         self.syncButton = wx.Button(self, label = 'SYNC', size = (120, 15))
         self.syncButton.Bind(wx.EVT_BUTTON, self.SyncWithPresenter)
         navVertSizer.Add(self.syncButton, 3, wx.CENTER)
      navVertSizer.AddStretchSpacer(1)

      navHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      navHoriSizer.AddStretchSpacer(1)
      navHoriSizer.Add(self.previousSlideButton, 1, wx.CENTER)
      navHoriSizer.Add(navVertSizer, 1, flag = wx.LEFT|wx.RIGHT|wx.CENTER,
         border = 20
      )
      navHoriSizer.Add(self.nextSlideButton, 1, wx.CENTER)
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
      self.whiteboard.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
      self.whiteboard.Bind(wx.EVT_MOTION, self.OnMotion)

      def onScroll(evt):
         self.Redraw()
      self.whiteboard.Bind(wx.EVT_SCROLLWIN, onScroll)

      self.Bind(wx.EVT_PAINT, self.DisplayLayers)
      self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
      self.Show()
      
      def listen():
         EClass.GetInstance().connection.registerMessageListener(
            'lockdown', self.LockdownMode
         )
      wx.CallLater(1, listen)
      
   # TODO docs
   def LockdownMode(self, message, student):
      if not EClass.GetInstance().user.isPresenter():
         if message['on']:
            self.previousSlideButton.Disable()
            self.nextSlideButton.Disable()
            self.syncButton.Disable()
            self.slideTextbox.SetEditable(False)
         else:
            self.previousSlideButton.Enable()
            self.nextSlideButton.Enable()
            self.syncButton.Enable()
            self.slideTextbox.SetEditable(True)
      
   def onKey(self, evt):
      if evt.GetKeyCode() == wx.WXK_DELETE or evt.GetKeyCode() == wx.WXK_BACK:
         if not self.selectedObj == None:
            EClass.GetInstance().layerManagerModel.RemoveObject(self.selectedObj)
            self.Redraw()
      else:
         evt.Skip()

   # TODO documentation
   def OnClickChange(self, evt):
      NOTES_OFFSET = 100
      curTool = EClass.GetInstance().drawingTools.selectedTool
      whiteboardMousePos = self.whiteboard.ScreenToClient(wx.GetMousePosition())
      self.__activeTool = curTool

      if curTool == 'Pencil':
         self.__currentLine = []
         EClass.GetInstance().layerManagerModel.AddObject({'type': 'Pencil',
            'points' : self.__currentLine
         })
         self.__currentLine.append(whiteboardMousePos)
         #self.CaptureMouse()
      elif curTool == 'Hand':
         self.selectedObj = self.findSelectedObject(whiteboardMousePos)
         self.leftdown = whiteboardMousePos
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
      elif curTool == 'Square Shape':
         EClass.GetInstance().layerManagerModel.AddObject({'type': 'Square',
            'position': whiteboardMousePos,
            'x_size': 100,
            'y_size': 100
         })
      elif curTool == 'Triangle Shape':
         pass
      elif curTool == None:
         pass
      else:
         assert False, 'Unknown drawing tool: ' + curTool

      self.Redraw()
      return
      
   def findSelectedObject(self, mousePos):
      lmm = EClass.GetInstance().layerManagerModel
      layer = lmm.layers[lmm.currLayer]
      for obj in layer.objects:
         if obj['type'] == 'Text' and obj['position'].x <= mousePos.x  and (obj['position'].x + (len(obj['text']) * 6)) >= mousePos.x and obj['position'].y <= mousePos.y and (obj['position'].y + 15) >= mousePos.y:
             return obj
         elif obj['type'] == 'Square' and obj['position'].x <= mousePos.x and (obj['position'].x + obj['x_size']) >= mousePos.x and obj['position'].y <= mousePos.y and (obj['position'].y + obj['y_size']) >= mousePos.y:
            return obj
         elif obj['type'] == 'Pencil':
            for pos in obj['points']:
               if pos.x + 10 >= mousePos.x and pos.x - 10 <= mousePos.x and pos.y + 10 >= mousePos.y and pos.y - 10 <= mousePos.y:
                  return obj

   def OnLeftUp(self, event):
      # drawing with pencil
      if self.__activeTool == 'Pencil':
         assert EClass.GetInstance().drawingTools.selectedTool == 'Pencil'
         # TODO were gonna remove redraw and use double buffering.. for now
         # this just draws after the complete motion is done.
         self.Redraw()
      elif self.__activeTool == 'Hand' and not self.selectedObj == None:
         assert EClass.GetInstance().drawingTools.selectedTool == 'Hand'
         newWhiteboardMousePos = self.whiteboard.ScreenToClient(wx.GetMousePosition())  
         EClass.GetInstance().layerManagerModel.ChangeObjPos(self.selectedObj, self.leftdown, newWhiteboardMousePos)
         self.Redraw()

      self.__activeTool = None

   def OnMotion(self, event):
      if self.__activeTool == 'Pencil':
         assert event.Dragging() and event.LeftIsDown()
         assert EClass.GetInstance().drawingTools.selectedTool == 'Pencil'
         pos = self.whiteboard.ScreenToClient(wx.GetMousePosition())
         self.__currentLine.append(pos)
         self.Redraw()
   
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
         isTrueDC = True
         if not sys.platform.startswith('darwin'):
            isTrueDC = False
            dc = wx.GraphicsContext.Create(dc)
            dc.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL), wx.Colour(0, 0, 0, 255)
            )
      except:
         print('Furq!')

      layers = EClass.GetInstance().layerManagerModel.layers
      layers.reverse()
      
      for layer in layers:
         # TODO colors per object?
         dc.SetBrush(wx.Brush(wx.Colour(100, 100, 100, layer.opacity), wx.SOLID))
         dc.SetPen(wx.Pen(
            wx.Colour(0, 0, 0, layer.opacity),
            1,
            wx.PENSTYLE_SOLID
         ))
         if layer.visible:
            for obj in layer.objects:
               if obj['type'] == 'Text':
                  dc.DrawText(obj['text'], obj['position'].x, obj['position'].y)
               elif obj['type'] == 'Square':
                  dc.DrawRectangle(obj['position'].x, obj['position'].y, obj['x_size'], obj['x_size'])
               elif obj['type'] == 'Pencil':
                  #dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
                  #dc.BeginDrawing()
                  #dc.SetPen(self.pen)

                  # TODO this is unecessary cpu work to do this every draw.
                  prev = { 'point' : None }
                  def toLines(lines, point):
                     if not prev['point'] == None:
                        lines.append((
                           prev['point'].x, prev['point'].y,
                           point.x, point.y
                        ))
                     prev['point'] = point
                     return lines
                  lines = reduce(toLines, obj['points'], [])

                  if isTrueDC:
                     dc.DrawLineList(lines)
                  else:
                     for line in lines:
                        dc.StrokeLine(line[0], line[1], line[2], line[3])
                  #dc.EndDrawing()

      layers.reverse()

   def MoveToPreviousSlide(self, event):
      if self.presentation.MoveToPreviousSlide():
         self.RefreshSlide()
         self.Redraw()

   def MoveToNextSlide(self, event):
      if self.presentation.MoveToNextSlide():
         self.RefreshSlide()
         self.Redraw()
         
   def SyncWithPresenter(self, event):
      self.presentation.SyncWithPresenter()
      self.RefreshSlide()
      self.Redraw()

   def MoveToSlide(self, event):
      if self.presentation.MoveToSlide(self.slideTextbox.GetValue()):
         self.RefreshSlide()
         self.Redraw()
      self.slideTextbox.Clear()

   
   # TODO documentation
   # only redraw at max every 30 ms.. reduce flickering and lag
   def Redraw(self):
      def millis():
        return int(round(time.time() * 1000))
      def redraw():
         self.__lastRedraw = millis()
         self.whiteboard.Refresh()
         self.Update()
         self.DisplayLayers()
      def scheduledRedraw():
         self.__redrawScheduled = False
         redraw()

      if not self.__redrawScheduled:
         # if we haven't drawn yet or it's been at least 30 ms, just draw now
         if self.__lastRedraw is None or millis() - self.__lastRedraw > 30:
            redraw()
         # else weve drawn before and it hasn't been 30 ms since our last redraw
         # schedule one to take place in less than 30 ms
         else:
            self.__redrawScheduled = True
            wx.CallLater(30 - (millis() - self.__lastRedraw), scheduledRedraw)

   def RefreshSlide(self):
      oldCurrLayer = EClass.GetInstance().layerManagerModel.currLayer
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent())
      EClass.GetInstance().setUpLayerManager()
      EClass.GetInstance().layerManagerModel.SetCurrentLayer(oldCurrLayer)
      self.parent.menuBar.layerManager.UpdateLayers()
      self.currSlideText.SetLabel(str(self.presentation.GetSlideNum()))
