from __init__ import BaseConnection
from twisted.internet import reactor

# a connection to a student
class Presenter_ServerOf_Student(BaseConnection):
   def __init__(self):
      self.__joinCallback = None
      self.__leaveCallback = None
      self.__joinSuccessResponse = None
      self.__messageListener = None

   def onClose(self, reason):
      if self.__joinSuccessResponse != None and self.__leaveCallback != None:
         self.__leaveCallback(self.__joinSuccessResponse['username'])

   def getUsername(self):
      return (
         self.__joinSuccessResponse['username'] if
         self.__joinSuccessResponse is not None else
         None
      )

   def setCentralClient(self, centralClient):
      # the connection to the central client
      self.__centralClient = centralClient

   def setJoinCallback(self, joinCallback):
      # called when a new student joins the presentation. username is only param
      self.__joinCallback = joinCallback
      
   def setLeaveCallback(self, leaveCallback):
      # called when a student leave the presentation. username is only param
      self.__leaveCallback = leaveCallback

   def onMessage(self, message):
      if message['code'] == 'message':
         message['student'] = self.__joinSuccessResponse['username']
         self.__messageListener and self.__messageListener(message)

      if message['code'] == 'join':
         self.onJoin(message)

   def onJoin(self, message):
      def onStudentValidation(response):
         self.send({
            'code' : 'join',
            'response' : response
         })
         if response['success']:
            self.__joinSuccessResponse = response
            self.__joinCallback(response['username'])
         else:
            self.close()

      # A student wishes to join the presentation
      if not self._verifyString(message, 'key'):
         return

      self.__centralClient.validateStudent(message['key'], onStudentValidation)

   def setMessageListener(self, callback):
      self.__messageListener = callback
