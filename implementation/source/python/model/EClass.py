import sys
from Presentation.Presentation import Presentation

from Person.Person import Person
from Person.Student import Student
from Person.Presenter import Presenter

from Presentation.Layer import Layer
from Presentation.LayerManagerModel import LayerManagerModel
from Connection import Connection

# this model is a singleton which has a reference to other important models

class EClass():

   __instance = None

   @staticmethod
   def GetInstance():
      print('In EClass.GetInstance(): ')

      if EClass.__instance == None:
         EClass.__instance = EClass()

      return EClass.__instance

   def __init__(self):

      self.connection = Connection.getInstance()
      self.presentation = Presentation(path = None)

      # the logged in user, None if logged out
      self.user = None

   def Login(self, username, password, onSuccess, onFailure):
      print('From EClass.Login(): ' + username + ' ' + password)

      def onResponse(authResponse):
         if authResponse.success:
            if authResponse.role == 'presenter':
               self.user = Presenter(username, password)
            else:
               self.user = Student(username, password)

            # warning! contains different data for presenter and student
            # see networking.html for what it contains
            self.classes = authResponse.classes

            onSuccess()
         else:
            onFailure(authResponse.reason)

      self.connection.authenticate(username, password, onResponse)

   def setUpLayerManager(self):
      print('In EClass.setUpLayerManager()')

      self.layerManagerModel = LayerManagerModel()

   def exit(self):
      self.connection.close()
      sys.exit()
