class Layer:
   def __init__(self, name, opacity, lock):
      self.objects = None
      self.opacity = opacity
      self.visible = True
      self.permissions = []
      self.name = name
      self.locked = lock

   def ChangePermissions(self, newPermissions):
      print('From Layer.ChangePermissions()')
      
   def ToggleLock(self):
      print('From Layer.ToggleLock()')
      
   def ToggleVisible(self):
      print('From Layer.ToggleVisible()')
      
   def ChangeName(self, newName):
      print('From Layer.ChangeName()')
      
   def SetOpacity(self, newOpacity):
      print('From Layer.setOpacity()')
