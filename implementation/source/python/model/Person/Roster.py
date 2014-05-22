class Roster:
   def setView(self, view):
      self.__view = view;
   def __init__(self):
      self.__view = None
      self.students = []
      """
      self.sObjs = [Student("Alek Squires", "")],
      Student("Alexa Fox", ""),
      Student("Carson Carroll", ""),
      Student("Emilio Cavazos", ""),
      Student("Haylee Springer", ""),
      Student("Jared Osborn", ""),
      Student("John Hanna", ""),
      Student("Kelsey Hansen", ""),
      Student("Kevin Wiebe", ""),
      Student("Mike Sevilla", ""),
      Student("Ryan Ginsberg", ""),
      Student("Tim Anderson", "")]"""

   def AddNewStudent(self):
      print('From Roster.AddNewStudent()')

   def RemoveStudent(self):
      print('From Roster.RemoveStudent()')

   def SortList(self, list):
      list.sort()
   
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
      self.__view and self.__view.redraw()
   
