import wx
import sys

from DrawingTools import DrawingTools
from DrawingToolsModel import DrawingToolsModel
from Layer import Layer
from LayerManager import LayerManager


"""

   Notes:
      -I'm not sure which models we need to import so here's a start (Mike)

   TODO:


"""


class DrawingCanvas(wx.Frame):

   def __init__(self, parent):

      wx.Frame.__init__(self, parent, id, title,
                         style = wx.DEFAULT_FRAME_STYLE | wx.WANTS_CHARS |
                                 wx.NO_FULL_REPAINT_ON_RESIZE)

      # Setup the main drawing area.

        self.drawPanel = wx.ScrolledWindow(self.topPanel, -1,
                                          style=wx.SUNKEN_BORDER|wx.NO_FULL_REPAINT_ON_RESIZE)
        self.drawPanel.SetBackgroundColour(wx.WHITE)

        self.drawPanel.EnableScrolling(True, True)
        self.drawPanel.SetScrollbars(20, 20, PAGE_WIDTH / 20, PAGE_HEIGHT / 20)

        self.drawPanel.Bind(wx.EVT_MOUSE_EVENTS, self.onMouseEvent)

        self.drawPanel.Bind(wx.EVT_IDLE, self.onIdle)
        self.drawPanel.Bind(wx.EVT_SIZE, self.onSize)
        self.drawPanel.Bind(wx.EVT_PAINT, self.onPaint)
        self.drawPanel.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.drawPanel.Bind(wx.EVT_SCROLLWIN, self.onPanelScroll)

        self.Bind(wx.EVT_TIMER, self.onIdle)




   def drawContents(self, dc):
      """
      Does the actual drawing of all drawing contents with the specified dc
      """
      # PrepareDC sets the device origin according to current scrolling
      scrollingelf.drawPanel.PrepareDC(dc)

      gdc = self.wrapDC(dc)

      # First pass draws objects
      ordered_selection = []
      for obj in self.contents[::-1]:
         if obj in self.selection:
            obj.draw(gdc, True)
            ordered_selection.append(obj)
         else:
            obj.draw(gdc, False)

      # First pass draws objects
      if self.curTool is not None:
         self.curTool.draw(gdc)

      # Second pass draws selection handles so they're always on top
      for obj in ordered_selection:
         obj.drawHandles(gdc)



