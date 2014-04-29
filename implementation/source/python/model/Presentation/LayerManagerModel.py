from Layer import Layer

class LayerManagerModel:
   def __init__(self):
      background = Layer("Background", 100, True)
      self.layers = [background]

   def DeleteLayer(self):
      print('From LayerManager.DeleteLayer()')

   def NewLayer(self, layer):
      print('From LayerManager.NewLayer()')
      self.layers.reverse()
      self.layers.append(layer)
      self.layers.reverse()
      
   def ChangeOpacity(self, index):
      print('From LayerManager.ChangeOpacity()')
