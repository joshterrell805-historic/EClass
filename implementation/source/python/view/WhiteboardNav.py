import wx, wx.html, wx.html2, wx.lib.intctrl
import sys

sys.path.insert(0, 'model')
from EClass import EClass
from Person.Student import Student

class DoodleWindow(wx.Window):
    menuColours = { 100 : 'Black',
                    101 : 'Yellow',
                    102 : 'Red',
                    103 : 'Green',
                    104 : 'Blue',
                    105 : 'Purple',
                    106 : 'Brown',
                    107 : 'Aquamarine',
                    108 : 'Forest Green',
                    109 : 'Light Blue',
                    110 : 'Goldenrod',
                    111 : 'Cyan',
                    112 : 'Orange',
                    113 : 'Navy',
                    114 : 'Dark Grey',
                    115 : 'Light Grey',
                    }
    maxThickness = 16


    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID, style=wx.NO_FULL_REPAINT_ON_RESIZE)
        # self.SetBackgroundColour("WHITE")
        self.listeners = []
        self.thickness = 1
        self.SetColour("Black")
        self.lines = []
        self.x = self.y = 0
        self.MakeMenu()
        self.InitBuffer()

        # hook some mouse events
        wx.EVT_LEFT_DOWN(self, self.OnLeftDown)
        wx.EVT_LEFT_UP(self, self.OnLeftUp)
        wx.EVT_RIGHT_UP(self, self.OnRightUp)
        wx.EVT_MOTION(self, self.OnMotion)

        # the window resize event and idle events for managing the buffer
        wx.EVT_SIZE(self, self.OnSize)
        wx.EVT_IDLE(self, self.OnIdle)

        # and the refresh event
        wx.EVT_PAINT(self, self.OnPaint)

        # When the window is destroyed, clean up resources.
        wx.EVT_WINDOW_DESTROY(self, self.Cleanup)


    def Cleanup(self, evt):
        if hasattr(self, "menu"):
            self.menu.Destroy()
            del self.menu


    def InitBuffer(self):
        """Initialize the bitmap used for buffering the display."""
        size = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.SetBackgroundMode(wx.TRANSPARENT)
        dc.Clear()
        self.DrawLines(dc)
        self.reInitBuffer = False


    def SetColour(self, colour):
        """Set a new colour and make a matching pen"""
        self.colour = colour
        self.pen = wx.Pen(self.colour, self.thickness, wx.SOLID)
        self.Notify()


    def SetThickness(self, num):
        """Set a new line thickness and make a matching pen"""
        self.thickness = num
        self.pen = wx.Pen(self.colour, self.thickness, wx.SOLID)
        self.Notify()


    def GetLinesData(self):
        return self.lines[:]


    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()


    def MakeMenu(self):
        """Make a menu that can be popped up later"""
        menu = wx.Menu()
        keys = self.menuColours.keys()
        keys.sort()
        for k in keys:
            text = self.menuColours[k]
            menu.Append(k, text, kind=wx.ITEM_CHECK)
        wx.EVT_MENU_RANGE(self, 100, 200, self.OnMenuSetColour)
        wx.EVT_UPDATE_UI_RANGE(self, 100, 200, self.OnCheckMenuColours)
        menu.Break()

        for x in range(1, self.maxThickness+1):
            menu.Append(x, str(x), kind=wx.ITEM_CHECK)
        wx.EVT_MENU_RANGE(self, 1, self.maxThickness, self.OnMenuSetThickness)
        wx.EVT_UPDATE_UI_RANGE(self, 1, self.maxThickness, self.OnCheckMenuThickness)
        self.menu = menu


    # These two event handlers are called before the menu is displayed
    # to determine which items should be checked.
    def OnCheckMenuColours(self, event):
        text = self.menuColours[event.GetId()]
        if text == self.colour:
            event.Check(True)
            event.SetText(text.upper())
        else:
            event.Check(False)
            event.SetText(text)

    def OnCheckMenuThickness(self, event):
        if event.GetId() == self.thickness:
            event.Check(True)
        else:
            event.Check(False)


    def OnLeftDown(self, event):
        """called when the left mouse button is pressed"""
        self.curLine = []
        self.x, self.y = event.GetPositionTuple()
        self.CaptureMouse()


    def OnLeftUp(self, event):
        """called when the left mouse button is released"""
        if self.HasCapture():
            self.lines.append( (self.colour, self.thickness, self.curLine) )
            self.curLine = []
            self.ReleaseMouse()


    def OnRightUp(self, event):
        """called when the right mouse button is released, will popup the menu"""
        pt = event.GetPosition()
        self.PopupMenu(self.menu, pt)



    def OnMotion(self, event):
        """
        Called when the mouse is in motion.  If the left button is
        dragging then draw a line from the last event position to the
        current one.  Save the coordinants for redraws.
        """
        if event.Dragging() and event.LeftIsDown():
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            dc.BeginDrawing()
            dc.SetPen(self.pen)
            pos = event.GetPositionTuple()
            coords = (self.x, self.y) + pos
            self.curLine.append(coords)
            dc.DrawLine(self.x, self.y, pos[0], pos[1])
            self.x, self.y = pos
            dc.EndDrawing()


    def OnSize(self, event):
        """
        Called when the window is resized.  We set a flag so the idle
        handler will resize the buffer.
        """
        self.reInitBuffer = True


    def OnIdle(self, event):
        """
        If the size was changed then resize the bitmap used for double
        buffering to match the window size.  We do it in Idle time so
        there is only one refresh after resizing is done, not lots while
        it is happening.
        """
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)


    def OnPaint(self, event):
        """
        Called when the window is exposed.
        """
        # Create a buffered paint DC.  It will create the real
        # wx.PaintDC and then blit the bitmap to it when dc is
        # deleted.  Since we don't need to draw anything else
        # here that's all there is to it.
        dc = wx.BufferedPaintDC(self)


    def DrawLines(self, dc):
        """
        Redraws all the lines that have been drawn already.
        """
        dc.BeginDrawing()
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                apply(dc.DrawLine, coords)
        dc.EndDrawing()


    # Event handlers for the popup menu, uses the event ID to determine
    # the colour or the thickness to set.
    def OnMenuSetColour(self, event):
        self.SetColour(self.menuColours[event.GetId()])

    def OnMenuSetThickness(self, event):
        self.SetThickness(event.GetId())


    # Observer pattern.  Listeners are registered and then notified
    # whenever doodle settings change.
    def AddListener(self, listener):
        self.listeners.append(listener)

    def Notify(self):
        for other in self.listeners:
            other.Update(self.colour, self.thickness)

