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
      self.__saveListeners = {}
      # set in WhiteboardNav
      self.RefreshSlide = None
      self.Redraw = None

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

   def savePresentationToFile(self, path):
      data = {}
      for identifier in self.__saveListeners:
         data[identifier] = self.__saveListeners[identifier](
            'save to file', identifier
         )
      f = open(path, 'w')
      import json
      json.dump(data, f)
      f.close()

   def loadPresentationFromFile(self, path):
      if path.endswith('.creampie'):
         f = open(path, 'r')
         import json
         data = json.load(f)
         self.loadFileData(data)
      elif path.endswith('.html'):
         EClass.GetInstance().presentation.SetPath(path)
         EClass.GetInstance().presentation.Slidify()
         EClass.GetInstance().setUpLayerManager()
      else:
         raise Exception('unknown filetype: ' + path)

   def registerOnSaveListener(self, identifier, callback):
      if identifier in self.__saveListeners:
         raise Exception("'" + identifier + "'is not unique.")
      self.__saveListeners[identifier] = callback

   def getStudentInitialData(self):
      data = {}
      for identifier in self.__saveListeners:
         data[identifier] = self.__saveListeners[identifier](
            'save initial data for student', identifier
         )
      return data

   def loadInitialData(self, data):
      for identifier in data:
         # obj = whatever you returned from 'callback' in registerOnSaveListener
         obj = data[identifier]

         if identifier == 'presentation':
            self.presentation.loadInitialData(obj)
         elif identifier == 'forum':
            self.forum.loadInitialData(obj)
         else:
            if obj is not None:
               raise Exception(
                  "Unhandled initial data '" + identifier + "'"
               )
      self.refreshView()
            
   def loadFileData(self, data):
      for identifier in data:
         # obj = whatever you returned from 'callback' in registerOnSaveListener
         obj = data[identifier]

         if identifier == 'presentation':
            self.presentation.loadFileData(obj)
         else:
            if obj is not None:
               raise Exception(
                  "Unhandled file data '" + identifier + "'"
               )
      self.refreshView()
   def refreshView(self):
      def _refresh():
         assert self.RefreshSlide is not None
         self.RefreshSlide()
         assert self.Redraw is not None
         self.Redraw()
      import wx
      wx.CallLater(1, _refresh) #lol
