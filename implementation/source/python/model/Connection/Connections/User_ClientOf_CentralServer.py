from __init__ import BaseConnection
from twisted.internet import reactor

class User_ClientOf_CentralServer(BaseConnection):
   def __init__(self):
      self.__connected = True
      self.__state = None

   def onClose(self, reason):
      self.__connected = False
      self.__closeReason = reason

   def onMessage(self, message):
      #print('receive')
      #print(message)
      if message['code'] != self.__state:
         raise Exception(
            "State is '" + self.__state + "' but response is '" +
            message['code'] + "'"
         )

      self.__timeoutCall.cancel()
      self.__state = None
      self.__stateCallback(message['response'])

   def tryAuth(self, username, password, callback):
      self.prepareSend()
      self.__state = 'authorize'
      self.__stateCallback = callback
      self.send({
         'code'     : self.__state,
         'username' : username,
         'password' : password
      })
      self.__timeoutCall = reactor.callLater(3, self.responseTimeout)

   def tryHost(self, className, port, callback):
      self.prepareSend()
      self.__state = 'host'
      self.__stateCallback = callback
      self.send({
         'code'  : self.__state,
         'class' : className,
         'port'  : port
      })
      self.__timeoutCall = reactor.callLater(3, self.responseTimeout)

   def responseTimeout(self):
      state = self.__state
      self.__state = None
      self.__stateCallback({
         'success' : False,
         'reason'  : state + ' response timed out'
      })
      
   def prepareSend(self):
      """ make sure that we're still connected and we're not waiting for a
      response from the server""" 

      if not self.__connected:
         raise Exception("Connection is closed: " + self.__closeReason)
      if self.__state:
         raise Exception("Cannot send message while " + self.__state)
