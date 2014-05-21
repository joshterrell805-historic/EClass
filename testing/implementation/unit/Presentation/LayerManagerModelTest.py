import unittest
import sys

sys.path.insert(0, '../../../../implementation/source/python/model/Presentation')

from LayerManager import LayerManager
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
      1        No layers and no parent  ValueError
      2        No parent                ValueError
      2        No layers                Empty Layer Manager Created
      2        Both Layer and parent    Layer Manager with layers created
      """
      
      self.layerManager = LayerManager(None, [])
      
      self.layerManager = LayerManager(none, [Layer("test", 50, false)])
      
      self.layerManager = LayerManager(self, [])
      self.assertEquals(self.layerManager.parent, self)
      self.assertEquals(self.layerManager.layers, [])
      
      self.layerManager = LayerManager(self, [Layer("test", 50, false)])
      self.assertEquals(self.layerManager.parent, self)
      self.assertEquals(self.layerManager.layers, [Layer("test", 50, false)])

   def test_DeleteLayer(self):
      """
      Unit test DeleteLayer.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        none (layers in manager)     true           
      2        none (no layers in manager)  false           
      """
      self.layerManager = LayerManager(self, [Layer("test", 50, false)])
      self.assertTrue(self.layerManager.DeleteLayer())
      self.assertFalse(self.layerManager.DeleteLayer())

   def test_NewLayer(self, layer):
      """
      Unit test NewLayer.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        no new layer given           false
      2        none (no layers in manager)  true           
      """
      self.assertFalse(self.layerManager.NewLayer())
      self.assertTrue(self.layerManager.NewLayer(Layer("test", 50, false)))
      
   def test_ChangeOpacity(self, index, newOpacity):
      """
      Unit test ChangeOpacity.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        bad index                    false
      2        bad opacity                  false           
      3        good index and opacity       true           
      """
      self.assertFalse(self.layerManager.ChangeOpacity(-1, 50))
      self.assertFalse(self.layerManager.ChangeOpacity(1, -50))   
      self.assertTrue(self.layerManager.ChangeOpacity(1, 50))   
