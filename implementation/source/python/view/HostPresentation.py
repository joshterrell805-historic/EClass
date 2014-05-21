import wx, sys
from EClassWindow import EClassWindow
sys.path.insert(0, 'model')
from EClass import EClass
sys.path.insert(0, 'model/Connection')
from __init__ import Connection
 
class HostPresentation(wx.Frame):
 
   def __init__(self, parent):
      wx.Frame.__init__(self, None, wx.ID_ANY)
      self.SetLabel('Select a Presentation to Host')

      panel = wx.Panel(self, wx.ID_ANY)
      self.index = 0
      self.parent = parent

      self.list_ctrl = wx.ListCtrl(panel, size=(-1,100),
         style=wx.LC_REPORT
         |wx.BORDER_SUNKEN
      )

      self.list_ctrl.InsertColumn(0, 'Class')

      btn = wx.Button(panel, label="Host")
      btn.Bind(wx.EVT_BUTTON, self.host)

      sizer = wx.BoxSizer(wx.VERTICAL)
      sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
      sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
      panel.SetSizer(sizer)
      self.Bind(wx.EVT_CLOSE, self.onClose)

      self.setClasses(EClass.GetInstance().classes)

   def setClasses(self, classes):
      self.list_ctrl.DeleteAllItems()
      for c in classes:
         self.list_ctrl.Append((c['name'],))

   def onClose(self, event):
      EClass.GetInstance().exit()

   def host(self, event):
      selected = EClass.GetInstance().classes[self.list_ctrl.GetFocusedItem()]

      Connection.getInstance().hostPresentation(selected['name'], self.callback,
         self.joinCallback
      )
      
   def callback(self):
      return true

   def joinCallback(self, username):
      return true
      
