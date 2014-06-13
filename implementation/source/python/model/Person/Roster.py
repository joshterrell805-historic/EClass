import sys
sys.path.insert(0, '../../view')

from Student import Student

class Roster:
   def __init__(self):
      self.__view = None
      self.students = []
      self.studentsPresent = []
      self.studentsAbsent = []

   def setView(self, view):
      self.__view = view;

   def SortList(self):
      def GetKeyName(item):
         return item.firstName
      self.students.sort(key=GetKeyName)
      self.studentsPresent.sort(key=GetKeyName)
      self.studentsAbsent.sort(key=GetKeyName)

   def GetRoster(self):
      def studentToString(student):
         return student.lastName + ', ' + student.firstName
      return map(studentToString, self.students)

   def onJoin(self, username):
      print(username + ' joined the presentation!')
      def matchesUsername(student):
         return student.username == username
      students = filter(matchesUsername, self.students)

      removeIndex = None
      if len(students) == 1:
         students[0].present = True
         self.studentsPresent.append(students[0])
         for i in range(0, len(self.studentsAbsent)):
            if self.studentsAbsent[i].username == students[0].username:
               removeIndex = i
         del self.studentsAbsent[removeIndex]
         self.SortList()

      else:
         raise Exception(username + ' should (but doesn\'t) exist in roster')
      self.__view and self.__view.Redraw()

   def onLeave(self, username):
      def matchesUsername(student):
         return student.username == username
      students = filter(matchesUsername, self.students)

      removeIndex = None
      if len(students) == 1:
         students[0].present = False
         self.studentsAbsent.append(students[0])
         for i in range(0, len(self.studentsPresent)):
            if self.studentsPresent[i].username == students[0].username:
               removeIndex = i
         del self.studentsPresent[removeIndex]
         self.SortList()
      else:
         raise Exception(username + ' should (but doesn\'t) exist in roster')
      self.__view and self.__view.Redraw()
   
   def setStudents(self, students):
      def toStudent(student):
         newStudent = Student(student['username'], student['firstname'], student['lastname'])
         return newStudent
      # contains Student objects
      self.students = map(toStudent, students)
      self.studentsAbsent = map(toStudent, students)
      self.SortList()
      self.__view and self.__view.Redraw()
   
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
