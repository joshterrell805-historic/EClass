import wx

from EClass import EClass

class DrawingTools(wx.Frame):
   def __init__(self):
      super(DrawingTools, self).__init__(None, -1, 'Drawing Tools')

      self.SetClientSizeWH(300, 400)
      self.SetBackgroundColour('#FFFFFFF')
      self.Show()