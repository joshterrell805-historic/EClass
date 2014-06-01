import sys
import operator
sys.path.insert(0, '../../view')

from Student import Student

class Roster:
   def __init__(self):
      self.__view = None
      self.students = []

   def setView(self, view):
      self.__view = view;

   def AddNewStudent(self):
      print('From Roster.AddNewStudent()')

   def RemoveStudent(self):
      print('From Roster.RemoveStudent()')

   def SortList(self):
      def GetKeyName(item):
         return item.firstName
      self.students.sort(key=GetKeyName)
      def GetKeyPresent(item):
         return item.present
      self.students.sort(key=GetKeyPresent, reverse=True)


   def GetRoster(self):
      def studentToString(student):
         return student.lastName + ', ' + student.firstName
      return map(studentToString, self.students)

   def onJoin(self, username):
      print(username + ' joined the presentation!')
      def matchesUsername(student):
         return student.username == username
      students = filter(matchesUsername, self.students)

      if len(students) == 1:
         students[0].present = True
      else:
         raise Exception(username + ' should (but doesn\'t) exist in roster')
      self.__view and self.__view.redraw()

   def onLeave(self, username):
      print(username + ' left the presentation!')
      def matchesUsername(student):
         return student.username == username
      students = filter(matchesUsername, self.students)

      if len(students) == 1:
         students[0].present = False
      else:
         raise Exception(username + ' should (but doesn\'t) exist in roster')
      self.__view and self.__view.redraw()
   
   def setStudents(self, students):
      def toStudent(student):
         newStudent = Student(student['username'], student['firstname'], student['lastname'])
         return newStudent
      # contains Student objects
      self.students = map(toStudent, students)
      self.SortList()
      self.__view and self.__view.redraw()
   
   # return the student if he exists, otherwise None
   def findStudentByUsername(self, username):

      def hasUsername(student):
         return student.username == username

      studentsWithUsername = filter(hasUsername, self.students)

      if len(studentsWithUsername) != 1:
         if len(studentWithUsername) >= 2:
            raise Exception("multiple students exist with the same username")
         else: # len == 0
            return False
      return studentsWithUsername[0]
