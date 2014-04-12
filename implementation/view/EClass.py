import wx
import sys

sys.path.insert(0, '../model')
from LoginWindow import LoginWindow
from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation
from Presentation import Presentation
from Person import Person

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
      user = Person(self.loginWindow.GetUsername(), self.loginWindow.GetPassword
         ()
      )
      user.Login()
      self.loginWindow.Close()
      self.Show()

   def Exit(self, event):
      sys.exit()

   def CreatePresentation(self, event):
      self.initialPrompt.Hide()

   def UsePresentation(self, event):
      self.initialPrompt.Hide()
      self.importPresentation = ImportPresentation(self.SelectPresentation, 
         self.CancelSelectPresentation
      )
      self.importPresentation.Show()

   def SelectPresentation(self, event):
      self.presentation = Presentation(self.importPresentation
         .GetPresentationPath()
      )
      self.presentation.ShowPresentation()

   def CancelSelectPresentation(self, event):
      self.initialPrompt.Show()
      self.importPresentation.Destroy()
