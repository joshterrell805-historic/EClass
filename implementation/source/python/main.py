import wx
import sys

sys.path.insert(0, 'model')
sys.path.insert(0, 'view')

from LoginWindow import LoginWindow


if __name__ == "__main__":
   if len(sys.argv) == 2 and sys.argv[1] == 'server':
      import Connection.CentralServer
   else:
      nullLog = wx.LogNull()
      app = wx.App(False)
      LoginWindow()
      app.MainLoop()
      sys.exit(1)
