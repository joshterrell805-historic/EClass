from Person import Person
from StudentPermissions import StudentPermissions

class Student(Person):

   def __init__(self, username, password, permissions = StudentPermissions()):
      super(Student, self).__init__(username, password)
      self.permissions = permissions

   def GetPermissions(self):
      print('From Student.GetPermissions()')
      return self.permissions

   def SetPermissions(self, value):
      print('From Student.SetPermissions()')
      self.permissions = value
