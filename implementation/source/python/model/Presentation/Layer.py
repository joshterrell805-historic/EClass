class Layer:
   def __init__(self, name = None, opacity = None, lock = False):
      self.objects = []
      if opacity == 0:
         self.visible = False
      else:
         self.visible = True
         
      if opacity == None:
         self.opacity = 255
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
      if self.locked == False and newOpacity >= 0 and newOpacity <= 255:
         if newOpacity == 0:
            self.visible = False
         else:
            self.visible = True
         self.opacity = newOpacity

   def toDict(self):
      def ptToDict(pt):
         return {
            'x': pt.x,
            'y': pt.y
         }

      def objToDict(obj):
         # make a new dict rather than mutating the passed one
         d = {
            'type': obj['type'],
         }

         if d['type'] == 'Square':
            d['position'] = ptToDict(obj['position'])
            d['x_size'] = obj['x_size']
            d['y_size'] = obj['y_size']

         elif d['type'] == 'Text':
            d['position'] = ptToDict(obj['position'])
            d['text'] = obj['text']

         elif d['type'] == 'Pencil':
            d['points'] = map(ptToDict, obj['points'])

         else:
            raise Exception(
               "Object type '" + d['type'] + "' cannot be translated to a dict"
            )

         return d
         
      return {
         'opacity' : self.opacity,
         'name': self.name,
         'locked' : self.locked,
         'objects' : map(objToDict, self.objects)
      }

   @staticmethod
   def fromDict(d):
      def ptFromDict(d):
         import wx
         return wx.Point(d['x'], d['y'])

      def objFromDict(d):
         # we don't care about making a new dict here as we do above,
         # because here is the place we interacting with this dict
         if d['type'] == 'Square':
            d['position'] = ptFromDict(d['position'])
         elif d['type'] == 'Text':
            d['position'] = ptFromDict(d['position'])
         elif d['type'] == 'Pencil':
            d['points'] = map(ptFromDict, d['points'])
         else:
            raise Exception(
               "Object type '" + d['type'] + "' cannot be translated from a dict"
            )
         return d

      layer = Layer(
         d['name'],
         d['opacity'],
         d['locked']
      )
      layer.objects = map(objFromDict, d['objects'])
      return layer
