from Layer import Layer

class Slide(object):
   
   def __init__(self, content, layers = []):
      self.content = content
      self.layers = layers

   def GetContent(self):
      return self.content

   def GetLayers(self):
      return self.layers
      
   def AddLayer(self, layer):
      if isinstance(layer, Layer):
         self.layers.append(layer)

   def OrderLayer(self, layer, newIndex):
   
      if (isinstance(layer, Layer) and 
          self.layers.count(layer) == 1 and
          newIndex >= 0 and 
          newIndex < len(self.layers)
      ):
         currIndex = self.layers.index(layer)
         if currIndex < newIndex:
            # Adjust newIndex to prevent off-by-one index error
            newIndex -= 1
         self.layers.insert(newIndex, layer)