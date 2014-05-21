from Layer import Layer

class LayerManagerModel:
   def __init__(self, parent, layers):
      if parent = None:
         raise ValueError('Layer Manager needs a parent!')
      else:
         self.layers = layers
         self.parent = parent

   def DeleteLayer(self):
      print('From LayerManager.DeleteLayer()')

   def NewLayer(self, layer):
      print('From LayerManager.NewLayer()')
      self.layers.reverse()
      self.layers.append(layer)
      self.layers.reverse()
      self.parent.presentation.slides[self.parent.presentation.currSlideNum].layers = self.layers
      
   def ChangeOpacity(self, index, newOpactiy):
      print('From LayerManager.ChangeOpacity()')
