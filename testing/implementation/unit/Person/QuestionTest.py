import unittest
import sys
sys.path.insert(0, '../../../implementation/source/python/model/Person')

from Question import Question

class QuestionTest(unittest.TestCase):
   """
   Class QuestionTest is the companion testing class for class Question.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the text access method GetText.
      Phase 3: Unit test the time access method GetTime.
   """

   def setUp(self):
      self.quest = Question(questionText = 'How are you?')
      self.assertEqual(self.quest.text, 'How are you?')
      
   def test_GetText(self):
      self.assertEqual(self.quest.GetText(), 'How are you?')

if __name__ == '__main__':
    unittest.main()