class WhiteboardNav(wx.Panel):

   def __init__(self, parent):
      super(WhiteboardNav, self).__init__(parent)

      self.parent = parent
      self.presentation = EClass.GetInstance().presentation
      self.whiteboard = wx.html2.WebView.New(self, -1, style = wx.DOUBLE_BORDER)
      self.whiteboard.Layout()
      self.whiteboard.SetPage(self.presentation.GetSlide().GetContent(),
         self.presentation.GetPath()
      )
      self.RunScript()

      # self.listeners = []
      # self.thickness = 1
      # self.SetColor("Black")
      # self.lines = []
      # self.x = self.y = 0
      # self.InitBuffer()
      # wx.EVT_LEFT_DOWN(self, self.OnLeftDown)
      # wx.EVT_LEFT_UP(self, self.OnLeftUp)
      # wx.EVT_MOTION(self, self.OnMotion)
      # wx.EVT_PAINT(self, self.OnPaint)
      doodle = DoodleWindow(self, -1)



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
      self.Show()

   # def InitBuffer(self):
   #    size = self.GetClientSize()
   #    self.buffer = wx.EmptyBitmap(size.width, size.height)
   #    dc = wx.BufferedDC(None, self.buffer)
   #    dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
   #    dc.Clear()
   #    self.DrawLines(dc)
   #    self.reInitBuffer = False

   # def GetLinesData(self):
   #    return self.lines[:]

   # def SetLinesData(self, lines):
   #    self.lines = lines[:]
   #    self.InitBuffer()
   #    self.Refresh()

   # def OnLeftDown(self, event):
   #    self.curLine = []
   #    self.x, self.y = event.GetPositionTuple()
   #    self.CaptureMouse()

   # def OnLeftUp(self, event):
   #    if self.HasCapture():
   #       self.lines.append((self.color, self.thickness, self.curLine))
   #       self.curLine = []
   #       self.ReleaseMouse()

   # def OnMotion(self, event):
   #    if event.Dragging() and event.LeftIsDown():
   #       dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
   #       dc.BeginDrawing()
   #       dc.SetPen(self.pen)
   #       pos = event.GetPositionTuple()
   #       coords = (self.x, self.y) + pos
   #       slef.curLine.append(coords)
   #       dc.DrawLine(self.x, self.y, pos[0], pos[1])
   #       self.x, self.y = pos
   #       dc.EndDrawing()

   # def OnPaint(self, event):
   #    dc = wx.BufferedPaintDC(self, self.buffer)

   # def DrawLines(self, dc):
   #    dc.BeginDrawing()
   #    for color, thickness, line in self.lines:
   #       pen = wx.Pen(color, thickness, wx.SOLID)
   #       dc.SetPen(pen)
   #       for coords in line:
   #          apply(dc.DrawLine, coords)
   #    dc.EndDrawing()

   # def SetColor(self, color):
   #    self.color = color
   #    self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
   #    self.Notify()

   # def Notify(self):
   #    for other in self.listeners:
   #       other.Update(self.color, self.thickness)

   def OnPageNavigation(self, evt):
      uri = evt.GetURL()

      if "__EVENT__/mousedown" in uri:
         # dc = wx.WindowDC(self.whiteboard)
         # dc.SetBrush(wx.Brush(wx.BLACK, wx.TRANSPARENT))
         # whiteboardMousePos = self.whiteboard.ScreenToClient(wx.GetMousePosition())
         # dc.DrawCircle(whiteboardMousePos.x, whiteboardMousePos.y, 100)
         print 'mousedown'
         evt.Veto()
         return

   def MoveToPreviousSlide(self, event):
      if self.presentation.MoveToPreviousSlide():
         self.RefreshSlide()

   def MoveToNextSlide(self, event):
      if self.presentation.MoveToNextSlide():
         self.RefreshSlide()

   def SyncWithPresenter(self, event):
      self.presentation.SyncWithPresenter(self.RefreshSlide)

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