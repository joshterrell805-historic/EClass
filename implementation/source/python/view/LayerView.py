import wx

class LayerView(wx.Panel):
   def layerListObject(self, parent):
      layerControls = wx.BoxSizer(wx.HORIZONTAL)
      label = wx.StaticText(parent, -1, self.layer.name, size = (175, 40), style = wx.ALIGN_LEFT)
      layerControls.Add(label, 1)

      if self.layer.locked == True:
         lock = wx.StaticText(parent, -1, 'locked', size = (80, 40), style = wx.ALIGN_RIGHT)
         layerControls.Add(lock, 1)
      else:
         visible = wx.CheckBox(parent, -1 ,'Visible', (15, 40))
         self.permissions = wx.Button(parent, -1, 'Perm', size = (20, 40))
         self.permissions.Bind(wx.EVT_BUTTON, self.changePermissions)
         layerControls.Add(visible, 1)
         layerControls.Add(permissions, 1)

      return layerControls

   def __init__(self, parent, layer):
      self.layer = layer

   def changePermissions(self):
      layer.changePermissions()
