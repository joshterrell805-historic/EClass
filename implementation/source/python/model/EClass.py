
from Presentation.Presentation import Presentation
from Person.Person import Person
from Person.Student import Student

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

      # valid credentials?
      if True:
         self.user = Person(username, password)
