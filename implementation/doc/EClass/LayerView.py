import wx

class LayerView(wx.Panel):
   def layerListObject(self, parent):
      """
      Set the selected layer's permissions.
      
      @precondition: self.layer != None
      
      @postcondition: self.layer == old(self.layer)
      """

   def __init__(self, parent, layer):
      """
      Initialize a Layer View.

      @param parent: The class that initialized this view.
      @param layer: The layer to be shown.
      """
   def changePermissions(self, event):
      """
      Set the selected layer's permissions.

      @postcondition: self.permissions != old(self.permissions)
      """
      
   def ToggleVisible(self, event):
      """
      Set the visibility of a layer.

      @postcondition: self.visible != old(self.visible)
      """

   def ToggleLock(self, event):
      """
      Set the lock state of a layer.

      @postcondition: self.locked != old(self.locked)
      """
