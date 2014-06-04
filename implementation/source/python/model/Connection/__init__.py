import os, json, wx
from Connections import Client, Server
from Connections.User_ClientOf_CentralServer import User_ClientOf_CentralServer as CentralClient
from Connections.Presenter_ServerOf_Student import Presenter_ServerOf_Student as PresenterServer
from Connections.Student_ClientOf_Presenter import Student_ClientOf_Presenter as PresenterClient
from Responses import *
from twisted.internet import reactor
import EClass

# This class is defined as a package-level class since this is the only class
# most of our model will need to interface with for networking.
class Connection(object):
   __instance = None
   def __init__(self):
      self.__centralClient = None
      self.__presenterClient = None
      self.__presenterServer = None
      self.__connections = []
      self.__messageListeners = {}

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

      if self.__presenterServer:
         self.__presenterServer.stopListening()

      if reactor.running:
         reactor.stop()

      # you got one second to exit, reactor
      # TODO figure out how to actually kill reactor the right way..
      # this was added because whenever a connection closes it we can't
      # close out of reactor.. it just hangs for a minute then finally dies.
      import time
      time.sleep(1)
      if reactor.running:
         print('reactor still running.. killing process')
         import os, signal
         os.kill(os.getpid(), signal.SIGKILL)
      
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

      self.__connectCentral(tryAuth, self.__connectCentralFail(callback))

   def hostPresentation(self, className, callback, joinCallback, leaveCallback):
      def onHost(response):
         if response['success']:
            self.__addCallback(callback, [
               HostSuccess()
            ])
         else:
            self.__addCallback(callback, [
               HostFailure(response['reason'])
            ])

      def tryHost():
         self.__centralClient.tryHost(className,
            self.__presenterServer.getHost().port, onHost
         )

      def doneStarting():
         self.__connectCentral(tryHost, self.__connectCentralFail(callback))

      self.__startPresentationServer(doneStarting, joinCallback, leaveCallback)

   def joinPresentation(self, className, presenterLastName,
      presenterFirstName, callback
   ):

      # confusing... :( need to refactor
      def onJoinCentral(response):
         def onJoinPresenter(responseJoin):
            if responseJoin['success']:
               self.__addCallback(callback, [
                  JoinSuccess(responseJoin['data'])
               ])
            else:
               self.__addCallback(callback, [
                  JoinFailure(responseJoin['reason'])
               ])

         def tryJoinPresenter():
            # success connecting to the presenter's computer; now try joining
            # the presentation.
            self.__presenterClient.tryJoin(response['key'],
               onJoinPresenter
            )

         def failConnectPresenter():
            self.__addCallback(callback, [
               JoinFailure('Failed to connect to presenter')
            ])


         # The central server has let us through, now connect to presenter
         if response['success']:
            self.__connectPresenter(response['ip'], response['port'],
               tryJoinPresenter, failConnectPresenter)
         else:
            self.__addCallback(callback, [
               JoinFailure(response['reason'])
            ])

      def tryJoinCentral():
         self.__centralClient.tryJoin(className, presenterLastName,
            presenterFirstName, onJoinCentral
         )

      self.__connectCentral(tryJoinCentral, self.__connectCentralFail(callback))

   def registerStudentClassesListener(self, listener):
      def wrappedListener(classes):
         self.__addCallback(listener, [classes])

      assert self.__centralClient != None

      self.__centralClient.registerStudentClassesListener(wrappedListener)

   def unregisterStudentClassesListener(self, listener):
      pass
   def send(self, identifier, message, recipient = None):
      # recipient can be the name of any one student or None to send to all students / the presenter
      msg = {
         'code' : 'message',
         'identifier' : identifier,
         'message' : message
      }

      if EClass.EClass.GetInstance().user.isPresenter():
         if recipient is not None:
            def matchesUsername(connection):
               return connection.getUsername() == recipient
            connections = filter(matchesUsername,
               self.__presenterServer.connections
            )
            assert len(connections) is 1, \
            recipient + "'s connections: " + str(len(connections))

            connections[0].send(msg)
         else:
            for student in self.__presenterServer.connections:
               student.send(msg)
      else:
         self.__presenterClient.send(msg)
   def registerMessageListener(self, identifier, listener):
      self.__messageListeners[identifier] = listener
   def unregisterMessageListener(self, identifier, listener):
      del self.__messageListeners[identifier]
   def onMessage(self, message):
      if ('identifier' in message and
          message['identifier'] in self.__messageListeners
      ):
         self.__addCallback(self.__messageListeners[message['identifier']],
            [message['message'], message['student']]
         )
   
   def CloseConnection(self, studentName):
      def matchesUsername(connection):
         return connection.getUsername() == studentName
      connections = filter(matchesUsername,
         self.__presenterServer.connections
      )
      assert len(connections) is 1, \
      recipient + "'s connections: " + str(len(connections))
      
      connections[0].close()
      

   # ----- helper methods ------

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

   def __loadSettings(self):
      # load and return the settings dictionary from config.json
      configFile = open(os.path.dirname(__file__) + '/config.json')
      return json.load(configFile)

   def __connectCentralFail(self, callback):
      # return a callback which (when called) lets the user know of failure
      # in a GenericFailure
      def addFailCallback():
         self.__addCallback(callback, [
            GenericFailure('Failed to connect to central server')
         ])

      return addFailCallback

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

   def __connectPresenter(self, hostname, port, callback, failCallback):
      def setPresenter(connection):
         if not self.__presenterClient:
            # only set the client once.. the user may have sent two responses
            self.__presenterClient = connection
            self.__connections.append(connection)
            connection.setMessageListener(self.onMessage)
         callback()

      if not self.__presenterClient:
         Client.connect(
            hostname,
            port,
            PresenterClient,
            setPresenter,
            failCallback
         )
      else:
         callback()

   def __startPresentationServer(self, callback, joinCallback, leaveCallback):
      def setPresenter(listeningPort):
         if not self.__presenterServer:
            self.__presenterServer = listeningPort
            self.__presenterServer.connections = []
            print('done starting presenter server')
         callback()

      def onConnection(connection):
         self.__presenterServer.connections.append(connection)
         connection.setCentralClient(self.__centralClient)
         connection.setJoinCallback(joinCallback)
         connection.setMessageListener(self.onMessage)
         connection.setLeaveCallback(leaveCallback)

      if not self.__presenterServer:
         Server.listen(
            0,
            PresenterServer,
            setPresenter,
            onConnection
         )
      else:
         callback()
