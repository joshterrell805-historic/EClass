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
      self.sizer = wx.BoxSizer(wx.VERTICAL)
      self.controls = wx.BoxSizer(wx.HORIZONTAL)
      self.selectedLayer = 0

      self.slider = wx.Slider(self, -1, 0, 0, 255, size = (100, 40))
      self.slider.Bind(wx.EVT_SLIDER, self.ChangeOpacity)
      self.trash = wx.Button(self, -1, 'X', size = (20, 40))
      self.trash.Bind(wx.EVT_BUTTON, self.DeleteLayer)
      self.add = wx.Button(self, -1, '+', size = (20, 40))
      self.add.Bind(wx.EVT_BUTTON, self.NewLayer)
      self.label = wx.StaticText(self, -1, 'Opacity:', size = (80, 40), style=wx.ALIGN_CENTER)

      self.layerDisplay = wx.BoxSizer(wx.VERTICAL)
      self.layers = []

      EClass.GetInstance().setUpLayerManager()

      for layer in EClass.GetInstance().layerManagerModel.layers:
         view = LayerView(self, layer)
         self.layers.append(view)
         self.layerDisplay.Add(view.layerListObject(self))
         self.layerDisplay.Add(wx.StaticLine(self, -1, (25, 50), (250,1)))

      self.controls.Add(self.label, 1)
      self.controls.Add(self.slider, 1)
      self.controls.Add(self.trash, 1)
      self.controls.Add(self.add, 1)

      self.sizer.Add(self.controls)
      self.sizer.Add(wx.StaticLine(self, -1, (25, 50), (250,1)))
      self.sizer.Add(self.layerDisplay)

      self.sizer.SetMinSize(size = (100,10))
      self.SetSizer(self.sizer)
      self.Bind(wx.EVT_CLOSE, self.onClose)

   def DeleteLayer(self, event):
      EClass.GetInstance().layerManagerModel.DeleteLayer(self.selectedLayer)
      self.UpdateLayers()
      self.parent.parent.whiteboard.Redraw()

   def NewLayer(self, event):
      self.newLayerWindow = NewLayerWindow(self)

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
         self.layerDisplay.Add(view.layerListObject(self, i, checked))
         i += 1
         self.layerDisplay.Add(wx.StaticLine(self, -1, (25, 50), (250,1)))
      self.sizer.Add(self.layerDisplay)
      self.sizer.Layout()

   def onClose(self, event):
      self.parent.showLayerManagerMenuItem.Check(False)
      self.Hide()
