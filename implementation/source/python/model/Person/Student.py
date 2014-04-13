from Person import Person
from StudentPermissions import StudentPermissions

class Student(Person):

   def __init__(self, username, password, permissions = StudentPermissions()):
      super(Student, self).__init__(username, password)
      self._permissions = permissions

   @property
   def permissions(self):
      print('From Student.permissions.getter')
      return self._permissions

   @permissions.setter
   def permissions(self, value):
      print('From Student.permissions.setter')
      self._permissions = value
