import unittest
import sys
sys.path.insert(0, '../../../implementation/source/python/model/')

from Presentation.QuestionList import QuestionList
from Person.Question import Question

class QuestionListTest(unittest.TestCase):
   """
   Class QuestionListTest is the companion testing class for class Presentation.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the Append method.
      Phase 3: Unit test the Remove and RemoveAll method.
      Phase 4: Unit test the __getitem__ method.
   """
   def setUp(self):
      """
      Unit test the constructor by building one QuestionList object.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        no input                Empty Question List  Only case
      """
      self.QuestionList = QuestionList()
      self.assertEqual(len(self.QuestionList.questions), 0)
      
   def test_Append(self):
      """
      Unit test the Append method by building adding questions.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        A question              1 Question on list  
      2        Another question        2 Questions on list  
      """
      self.QuestionList.Append(Question("my question"))
      self.assertEqual(len(self.QuestionList.questions), 1)
      self.QuestionList.Append(Question("another question"))
      self.assertEqual(len(self.QuestionList.questions), 2)
      
   def test_Remove(self):
      """
      Unit test the Remove method by building removeing questions.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        -1                      Bad Index/No change in list
      2        100                     Bad Index/No change in list
      3        1                       1 Questions on list  
      """
      self.QuestionList.Remove(-1)
      self.assertEqual(len(self.QuestionList.questions), 2)
      self.QuestionList.Remove(100)
      self.assertEqual(len(self.QuestionList.questions), 2)
      self.QuestionList.Remove(1)
      self.assertEqual(len(self.QuestionList.questions), 1)
   def test_RemoveAll(self):
      """
      Unit test the RemoveAll method by building a lsit of questions then 
      removing them all.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        None                    0 Questions on list  only test
      """
      self.QuestionList.Append(Question("my question"))
      self.QuestionList.RemoveAll()
      self.assertEqual(len(self.QuestionList.questions), 0)

   def test__getitem__(self):   
      pass
