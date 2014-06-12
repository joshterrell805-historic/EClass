import wx
import sys

from LayerView import LayerView
from NewLayerWindow import NewLayerWindow

#model
sys.path.insert(0, 'model')
from EClass import EClass

class LayerManager(wx.Frame):
   def __init__(self, parent):
      super(LayerManager, self).__init__(None, size = (300,400))
      self.parent = parent
      self.layers = []

      self.sizer = wx.BoxSizer(wx.VERTICAL)
      controls = wx.BoxSizer(wx.HORIZONTAL)
      self.selectedLayer = 0

      self.slider = wx.Slider(self, -1, 0, 0, 255, size = (100, 40))
      self.slider.Bind(wx.EVT_SLIDER, self.ChangeOpacity)
      trash = wx.Button(self, -1, 'X', size = (20, 40))
      trash.Bind(wx.EVT_BUTTON, self.DeleteLayer)
      add = wx.Button(self, -1, '+', size = (20, 40))
      add.Bind(wx.EVT_BUTTON, self.NewLayer)
      label = wx.StaticText(self, -1, 'Opacity:', size = (80, 40), style=wx.ALIGN_CENTER)
      

      EClass.GetInstance().setUpLayerManager()
      self.layerDisplay = wx.BoxSizer(wx.VERTICAL)
      for layer in EClass.GetInstance().layerManagerModel.layers:
         view = LayerView(self, layer)
         self.layers.append(view)
         self.layerDisplay.Add(view.LayerListObject(self))
         self.layerDisplay.Add(wx.StaticLine(self, -1, (25, 50), (250,1)))

      controls.Add(label, 1)
      controls.Add(self.slider, 1)
      controls.Add(trash, 1)
      controls.Add(add, 1)

      self.sizer.Add(controls)
      self.sizer.Add(wx.StaticLine(self, -1, (25, 50), (250,1)))
      self.sizer.Add(self.layerDisplay)

      self.sizer.SetMinSize(size = (100,10))
      self.SetSizer(self.sizer)
      self.Bind(wx.EVT_CLOSE, self.OnClose)

   def DeleteLayer(self, event):
      EClass.GetInstance().layerManagerModel.DeleteLayer(self.selectedLayer)
      self.UpdateLayers()
      self.parent.parent.whiteboard.Redraw()

   def NewLayer(self, event):
      newLayerWindow = NewLayerWindow(self)

   def ChangeOpacity(self, event):
      EClass.GetInstance().layerManagerModel.ChangeOpacity(self.selectedLayer, self.slider.GetValue())
      self.parent.parent.whiteboard.Redraw()
   
   def UpdateLayers(self):
      i = 0
      self.sizer.Hide(2)
      self.sizer.Detach(2)
      self.layerDisplay = wx.BoxSizer(wx.VERTICAL)
      for layer in EClass.GetInstance().layerManagerModel.layers:
         view = LayerView(self, layer)
         self.layers.append(view)
         if(i == self.selectedLayer):
            self.slider.SetValue(layer.opacity)
            checked = True
         else:
            checked = False
         self.layerDisplay.Add(view.LayerListObject(self, i, checked))
         i += 1
         self.layerDisplay.Add(wx.StaticLine(self, -1, (25, 50), (250,1)))
      self.sizer.Add(self.layerDisplay)
      self.sizer.Layout()

   def OnClose(self, event):
      self.parent.showLayerManagerMenuItem.Check(False)
      self.Hide()
