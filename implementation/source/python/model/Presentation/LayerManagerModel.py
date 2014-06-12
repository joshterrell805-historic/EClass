from Layer import Layer

class LayerManagerModel:
   def __init__(self, parent, layers):
      self.layers = layers
      self.parent = parent
      self.currLayer = 0
         
   def SetCurrentLayer(self, index):
      if index >= 0 and len(self.layers) > 0 and index <= len(self.layers):
         self.currLayer = index
      
   def AddObject(self, newObj):
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
         self.layers[self.currLayer].objects.append(newObj)
      
   def RemoveObject(self, objToRemove):
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
          i = 0
          for obj in self.layers[self.currLayer].objects:
             if obj == objToRemove:
                del self.layers[self.currLayer].objects[i]
             i += 1
             
   def ChangeObjPos(self, objToChange, oldPos, newPos):
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
          xdiff = newPos.x - oldPos.x
          ydiff = newPos.y - oldPos.y
          if objToChange['type'] == 'Pencil':
             for point in objToChange['points']:
                point.x += xdiff
                point.y += ydiff
          else:
             objToChange['position'].x += xdiff
             objToChange['position'].y += ydiff
            
   def DeleteLayer(self, index):
      if index >= 0 and len(self.layers) > 0 and index <= len(self.layers) and self.layers[index].locked == False:
         del self.layers[index]

   def NewLayer(self, layer):
      if isinstance(layer, Layer):
         self.layers.reverse()
         self.layers.append(layer)
         self.layers.reverse()
         self.currLayer = 0
         
   def ChangeOpacity(self, index, newOpacity):
      if index > -1 and index < len(self.layers) and newOpacity > -1 and newOpacity <= 255:
         self.layers[index].SetOpacity(newOpacity)
