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
      self.layer = Layer()
      sizer = wx.BoxSizer(wx.VERTICAL)
      nameline = wx.BoxSizer(wx.HORIZONTAL) 
      opacityline  = wx.BoxSizer(wx.HORIZONTAL)
      permline = wx.BoxSizer(wx.HORIZONTAL)
      controls = wx.BoxSizer(wx.HORIZONTAL)

      namelabel = wx.StaticText(self, -1, 'Name:', size = (150, 40), style=wx.ALIGN_CENTER)
      self.newname = wx.TextCtrl(self, size=(140, -1))
      nameline.Add(namelabel, 1)
      nameline.Add(self.newname, 1)
      
      opacitylabel = wx.StaticText(self, -1, 'Opacity:', size = (150, 40), style=wx.ALIGN_CENTER)
      self.slider = wx.Slider(self, -1, 0, 0, 255, size = (140, -1))
      self.slider.SetValue(255)
      opacityline.Add(opacitylabel, 1)
      opacityline.Add(self.slider, 1)
      
      permlabel = wx.StaticText(self, -1, 'Permissions:', size = (150, 40), style=wx.ALIGN_CENTER)
      trash = wx.Button(self, -1, 'Change', size = (20, 40))
      trash.Bind(wx.EVT_BUTTON, self.ChangePermissions)
      permline.Add(permlabel, 1)
      permline.Add(trash, 1)
      
      make = wx.Button(self, -1, 'OK', size = (100, 40))
      make.Bind(wx.EVT_BUTTON, self.MakeNewLayer)
      controls.Add(make, 1)

      sizer.Add(nameline)
      sizer.Add(opacityline)
      sizer.Add(permline)
      sizer.Add(controls)

      sizer.SetMinSize(size = (100,10))
      self.SetSizer(sizer)
      self.Show()

   def MakeNewLayer(self, event):
      self.layer.ChangeName(self.newname.GetValue())
      self.layer.SetOpacity(self.slider.GetValue())
      EClass.GetInstance().layerManagerModel.NewLayer(self.layer)
      self.parent.UpdateLayers()
      self.Destroy()
      
   def ChangePermissions(self, event):
      self.changeLayerPerm = ChangePermWindow(self, self.layer)
