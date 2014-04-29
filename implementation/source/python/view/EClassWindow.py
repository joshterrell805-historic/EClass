import wx
import sys

from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation
from MenuBar import MenuBar

sys.path.insert(0, 'model')
from EClass import EClass

class EClassWindow(wx.Frame):

   def __init__(self):
      super(EClassWindow, self).__init__(None, -1, 'EClass')
      self.SetClientSizeWH(800, 600)
      self.SetBackgroundColour('#FFFFFF')
      self.menuBar = MenuBar(self)
      self.CreateStatusBar()

      self.initialPrompt = InitialPrompt(self)
      self.importPresentation = ImportPresentation(self)

      self.Bind(wx.EVT_CLOSE, self.onClose)

      self.Centre()
      self.Show()

   def onClose(self, event):
      EClass.GetInstance().exit()
      sys.exit()
