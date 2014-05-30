class Layer:
   def __init__(self, name, opacity, lock):
      self.objects = []
      if opacity == 0:
         self.visible = False
      else:
         self.visible = True
         
      if opacity == None:
         self.opacity = 100
      else:
         self.opacity = opacity
         
      self.permissions = []
      
      if name == None:
         self.name = "Layer"
      else:
         self.name = name
         
      self.locked = lock

   def ChangePermissions(self, newPermissions):
      if self.locked == False:
         self.permissions = newPermissions
      
   def ToggleLock(self):
      self.locked = not self.locked
      
   def ToggleVisible(self):
      if self.locked == False:
         self.visible = not self.visible
   
   def ChangeName(self, newName):
      if self.locked == False and newName != "":
         self.name = newName
      
   def SetOpacity(self, newOpacity):
      if self.locked == False and newOpacity >= 0 and newOpacity <= 100:
         if newOpacity == 0:
            self.visible = False
         else:
            self.visible = True
         self.opacity = newOpacity
