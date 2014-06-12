import wx
import sys

from ChangePermWindow import ChangePermWindow
sys.path.insert(0, 'model')
from EClass import EClass

class LayerView(wx.Panel):
   def LayerListObject(self, parent, index, checked):
      self.index = index
      
      layerControls = wx.BoxSizer(wx.HORIZONTAL)
      select = wx.CheckBox(parent, -1, '', (15, 20))
      select.Bind(wx.EVT_CHECKBOX, self.SelectLayer)
      select.SetValue(checked)
      label = wx.StaticText(parent, -1, self.layer.name, size = (100, 40), style = wx.ALIGN_LEFT)
      layerControls.Add(select, 1)
      layerControls.Add(label, 1)

      visible = wx.CheckBox(parent, -1 ,'Visible', (15, 40))
      if self.layer.visible == True:
         visible.SetValue(True)
      visible.Bind(wx.EVT_CHECKBOX, self.ToggleVisible)
      
      lock = wx.CheckBox(parent, -1 ,'Lock', (15, 40))
      if self.layer.locked == True:
         lock.SetValue(True)
      lock.Bind(wx.EVT_CHECKBOX, self.ToggleLock)
      
      permissions = wx.Button(parent, -1, 'Perm', size = (20, 40))
      permissions.Bind(wx.EVT_BUTTON, self.ChangePermissions)
      
      layerControls.Add(visible, 1)
      layerControls.Add(lock, 1)
      layerControls.Add(permissions, 1)

      return layerControls

   def __init__(self, parent, layer):
      self.layer = layer
      self.parent = parent

   def ChangePermissions(self, event):
      self.changeLayerPerm = ChangePermWindow(self.parent, self.layer)
      
   def ToggleVisible(self, event):
      self.layer.ToggleVisible()
      self.parent.parent.parent.whiteboard.Redraw()

   def ToggleLock(self, event):
      self.layer.ToggleLock()
      
   def SelectLayer(self, event):
      self.parent.selectedLayer = self.index
      EClass.GetInstance().layerManagerModel.SetCurrentLayer(self.index)
      self.parent.slider.SetValue(self.layer.opacity)
      self.parent.UpdateLayers()
