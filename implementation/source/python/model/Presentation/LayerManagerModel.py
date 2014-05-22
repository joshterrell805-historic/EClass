from Layer import Layer

class LayerManagerModel:
   def __init__(self, parent, layers):
      if parent == None:
         raise ValueError('Layer Manager needs a parent!')
      else:
         self.layers = layers
         self.parent = parent

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
         
   def ChangeOpacity(self, index, newOpacity):
      if index > -1 and index < len(self.layers) and newOpacity > -1 and newOpacity <= 100:
         self.layers[index].SetOpacity(newOpacity)
