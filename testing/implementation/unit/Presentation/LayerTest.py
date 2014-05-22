import unittest
import sys
sys.path.insert(0, '../../../implementation/source/python/model/Presentation')

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
      Unit test the constructor by building one Layer objects.

      Test
      Case     Input                        Output               Remarks
      =========================================================================
      1        No name, opacity, or lock    Generic Layer
      2        All name, opacity, and lock  Unique Layer
      """
      self.layer = Layer(None, None, None)
      self.assertEquals(self.layer.name, "Layer")
      self.assertEquals(self.layer.opacity, 100)
      self.assertFalse(self.layer.locked)
      
      self.layer = Layer("Joey", 50, True)
      self.assertEquals(self.layer.name, "Joey")
      self.assertEquals(self.layer.opacity, 50)
      self.assertTrue(self.layer.locked)

   def test_ChangePermissions(self):
      """
      Unit test ChangePermissions.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        []                      changed
      2        [Ralpy]                 changed
      3        [Ralpy, Donna]          changed
      """
      self.layer = Layer("Mep", 0, False)
      self.layer.ChangePermissions([]);
      self.assertEquals(self.layer.permissions, [])
      self.layer.ChangePermissions(["Ralpy"]);
      self.assertEquals(self.layer.permissions, ["Ralpy"])
      self.layer.ChangePermissions(["Ralpy", "Donna"]);
      self.assertEquals(self.layer.permissions, ["Ralpy", "Donna"])
      
   def test_ToggleLock(self):
      """
      Unit test ToggleLock.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Layer is not locked     lock = True
      2        Layer is locked         lock = False
      """
      self.layer = Layer("Mep", 0, False)
      self.layer.ToggleLock()
      self.assertTrue(self.layer.locked)
      self.layer.ToggleLock()
      self.assertFalse(self.layer.locked)
      
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
      self.layer = Layer("Mep", 0, False)
      self.layer.ToggleVisible()
      self.assertTrue(self.layer.visible)
      self.layer.ToggleVisible()
      self.assertFalse(self.layer.visible)
      self.layer = Layer("Mep", 0, True)
      self.layer.ToggleVisible()
      self.assertFalse(self.layer.visible)
      
   def test_ChangeName(self):
      """
      Unit test ChangeName.

      Test
      Case     Input                     Output               Remarks
      =========================================================================
      1        ""                        no change
      2        "SuperLayer"              name changed
      3        "Yikes" (Layer is locked) no change
      """
      self.layer = Layer("Mep", 50, False)
      self.layer.ChangeName("")
      self.assertEquals(self.layer.name, "Mep")
      self.layer.ChangeName("SuperLayer");
      self.assertEquals(self.layer.name, "SuperLayer")
      self.layer = Layer("Pem", 50, True)
      self.layer.ChangeName("Yikes");
      self.assertEquals(self.layer.name, "Pem")
      
   def test_SetOpacity(self):
      """
      Unit test SetOpacity.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        -5                      no change
      2        100                     opacity changed
      3        10 (Layer is locked)    no change
      """
      self.layer = Layer("Mep", 50, False)
      self.layer.SetOpacity(-5)
      self.assertEquals(self.layer.opacity, 50)
      self.layer.SetOpacity(100);
      self.assertEquals(self.layer.opacity, 100)
      self.layer = Layer("Pem", 50, True)
      self.layer.SetOpacity(10);
      self.assertEquals(self.layer.opacity, 50)
      
if __name__ == "__main__":
   unittest.main()
