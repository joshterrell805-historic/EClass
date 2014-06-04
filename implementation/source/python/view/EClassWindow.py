import wx
import sys

from InitialPrompt import InitialPrompt
from ImportPresentation import ImportPresentation
from MenuBar import MenuBar
from WhiteboardNav import WhiteboardNav

sys.path.insert(0, 'model')
from EClass import EClass

class EClassWindow(wx.Frame):

   def __init__(self):
      super(EClassWindow, self).__init__(None, -1, 'EClass')
      self.SetClientSizeWH(800, 600)
      self.SetBackgroundColour('#FFFFFF')
      self.menuBar = MenuBar(self)
      self.CreateStatusBar()

      # Infinite recurion without using CallLater
      # EClass.GetInstance() -> Presentation() ->EClass.GetInstance() ...
      # Wait a second, then get the instance to avoid infinite recursion
      def listen():
         EClass.GetInstance().connection.registerMessageListener(
            'kick notification', self.NotifyKickedStudent
         )
      wx.CallLater(1, listen)
      
      if EClass.GetInstance().user.isPresenter():
         self.initialPrompt = InitialPrompt(self)
         self.importPresentation = ImportPresentation(self)

      self.Bind(wx.EVT_CLOSE, self.onClose)

      self.Centre()
      self.Show()

   def onClose(self, event):
      EClass.GetInstance().exit()
      sys.exit()
   def setPresentation(self, presentationHTML):
      f = open('presentation.html', 'w')
      f.write(presentationHTML)
      f.close()
      EClass.GetInstance().setPresentation('presentation.html')
      self.menuBar.layerManager.UpdateLayers()
      self.whiteboard = WhiteboardNav(self)
      self.SendSizeEvent()

   # TODO documentation
   def NotifyKickedStudent(self, message, student):
      if not EClass.GetInstance().user.isPresenter():
         wx.MessageBox('You have been kicked from the presentation, but you ' +
          'may continue to edit your layers and view the presentation file.', 
          'Kick Notification', wx.OK | wx.ICON_INFORMATION)