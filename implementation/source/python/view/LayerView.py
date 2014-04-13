import wx

class LayerView(wx.Panel):
   def layerListObject(self, parent):
      layerControls = wx.BoxSizer(wx.HORIZONTAL)
      label = wx.StaticText(parent, -1, self.layer.name, size = (100, 40), style = wx.ALIGN_LEFT)
      layerControls.Add(label, 1)

      self.visible = wx.CheckBox(parent, -1 ,'Visible', (15, 40))
      self.visible.Bind(wx.EVT_CHECKBOX, self.ToggleVisible)
      self.lock = wx.CheckBox(parent, -1 ,'Lock', (15, 40))
      if self.layer.locked == True:
         self.lock.SetValue(True)
      self.lock.Bind(wx.EVT_CHECKBOX, self.ToggleLock)
      self.permissions = wx.Button(parent, -1, 'Perm', size = (20, 40))
      self.permissions.Bind(wx.EVT_BUTTON, self.changePermissions)
      layerControls.Add(self.visible, 1)
      layerControls.Add(self.lock, 1)
      layerControls.Add(self.permissions, 1)

      return layerControls

   def __init__(self, parent, layer):
      self.layer = layer

   def changePermissions(self, event):
      self.layer.ChangePermissions()
      
   def ToggleVisible(self, event):
      self.layer.ToggleVisible()
      
   def ToggleLock(self, event):
      self.layer.ToggleLock()
