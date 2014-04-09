import wx
import sys

from LoginWindow import LoginWindow
from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation

class EClass(wx.Frame):
   """EClass is a window"""

   def __init__(self):
      super(EClass, self).__init__(None, -1, 'EClass')
      self.Maximize()
      self.SetBackgroundColour('#FFFFFF')
      self.AddMenubar()

      self.loginWindow = LoginWindow(self.LoginSuccessful, self.Exit)
      self.loginWindow.Show()

      self.initialPrompt = InitialPrompt(self, self.CreatePresentation, self.UsePresentation)
      self.initialPrompt.Show()  

   def AddMenubar(self):
      menuBar = wx.MenuBar()

      fileMenu = wx.Menu()
      menuBar.Append(fileMenu, 'File')

      editMenu = wx.Menu()
      menuBar.Append(editMenu, 'Edit')

      viewMenu = wx.Menu()
      menuBar.Append(viewMenu, 'View')

      self.SetMenuBar(menuBar)

   def LoginSuccessful(self, event):
      self.loginWindow.Close()
      self.Show()

   def Exit(self, event):
      sys.exit()

   def CreatePresentation(self, event):
      self.initialPrompt.Destroy()
      print('Create Presentation')

   def UsePresentation(self, event):
      self.initialPrompt.Destroy()
      self.importPresentation = ImportPresentation()
      self.importPresentation.Show()
      print('Use Presentation')
