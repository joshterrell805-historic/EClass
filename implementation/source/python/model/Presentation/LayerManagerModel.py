from Layer import Layer

class LayerManagerModel:
   def __init__(self):
      background = Layer("Background", True)
      self.layers = [background]

   def DeleteLayer(self):
      print('From LayerManager.DeleteLayer()')

   def NewLayer(self):
      print('From LayerManager.NewLayer()')
      
   def ChangeOpacity(self, index):
      print('From LayerManager.ChangeOpacity()')
