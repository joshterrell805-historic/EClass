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
      self.layers.reverse()
      if ( self.layers[self.currLayer].locked == False 
       and self.layers[self.currLayer].visible == True):
         self.layers[self.currLayer].objects.append(newObj)
         self.layers.reverse()
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
      
   def DeleteLayer(self, index):
      if index >= 0 and len(self.layers) > 0 and index <= len(self.layers) and self.layers[index].locked == False:
         del self.layers[index]
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
         if self.currLayer == index:
            self.currLayer = len(self.layers) - 1

   def NewLayer(self, layer):
      if isinstance(layer, Layer):
         self.layers.reverse()
         self.layers.append(layer)
         self.layers.reverse()
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
         self.currLayer = len(self.layers) - 1
         
   def ChangeOpacity(self, index, newOpacity):
      if index > -1 and index < len(self.layers) and newOpacity > -1 and newOpacity <= 255:
         self.layers[index].SetOpacity(newOpacity)
