from __init__ import BaseConnection
from twisted.internet import reactor

# a connection from a student to a presenter
class Student_ClientOf_Presenter(BaseConnection):
   def __init__(self):
      self.__state = None
      self.__messageListener = None

   def onClose(self, reason):
      pass

   def onMessage(self, message):
      if message['code'] == 'message':
         message['student'] = False
         self.__messageListener and self.__messageListener(message)

      if self.__state != None:
         if message['code'] != self.__state:
            raise Exception(
               "State is '" + self.__state + "' but response is '" +
               message['code'] + "'"
            )
         else:
            self.__timeoutCall.cancel()
            self.__state = None
            self.__stateCallback(message['response'])

   def tryJoin(self, key, callback):
      self.__state = 'join'
      self.__stateCallback = callback;
      self.send({
         'code'   : self.__state,
         'key'    : key
      });
      self.__timeoutCall = reactor.callLater(3, self.responseTimeout)

   def responseTimeout(self):
      state = self.__state
      self.__state = None
      self.__stateCallback({
         'success' : False,
         'reason'  : state + ' response timed out'
      })

   def setMessageListener(self, callback):
      self.__messageListener = callback
