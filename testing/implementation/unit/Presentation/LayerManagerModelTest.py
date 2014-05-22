import unittest
import sys

sys.path.insert(0, '../../../implementation/source/python/model/Presentation')

from Slide import Slide
from LayerManagerModel import LayerManagerModel
from Layer import Layer

class LayerManagerModelTest(unittest.TestCase):
   """
   Class LayerManagerModelTest is the companion testing class for class LayerManagerModel.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the new Layer method.
      Phase 3: Unit test the Delete Layer method.
      Phase 4: Unit test the change opacity method.
   """
   
   def setUp(self):
      """
      Unit test the constructor by building one LayerManagerModel object.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        No parent                ValueError
      2        No layers                Empty Layer Manager Created
      3        Both Layer and parent    Layer Manager with layers created
      """
      
      #self.layerManager = LayerManagerModel(None, [])
      
      self.layerManager = LayerManagerModel(self, [])
      self.assertEquals(self.layerManager.parent, self)
      self.assertEquals(self.layerManager.layers, [])
      
      layer = Layer("test", 50, False)
      self.layerManager = LayerManagerModel(self, [layer])
      self.assertEquals(self.layerManager.parent, self)
      self.assertEquals(self.layerManager.layers, [layer])

   def test_DeleteLayer(self):
      """
      Unit test DeleteLayer.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        none (layers in manager)     layer deleted           
      2        none (no layers in manager)  nothing happens           
      """
      class Object:
         pass
      layer = Layer("test", 50, False)
      self.layerManager = LayerManagerModel(self, [layer])
      self.presentation = Object()
      self.presentation.slides = [Slide("",[layer])]
      self.presentation.currSlideNum = 0
      self.layerManager.DeleteLayer(0)
      self.assertEquals(len(self.layerManager.layers), 0)
      self.layerManager.DeleteLayer(0)
      self.assertEquals(len(self.layerManager.layers), 0)

   def test_NewLayer(self):
      """
      Unit test NewLayer.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        no new layer given           false
      2        none (no layers in manager)  true           
      """
      class Object:
         pass
      self.presentation = Object()
      self.presentation.slides = [Slide("",[])]
      self.presentation.currSlideNum = 0
      self.layerManager = LayerManagerModel(self, [])
      self.layerManager.NewLayer("bad")
      self.assertEquals(self.layerManager.layers, [])
      newLayer = Layer("test", 50, False)
      self.layerManager.NewLayer(newLayer)
      self.assertEquals(self.layerManager.layers, [newLayer])
      
   def test_ChangeOpacity(self):
      """
      Unit test ChangeOpacity.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        bad index                    false
      2        bad opacity                  false           
      3        good index and opacity       true           
      """
      layer = Layer("test", 50, False)
      self.layerManager = LayerManagerModel(self, [layer])
      origMan = self.layerManager
      self.layerManager = LayerManagerModel(self, [layer])
      self.layerManager.ChangeOpacity(-1, 50)
      self.assertEquals(self.layerManager.layers[0].opacity, 50)
      self.layerManager.ChangeOpacity(0, -50)
      self.assertEquals(self.layerManager.layers[0].opacity, 50)   
      self.layerManager.ChangeOpacity(0, 100)
      self.assertEquals(self.layerManager.layers[0].opacity, 100)   
      
if __name__ == "__main__":
   unittest.main()
