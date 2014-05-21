import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Person')

from Roster import Roster

class RosterTest(unittest.TestCase):

   def setUp(self):
      self.roster = Roster()
      #TODO: fix test below to be a dynamic test
      self.assertEqual(12, len(self.roster.students))

   def test_SortList(self):
      self.roster.SortList(self.roster.students)
      self.assertTrue(sorted(self.roster.students))

if __name__ == '__main__':
    unittest.main()
