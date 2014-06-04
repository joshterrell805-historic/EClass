from __init__ import BaseConnection
from twisted.internet import reactor

class User_ClientOf_CentralServer(BaseConnection):
   def __init__(self):
      self.__connected = True
      self.__state = None
      self.__studentClassesListener = None

   def onClose(self, reason):
      self.__connected = False
      self.__closeReason = reason
      self.close()

   def send(self, message, timeout=True):
      # any communication that takes too long is assumed failed.
      if timeout:
         self.__timeoutCall = reactor.callLater(3, self.responseTimeout)

      return super(User_ClientOf_CentralServer, self).send(message)

   def onMessage(self, message):
      #print('receive')
      #print(message)
      if message['code'] == 'classes':
         if self.__studentClassesListener != None:
            self.__studentClassesListener(message['classes'])
         return
      elif message['code'] != self.__state:
         raise Exception(
            "State is '" + (self.__state if self.__state else '')
            + "' but response is '" +
            (message['code'] if message['code'] else '') + "'"
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
   def registerStudentClassesListener(self, listener):
      # TODO support multiple listeners
      self.__studentClassesListener = listener

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

   def unjoinStudent(self, studentKey):
      """Inform the central server that the student failed to join the presentaiton"""
      self.send({
         'code'     : 'cancelJoin',
         'key'      : studentKey
      }, timeout=False)

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
         'reason'  : (self.__state if self.__state else '') + ' response timed out'
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
