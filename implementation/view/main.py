import wx
import sys

from EClass import EClass

if __name__ == "__main__":
    app = wx.App(False)
    EClass = EClass()
    app.MainLoop()
sys.exit(1)
