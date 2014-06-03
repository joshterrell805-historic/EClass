from Layer import Layer

class LayerManagerModel:
   def __init__(self, parent, layers):
      if parent == None:
         raise ValueError('Layer Manager needs a parent!')
      else:
         self.layers = layers
         self.parent = parent
         self.currLayer = 0
         
   def SetCurrentLayer(self, index):
      if index >= 0 and len(self.layers) > 0 and index <= len(self.layers):
         self.currLayer = index
      
   # TODO update documentation - newObj is a dictionary with all needed info for an object
   def AddObject(self, newObj):
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
         self.layers[self.currLayer].objects.append(newObj)
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
      
   def RemoveObject(self, objToRemove):
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
          i = 0
          for obj in self.layers[self.currLayer].objects:
             if obj == objToRemove:
                del self.layers[self.currLayer].objects[i]
                self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
             i += 1
             
   def ChangeObjPos(self, objToChange, newPos):
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
          i = 0
          for obj in self.layers[self.currLayer].objects:
             if obj == objToChange:
                self.layers[self.currLayer].objects[i]['position'] = newPos
                self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
             i += 1
      
   def DeleteLayer(self, index):
      if index >= 0 and len(self.layers) > 0 and index <= len(self.layers) and self.layers[index].locked == False:
         del self.layers[index]
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers

   def NewLayer(self, layer):
      if isinstance(layer, Layer):
         self.layers.reverse()
         self.layers.append(layer)
         self.layers.reverse()
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
         self.currLayer = 0
         
   def ChangeOpacity(self, index, newOpacity):
      if index > -1 and index < len(self.layers) and newOpacity > -1 and newOpacity <= 255:
         self.layers[index].SetOpacity(newOpacity)
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
