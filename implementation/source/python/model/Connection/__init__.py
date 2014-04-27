import os, json, wx
from Connections import Client
from Connections.User_ClientOf_CentralServer import User_ClientOf_CentralServer as CentralClient
from Responses import *
from twisted.internet import reactor

# This class is defined as a package-level class since this is the only class
# most of our model will need to interface with for networking.
class Connection(object):
   __instance = None
   def __init__(self):
      self.__centralClient = None
      self.__connections = []

      #see self.__loop
      self.__callbacksToCall = []
      self.__argsToPass = []
      self.__continueLoop = True
      self.__loop()

   @staticmethod
   def getInstance():
      if Connection.__instance == None:
         Connection.__instance = Connection()
      return Connection.__instance

   def close(self):
      def closeConnection(connection):
         connection.close()

      map(closeConnection, self.__connections)
      self.__continueLoop = False

      if reactor.running:
         reactor.stop()
      
   # wx can't be called from twisted... fuck
   # two threads now...
   # what this does is start an infinite loop in wx's thread that calls any
   # callbacks that reactor's thread adds to the callback list.
   def __loop(self):
      if self.__continueLoop:
         wx.FutureCall(100, self.__loop)
      callbacks = self.__callbacksToCall
      args = self.__argsToPass
      self.__callbacksToCall = []
      self.__argsToPass = []
      for callback, args in zip(callbacks, args):
         callback(*args)

   # add a callback to be called in __loop (wx thread)
   # args is a list of arguments
   # NOTE.. user-passed callbacks should ONLY be called in wx
   def __addCallback(self, callback, args):
      self.__callbacksToCall.append(callback)
      self.__argsToPass.append(args)

   def authenticate(self, username, password, callback):
      self.__username = username
      self.__password = password
      self.__settings = self.__loadSettings()

      def onAuth(response):
         if response['success']:
            self.__addCallback(callback, [
               AuthenticationSuccess(response['role'], response['classes'])
            ])
         else:
            self.__addCallback(callback, [
               AuthenticationFailure(response['reason'])
            ])

      def tryAuth():
         self.__centralClient.tryAuth(username, password, onAuth)

      def failConnect(reason):
         callback(AuthenticationFailure('Failed to connect to server'))

      self.__connectCentral(tryAuth, failConnect)

   def hostPresentation(self, className, callback):
      pass
   def registerStudentClassesListener(self, listener):
      pass
   def unregisterStudentClassesListener(self, listener):
      pass
   def sendMessage(self, identifier, recipient, message):
      pass
   def registerMessageListener(self, identifier, listener):
      pass
   def unregisterMessageListener(self, identifier, listener):
      pass

   # ----- helper methods ------

   def __loadSettings(self):
      # load and return the settings dictionary from config.json
      configFile = open(os.path.dirname(__file__) + '/config.json')
      return json.load(configFile)

   def __connectCentral(self, callback, failCallback):
      def setCentral(connection):
         if not self.__centralClient:
            # only set the client once.. the user may have sent two responses
            self.__centralClient = connection
            self.__connections.append(connection)
         callback()

      if not self.__centralClient:
         Client.connect(
            self.__settings['central server']['hostname'],
            self.__settings['central server']['port'],
            CentralClient,
            setCentral,
            failCallback
         )
      else:
         callback()

