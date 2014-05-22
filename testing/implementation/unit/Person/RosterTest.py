import unittest
import sys
sys.path.insert(0, '../../../implementation/source/python/model')

from Person.Roster import Roster

class RosterTest(unittest.TestCase):

   def setUp(self):
      self.roster = Roster()
      self.assertEqual(0, len(self.roster.students))

   def test_setStudents(self):
      studs = [{'username' : 'jmterrel', 'firstname' : 'Josh', 'lastname' : 'Terrell'}, 
      {'username' : 'ccarro03', 'firstname' : 'Carson', 'lastname' : 'Carroll'},
      {'username' : 'jnwilcox', 'firstname' : 'Joel', 'lastname' : 'Wilcox'},
      {'username' : 'mjsevill', 'firstname' : 'Mike', 'lastname' : 'Sevilla'}]

      self.roster.setStudents(studs)

      self.assertEqual(4, len(self.roster.students))

   def test_SortList(self):
      studs = [{'username' : 'jmterrel', 'firstname' : 'Josh', 'lastname' : 'Terrell'}, 
      {'username' : 'ccarro03', 'firstname' : 'Carson', 'lastname' : 'Carroll'},
      {'username' : 'jnwilcox', 'firstname' : 'Joel', 'lastname' : 'Wilcox'},
      {'username' : 'mjsevill', 'firstname' : 'Mike', 'lastname' : 'Sevilla'}]

      self.roster.setStudents(studs)

      self.assertEqual(len(self.roster.students), 4)
      self.roster.SortList()

      self.assertEqual(self.roster.students[0].firstName, 'Carson')
      self.assertEqual(self.roster.students[1].firstName, 'Joel')
      self.assertEqual(self.roster.students[2].firstName, 'Josh')
      self.assertEqual(self.roster.students[3].firstName, 'Mike')


if __name__ == '__main__':
    unittest.main()
