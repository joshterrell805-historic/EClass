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
         
   def AddObject(self, name, position):
      print self.currLayer
      self.layers.reverse()
      if self.layers[self.currLayer].locked == False:
         print self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers[self.currLayer].objects
         self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers[self.currLayer].objects.append(position)
      self.layers.reverse()
      
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
      if index > -1 and index < len(self.layers) and newOpacity > -1 and newOpacity <= 100:
         self.layers[index].SetOpacity(newOpacity)
