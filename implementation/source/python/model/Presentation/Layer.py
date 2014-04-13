class Layer:
   def __init__(self, name, lock):
      self.objects = None
      self.opacity = 100.00
      self.visible = True
      self.permissions = None
      self.name = name
      self.locked = lock

   def changePermissions(self):
      print('From LayerManager.DeleteLayer()')
