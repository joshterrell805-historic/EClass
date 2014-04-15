import wx
import sys

from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation
from MenuBar import MenuBar

class EClassWindow(wx.Frame):

   def __init__(self):
      super(EClassWindow, self).__init__(None, -1, 'EClass')
      #self.Maximize()
      self.SetClientSizeWH(800, 600)
      self.SetBackgroundColour('#FFFFFF')
      self.menuBar = MenuBar(self)
      self.CreateStatusBar()

      self.initialPrompt = InitialPrompt(self)
      self.importPresentation = ImportPresentation(self)

      self.Bind(wx.EVT_CLOSE, sys.exit)

      self.Show()
