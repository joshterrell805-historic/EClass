import wx
import sys

from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation

class EClassWindow(wx.Frame):

   def __init__(self):
      super(EClassWindow, self).__init__(None, -1, 'EClass')
      #self.Maximize()
      self.SetClientSizeWH(800, 600)
      self.SetBackgroundColour('#FFFFFF')
      self.AddMenubar()

      self.initialPrompt = InitialPrompt(self)
      self.importPresentation = ImportPresentation(self)

      self.Bind(wx.EVT_CLOSE, sys.exit)

      self.Show()


   def AddMenubar(self):
      menuBar = wx.MenuBar()

      fileMenu = wx.Menu()
      menuBar.Append(fileMenu, 'File')

      editMenu = wx.Menu()
      menuBar.Append(editMenu, 'Edit')

      viewMenu = wx.Menu()
      menuBar.Append(viewMenu, 'View')

      self.SetMenuBar(menuBar)
