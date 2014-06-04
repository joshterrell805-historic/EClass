import sys
from Presentation.Presentation import Presentation

from Person.Person import Person
from Person.Presenter import Presenter
from Person.Roster import Roster
from Person.Student import Student

from Presentation.Layer import Layer
from Presentation.LayerManagerModel import LayerManagerModel
from Presentation.QuestionList import QuestionList
from Connection import Connection

from Forum.Forum import Forum

# this model is a singleton which has a reference to other important models

class EClass():

   __instance = None

   @staticmethod
   def GetInstance():
      if EClass.__instance == None:
         EClass.__instance = EClass()

      return EClass.__instance

   def __init__(self):

      self.connection = Connection.getInstance()
      self.presentation = Presentation(path = None)
      self.roster = Roster()
      self.forum = Forum()
      self.questionList = QuestionList()
      # this is an object sent to every client when they connect.
      # you may modify it (eclass.initialData['my value'] = crap),
      # but do not overwrite it (eclass.initialData = crap)
      # this value appears in the client at view/JoinPresentation.callback
      # as the "data" field of response
      self.initialData = {}

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
      if len(self.presentation.slides) != 0:
         layers = self.presentation.slides[self.presentation.currSlideNum].layers
         self.layerManagerModel = LayerManagerModel(self, layers)
      else:
         self.layerManagerModel = LayerManagerModel(self, [])

   def exit(self):
      self.connection.close()
      sys.exit()

   def setPresentation(self, path):
      EClass.GetInstance().presentation.SetPath(path)
      EClass.GetInstance().presentation.Slidify()
      EClass.GetInstance().setUpLayerManager()
