import wx
import sys

from LayerView import LayerView

class LayerManager(wx.Frame):
   def __init__(self, parent):
      super(LayerManager, self).__init__(parent, size = (250,400))

      self.parent = parent
      self.sizer = wx.BoxSizer(wx.VERTICAL)
      self.controls = wx.BoxSizer(wx.HORIZONTAL)

      self.slider = wx.Slider(self, -1, 0, 0, 100, size = (100, 40))
      self.trash = wx.Button(self, -1, 'X', size = (20, 40))
      self.trash.Bind(wx.EVT_BUTTON, self.DeleteLayer)
      self.add = wx.Button(self, -1, '+', size = (20, 40))
      self.add.Bind(wx.EVT_BUTTON, self.NewLayer)
      self.label = wx.StaticText(self, -1, 'Opacity:', size = (80, 40), style=wx.ALIGN_CENTER)

      #currentLayers = self.parent.layerManagerModel
      self.layerDisplay = wx.BoxSizer(wx.VERTICAL)
      self.layers = []
      for layer in self.parent.layerManagerModel.layers:
         view = LayerView(parent, layer)
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

   def DeleteLayer(self, event):
      self.parent.layerManagerModel.DeleteLayer()

   def NewLayer(self, event):
      self.parent.layerManagerModel.NewLayer()
