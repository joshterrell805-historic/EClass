
from Presentation.Presentation import Presentation
from Person.Person import Person
from Person.Student import Student
from Person.Presenter import Presenter

# this model is a singleton which has a reference to other important models

class EClass():

   __instance = None

   @staticmethod
   def getInstance():

      if EClass.__instance == None:
         EClass.__instance = EClass()

      return EClass.__instance

   def __init__(self):

      self.presentation = Presentation(path = None)

      # the logged in user, None if logged out
      self.user = None

   def Login(self, username, password):
      print('From EClass.Login(): ' + username + ' ' + password)

      if username == 'presenter':
         self.user = Presenter(username, password)
      elif username == 'student':
         self.user = Student(username, password)
      else:
         # for now just assume it's a student
         self.user = Student(username, password)
