import wx
import sys

#model
sys.path.insert(0, 'model')
from EClass import EClass
from Person.Roster import Roster

class ChangePermWindow(wx.Frame):
   def __init__(self, parent, layer):
      super(ChangePermWindow, self).__init__(parent, size = (200,400))
      self.parent = parent
      self.layer = layer
      self.sizer = wx.BoxSizer(wx.VERTICAL)
      self.controls = wx.BoxSizer(wx.HORIZONTAL)

      self.namelabel = wx.StaticText(self, -1, 'Choose Some Students:', size = (150, 40), style=wx.ALIGN_CENTER)
      otherOptions = ["All", "None"]
      self.listBox1 = wx.ListBox(choices=otherOptions + EClass.GetInstance().rosterModel.GetRoster(), name='listBox1', parent=self, size=wx.Size(184, 256), style=wx.ALIGN_CENTER)
      
      self.make = wx.Button(self, -1, 'OK', size = (100, 40), style=wx.ALIGN_CENTER)
      self.make.Bind(wx.EVT_BUTTON, self.ChangeLayerPerm)
      self.controls.AddStretchSpacer(1)
      self.controls.Add(self.make)
      self.controls.AddStretchSpacer(1)

      self.sizer.Add(self.namelabel)
      self.sizer.Add(self.listBox1)
      self.sizer.Add(self.controls)

      self.sizer.SetMinSize(size = (100,10))
      self.SetSizer(self.sizer)
      self.Show()

   def ChangeLayerPerm(self, event):
      sel = self.listBox1.GetStringSelection()
      if sel == "All":
         self.layer.permissions = EClass.GetInstance().rosterModel.GetRoster()
         print(''.join(self.layer.permissions) + " add to permissions on " + self.layer.name)
      elif sel == "None":
         self.layer.permissions = []
         print("Removed all layer permissions from" + self.layer.name)
      else:
         self.layer.permissions.append(sel)
      self.Destroy()
