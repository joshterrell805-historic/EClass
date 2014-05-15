import wx
import sys

sys.path.insert(0, 'model/Person')
from EClass import EClass

from RosterItem import RosterItem

class RosterStaticPanel(wx.Panel):
   # TODO Update doc
   def __init__(self, parent):
      super(RosterStaticPanel, self).__init__(parent, -1)

      self.sizer = wx.BoxSizer(wx.VERTICAL)
      self.SetBackgroundColour('#FEEECC')
      
