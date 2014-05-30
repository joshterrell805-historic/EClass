import wx
import sys

from ChangePermWindow import ChangePermWindow
sys.path.insert(0, 'model')
from EClass import EClass

class LayerView(wx.Panel):
   def layerListObject(self, parent, index, checked):
      self.index = index
      layerControls = wx.BoxSizer(wx.HORIZONTAL)
      self.select = wx.CheckBox(parent, -1, '', (15, 20))
      self.select.Bind(wx.EVT_CHECKBOX, self.SelectLayer)
      self.select.SetValue(checked)
      label = wx.StaticText(parent, -1, self.layer.name, size = (100, 40), style = wx.ALIGN_LEFT)
      layerControls.Add(self.select, 1)
      layerControls.Add(label, 1)

      self.visible = wx.CheckBox(parent, -1 ,'Visible', (15, 40))
      if self.layer.visible == True:
         self.visible.SetValue(True)
      self.visible.Bind(wx.EVT_CHECKBOX, self.ToggleVisible)
      self.lock = wx.CheckBox(parent, -1 ,'Lock', (15, 40))
      if self.layer.locked == True:
         self.lock.SetValue(True)
      self.lock.Bind(wx.EVT_CHECKBOX, self.ToggleLock)
      self.permissions = wx.Button(parent, -1, 'Perm', size = (20, 40))
      self.permissions.Bind(wx.EVT_BUTTON, self.ChangePermissions)
      layerControls.Add(self.visible, 1)
      layerControls.Add(self.lock, 1)
      layerControls.Add(self.permissions, 1)

      return layerControls

   def __init__(self, parent, layer):
      self.layer = layer
      self.parent = parent

   def ChangePermissions(self, event):
      self.changeLayerPerm = ChangePermWindow(self.parent, self.layer)
      
   def ToggleVisible(self, event):
      self.layer.ToggleVisible()
      self.parent.parent.parent.whiteboard.UpdateLayers()

   def ToggleLock(self, event):
      self.layer.ToggleLock()
      
   def SelectLayer(self, event):
      self.parent.selectedLayer = self.index
      EClass.GetInstance().layerManagerModel.SetCurrentLayer(self.index)
      self.parent.slider.SetValue(self.layer.opacity)
      self.parent.UpdateLayers()
