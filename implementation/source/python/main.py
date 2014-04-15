import wx
import sys

sys.path.insert(0, 'model')
sys.path.insert(0, 'view')

from LoginWindow import LoginWindow


if __name__ == "__main__":
   nullLog = wx.LogNull()
   app = wx.App(False)
   LoginWindow()
   app.MainLoop()
   sys.exit(1)
