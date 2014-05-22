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
      def GetKey(item):
         return item.firstname
      self.students.sort(key=GetKey)
   
   def GetRoster(self):
      def studentToString(student):
         return student.lastname + ', ' + student.firstname
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
         # temporary because there's errors when including student.
         class Student():
            pass
         newStudent = Student()
         newStudent.username = student['username']
         newStudent.present = False
         # temporary... these should be passed to the constructor
         newStudent.firstname = student['firstname']
         newStudent.lastname = student['lastname']
         return newStudent
      # contains Student objects
      self.students = map(toStudent, students)
      self.SortList()
      self.__view and self.__view.redraw()
   
