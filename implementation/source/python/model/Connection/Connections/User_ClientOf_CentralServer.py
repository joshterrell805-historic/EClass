from __init__ import BaseConnection
from twisted.internet import reactor

class User_ClientOf_CentralServer(BaseConnection):
   def __init__(self):
      self.__connected = True
      self.__state = None

   def onClose(self, reason):
      self.__connected = False
      self.__closeReason = reason
      self.close()

   def send(self, message):
      # any communication that takes too long is assumed failed.
      self.__timeoutCall = reactor.callLater(3, self.responseTimeout)
      return super(User_ClientOf_CentralServer, self).send(message)

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
      if not self.prepareSend(callback):
         return
      self.__state = 'authorize'
      self.__stateCallback = callback
      self.send({
         'code'     : self.__state,
         'username' : username,
         'password' : password
      })

   def tryHost(self, className, port, callback):
      if not self.prepareSend(callback):
         return
      self.__state = 'host'
      self.__stateCallback = callback
      self.send({
         'code'  : self.__state,
         'class' : className,
         'port'  : port
      })

   def tryJoin(self, className, presenterLastName, presenterFirstName,
      callback
   ):
      if not self.prepareSend(callback):
         return

      self.__state = 'join'
      self.__stateCallback = callback
      self.send({
         'code'      : self.__state,
         'class'     : className,
         'lastname'  : presenterLastName,
         'firstname' : presenterFirstName
      })

   def validateStudent(self, studentKey, callback):
      """verify that the student may join this presentation"""
      if not self.prepareSend(callback):
         return

      self.__state = 'validateStudent'
      self.__stateCallback = callback
      self.send({
         'code'      : self.__state,
         'key'       : studentKey
      })

   def responseTimeout(self):
      state = self.__state
      self.__state = None
      self.__stateCallback({
         'success' : False,
         'reason'  : state + ' response timed out'
      })
      
   def prepareSend(self, callback):
      """ make sure that we're still connected and we're not waiting for a
      response from the server""" 

      if not self.__connected:
         callback({'success': False, 'reason': 'Connection is closed'})
         return False
      if self.__state:
         callback({
            'success': False,
            'reason': ('Cannot send message while waiting for ' + self.__state
            + ' response')
         })
         return False
      return True
