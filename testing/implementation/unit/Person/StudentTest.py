import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Person')

from Student import Student
from Question import Question
from StudentPermissions import StudentPermissions

class StudentTest(unittest.TestCase):
   """
   Class StudentTest is the companion testing class for class Student.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the permissions access methods SetPermissions and 
               GetPermissions.
      Phase 3: Unit test the status access methods SetPresent, IsPresent,
               SetKicked, and IsKicked.
      Phase 4: Unit test the question methods HasQuestion, SetQuestion,
               and GetQuestion.
      Phase 5: Unit test the layer methods SetPushedLayer and GetPushedLayer.
   """

   def setUp(self):
      """
      Unit test the constructor by building one Student object.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        No permissions given    New permissions
                                       created
      2        Permissions given       Permissions set to
                                       the ones given
      """
      
      self.student = Student('BurtMacklin', 'blah')
      self.assertTrue(self.student.present)
      self.assertFalse(self.student.kicked)
      self.assertEqual(self.student.question, None)
      self.assertEqual(self.student.pushedLayer, None)
      self.assertTrue(isinstance(self.student.permissions, StudentPermissions))
      
      self.perms = StudentPermissions()
      self.student = Student('BurtMacklin', 'blah', perms)
      self.assertEqual(self.perms, self.student.permissions)

   def test_GetPermissions(self):
      """
      Unit test GetPermissions.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        permissions =           self.perms           Only case
               self.perms
      """
      
      self.assertTrue(isinstance(self.student.GetPermissions(), StudentPermissions))
      self.assertEqual(self.student.GetPermissions(), self.perms)

   def test_SetPermissions(self):
      """
      Unit test SetPermissions.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        None                                         permissions are unchanged
      2        a number                                     permissions are unchanged
      3        valid permissions                            permissions are set
      """
      
      self.student.SetPermissions(None)
      self.assertEqual(self.student.GetPermissions(), self.perms)
      self.student.SetPermissions(3)
      self.assertEqual(self.student.GetPermissions(), self.perms)
      newPerms = StudentPermissions()
      self.student.SetPermissions(newPerms)
      self.assertEqual(self.student.GetPermissions(), newPerms)
      
   def test_IsPresent(self):
      """
      Unit test IsPresent.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        present = True          True
      2        present = False         False
      """
      
      self.assertTrue(self.student.IsPresent())
      self.student.present = False
      self.assertFalse(self.student.IsPresent())
      
   def test_SetPresent(self):
      """
      Unit test SetPresent.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        a number                                     present status not changed
      2        False                                        present status changed
      3        True                                         present status changed
      """
      
      present = self.student.IsPresent()
      self.student.SetPresent(3)
      self.assertEqual(self.student.IsPresent(), present)
      self.student.SetPresent(False)
      self.assertFalse(self.student.IsPresent())
      self.student.SetPresent(True)
      self.assertTrue(self.student.IsPresent())
      
   def test_IsKicked(self):
      """
      Unit test IsKicked.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        kicked = False          False
      2        kicked = True           True
      """
      
      self.assertFalse(self.student.IsKicked())
      self.student.kicked = True
      self.assertTrue(self.student.IsKicked())
      
   def test_SetKicked(self):
      """
      Unit test SetPresent.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        a number                                     kicked status not changed
      2        True                                         kicked status changed
      3        False                                        kicked status changed
      """
      
      kicked = self.student.IsKicked()
      self.student.SetKicked(3)
      self.assertEqual(self.student.IsKicked(), kicked)
      self.student.SetKicked(True)
      self.assertTrue(self.student.IsKicked())
      self.student.SetKicked(False)
      self.assertFalse(self.student.IsKicked())
      
   def test_HasQuestion(self):
      """
      Unit test HasQuestion.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        student has a question  True
      2        student doesn't have    False
               a question
      """
      pass
      
   def test_GetQuestion(self):
      """
      Unit test GetQuestion.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        question != None        student.question
      2        question == None        None
      """
      pass
      
   def test_SetQuestion(self):
      """
      Unit test SetQuestion.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Question object                              question is set
      2        non-Question                                 question is unchanged
      """
      pass
         
   def test_GetPushedLayer(self):
      """
      Unit test GetPushedLayer.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        pushedLayer != None     student.pushedLayer
      2        pushedLayer == None     None
      """
      pass
      
   def test_SetPushedLayer(self):
      """
      Unit test SetPushedLayer.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Layer object                                 pushedLayer is set
      2        non-Layer                                    pushedLayer is unchanged
      """
      pass
      
if __name__ == "__main__":
   unittest.main()