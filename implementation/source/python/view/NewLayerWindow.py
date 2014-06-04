import wx
import sys

from ChangePermWindow import ChangePermWindow

#model
sys.path.insert(0, 'model')
from EClass import EClass
from Presentation.Layer import Layer

class NewLayerWindow(wx.Frame):
   def __init__(self, parent):
      super(NewLayerWindow, self).__init__(parent, size = (350,300))
      self.parent = parent
      self.layers = self.parent.layers
      self.sizer = wx.BoxSizer(wx.VERTICAL)
      self.nameline = wx.BoxSizer(wx.HORIZONTAL) 
      self.opacityline  = wx.BoxSizer(wx.HORIZONTAL)
      self.permline = wx.BoxSizer(wx.HORIZONTAL)
      self.controls = wx.BoxSizer(wx.HORIZONTAL)

      self.namelabel = wx.StaticText(self, -1, 'Name:', size = (150, 40), style=wx.ALIGN_CENTER)
      self.newname = wx.TextCtrl(self, size=(140, -1))
      self.nameline.Add(self.namelabel, 1)
      self.nameline.Add(self.newname, 1)
      
      self.opacitylabel = wx.StaticText(self, -1, 'Opacity:', size = (150, 40), style=wx.ALIGN_CENTER)
      self.slider = wx.Slider(self, -1, 0, 0, 255, size = (140, -1))
      self.slider.SetValue(255)
      self.opacityline.Add(self.opacitylabel, 1)
      self.opacityline.Add(self.slider, 1)
      
      self.permlabel = wx.StaticText(self, -1, 'Permissions:', size = (150, 40), style=wx.ALIGN_CENTER)
      self.trash = wx.Button(self, -1, 'Change', size = (20, 40))
      self.trash.Bind(wx.EVT_BUTTON, self.ChangePermissions)
      self.permline.Add(self.permlabel, 1)
      self.permline.Add(self.trash, 1)
      
      self.make = wx.Button(self, -1, 'OK', size = (100, 40))
      self.make.Bind(wx.EVT_BUTTON, self.MakeNewLayer)
      self.controls.Add(self.make, 1)

      self.sizer.Add(self.nameline)
      self.sizer.Add(self.opacityline)
      self.sizer.Add(self.permline)
      self.sizer.Add(self.controls)

      self.sizer.SetMinSize(size = (100,10))
      self.SetSizer(self.sizer)
      self.Show()

   def MakeNewLayer(self, event):
      self.layer = Layer(self.newname.GetValue(), self.slider.GetValue(), False)
      EClass.GetInstance().layerManagerModel.NewLayer(self.layer)
      self.parent.UpdateLayers()
      self.Destroy()
      print("Made Layer:" + self.layer.name + " added to layerManager")
      
   def ChangePermissions(self, event):
      self.changeLayerPerm = ChangePermWindow(self, self.layer)
