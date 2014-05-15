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

      