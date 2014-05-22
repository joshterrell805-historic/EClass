import unittest
import sys
sys.path.insert(0, '../../../implementation/source/python/model')
sys.path.insert(0, '../../../implementation/source/python/model')

from Person.StudentPermissions import StudentPermissions
from Presentation.PermissionLevel import PermissionLevel

class StudentPermissionsTest(unittest.TestCase):
   """
   Class QuestionTest is the companion testing class for class Question.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the Permission Level access methods GetPresPermLevel
               and SetPresPermLevel.
      Phase 3: Unit test the hand raise access methods CanRaiseHand and
               SetCanRaiseHand.
      Phase 4: Unit test the layer pushing access methods CanPushLayer and
               SetCanPushLayer.
   """

   def setUp(self):
      self.sp = StudentPermissions(PermissionLevel.Normal, True, True)
      self.assertEqual(self.sp.presPermLevel, PermissionLevel.Normal)
      self.assertEqual(self.sp.canRaiseHand, True)
      self.assertEqual(self.sp.canPushLayer, True)
      

   def test_GetPresPermLevel(self):
      self.assertEqual(self.sp.GetPresPermLevel(), PermissionLevel.Normal)

   def test_SetPresPermLevel(self):
      self.sp.SetPresPermLevel(PermissionLevel.Unrestricted)
      self.assertEqual(self.sp.GetPresPermLevel(), PermissionLevel.Unrestricted)
      
   def test_CanRaiseHand(self):
      self.assertEqual(self.sp.CanRaiseHand(), True)

   def test_SetCanRaiseHand(self):
      self.sp.SetCanRaiseHand(False)
      self.assertEqual(self.sp.canRaiseHand, False)

   def test_CanPushLayer(self):
      self.assertEqual(self.sp.CanPushLayer(), True)

   def test_SetCanPushLayer(self):
      self.sp.SetCanPushLayer(False)
      self.assertEqual(self.sp.canPushLayer, False)

if __name__ == '__main__':
    unittest.main()
      
