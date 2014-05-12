from Person import Person
from StudentPermissions import StudentPermissions
from Question import Question

class Student(Person):

   def __init__(self, username, password, permissions = None):
      super(Student, self).__init__(username, password)
      if permissions != None:
         self.permissions = permissions
      else:
         self.permissions = StudentPermissions()
      self.present = True
      self.kicked = False
      self.question = None
      self.pushedLayer = None

   def GetPermissions(self):
      return self.permissions

   def SetPermissions(self, permissions):
      if isinstance(permissions, StudentPermissions):
         self.permissions = permissions
      
   def IsPresent(self):
      return self.present
      
   def SetPresent(self, value):
      if value == True or value == False:
         self.present = value
      
   def IsKicked(self):
      return self.kicked
      
   def SetKicked(self, value):
      if value == True or value == False:
         self.kicked = value
      
   def HasQuestion(self):
      return self.question == None
      
   def GetQuestion(self):
      return self.question
      
   def SetQuestion(self, question):
      if isinstance(question, Question):
         self.question = question
         
   def GetPushedLayer(self):
      return self.pushedLayer
      
   def SetPushedLayer(self, layer):
      self.pushedLayer = layer
