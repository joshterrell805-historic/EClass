class Layer:
   def __init__(self, name, opacity, lock):
      self.objects = None
      self.opacity = opacity
      self.visible = True
      self.permissions = []
      self.name = name
      self.locked = lock

   def ChangePermissions(self):
      print('From Layer.ChangePermissions()')
      
   def ToggleLock(self):
      print('From Layer.ToggleLock()')
      
   def ToggleVisible(self):
      print('From Layer.ToggleVisible()')
