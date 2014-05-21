import unittest
import sys

sys.path.insert(0, '../../../../implementation/source/python/model/Presentation')

from Layer import Layer

class LayerTest(unittest.TestCase):
   """
   Class LayerTest is the companion testing class for class Layer.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the ToggleLock.
      Phase 3: Unit test the ToggleVisible and SetOpacity.
      Phase 4: Unit test the change name and permissions methods.
   """
   
   def setUp(self):
      """
      Unit test the constructor by building one Layer object.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        No name, opacity, or lock    Generic Layer
      2        All name, opacity, and lock  Unique Layer
      """
      
      self.layer = Layer(None, None, None)
      self.assertEquals(self.layer.name, "Layer")
      self.assertEquals(self.layer.opacity, 100)
      self.assertFalse(self.layer.lock)
      
      self.layer = Layer("Joey", 50, True)
      self.assertEquals(self.layer.name, "Joey")
      self.assertEquals(self.layer.opacity, 50)
      self.assertTrue(self.layer.lock)

   def test_ChangePermissions(self):
      """
      Unit test ChangePermissions.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        []                      True
      2        [Ralpy]                 True
      3        [Ralpy, Donna]          True
      4        [Ted](Not is Class)     False
      """
      print('From Layer.ChangePermissions()')
      
   def test_ToggleLock(self):
      """
      Unit test ToggleLock.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Layer is not locked     True
      2        Layer is locked         False
      """
      print('From Layer.ToggleLock()')
      
   def test_ToggleVisible(self):
      """
      Unit test ToggleVisible.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Layer is not visible    True
      2        Layer is visible        False
      3        Layer is locked         False
      """
      print('From Layer.ToggleVisible()')
      
   def test_ChangeName(self, newName):
      """
      Unit test ChangeName.

      Test
      Case     Input                     Output               Remarks
      =========================================================================
      1        ""                        False
      2        "SuperLayer"              True
      3        "Yikes" (Layer is locked) False
      """
      print('From Layer.ChangeName()')
      
   def test_SetOpacity(self, newOpacity):
      """
      Unit test SetOpacity.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        -5                      False
      2        100                     True
      3        10 (Layer is locked)    False
      """
      print('From Layer.setOpacity()')
