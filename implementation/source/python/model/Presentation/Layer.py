class Layer:
   def __init__(self, name, lock):
      self.objects = None
      self.opacity = 100.00
      self.visible = True
      self.permissions = None
      self.name = name
      self.locked = lock

   def ChangePermissions(self):
      print('From Layer.ChangePermissions()')
      
   def ToggleLock(self):
      print('From Layer.ToggleLock()')
      
   def ToggleVisible(self):
      print('From Layer.ToggleVisible()')
