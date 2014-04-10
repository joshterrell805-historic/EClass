import wx
import sys

from LoginWindow import LoginWindow
from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation
sys.path.insert(0, '..\model')
from Presentation import Presentation

class EClass(wx.Frame):
   """EClass is a window"""

   def __init__(self):
      super(EClass, self).__init__(None, -1, 'EClass')
      self.Maximize()
      self.SetBackgroundColour('#FFFFFF')
      self.AddMenubar()

      self.loginWindow = LoginWindow(self.LoginSuccessful, self.Exit)
      self.loginWindow.Show()

      self.initialPrompt = InitialPrompt(self, self.CreatePresentation, 
         self.UsePresentation
      )

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
      self.initialPrompt.Hide()
      print('Create Presentation')

   def UsePresentation(self, event):
      self.initialPrompt.Hide()
      self.importPresentation = ImportPresentation(self.SelectPresentation, 
         self.CancelSelectPresentation
      )
      self.importPresentation.Show()
      print('Use Presentation')

   def SelectPresentation(self, event):
      """
      Controller for the Select buttin in the ImportPresentation Window. Gets the
      Presentation file path from the ImportPresentation object instantiates
      a new Presentation object with the path and calls ShowPresentation().
      """
      self.presentation = Presentation(self.importPresentation
         .GetPresentationPath()
      )
      self.presentation.ShowPresentation()

   def CancelSelectPresentation(self, event):
      self.initialPrompt.Show()
      self.importPresentation.Destroy()
      print('Cancel Select Presentation')
