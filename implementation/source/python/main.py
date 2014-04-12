import wx
import sys

sys.path.insert(0, 'model')
sys.path.insert(0, 'view')
from EClass import EClass

if __name__ == "__main__":
   app = wx.App(False)
   EClass = EClass()
   app.MainLoop()
   sys.exit(1)
