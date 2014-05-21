from __init__ import BaseConnection
from twisted.internet import reactor

# a connection to a student
class Presenter_ServerOf_Student(BaseConnection):
   def __init__(self):
      pass

   def onClose(self, reason):
      pass

   def setCentralClient(self, centralClient):
      # the connection to the central client
      self.__centralClient = centralClient

   def setJoinCallback(self, joinCallback):
      # called when a new student joins the presentation. username is only param
      self.__joinCallback = joinCallback

   def onMessage(self, message):
      if message['code'] == 'join':
         self.onJoin(message)

   def onJoin(self, message):
      def onStudentValidation(response):
         self.send({
            'code' : 'join',
            'response' : response
         })
         if response['success']:
            self.__joinCallback(response['username'])
         else:
            self.close()

      # A student wishes to join the presentation
      if not self._verifyString(message, 'key'):
         return

      self.__centralClient.validateStudent(message['key'], onStudentValidation)
