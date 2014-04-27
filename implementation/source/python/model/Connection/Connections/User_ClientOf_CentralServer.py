from __init__ import BaseConnection

class User_ClientOf_CentralServer(BaseConnection):
   def __init__(self):
      self.__connected = True
      self.__state = None

   def onClose(self, reason):
      self.__connected = False
      self.__closeReason = reason

   def onMessage(self, message):
      print('receive')
      print(message)
      if message['code'] != self.__state:
         raise Exception(
            "State is '" + self.__state + "' but response is '" +
            message['code'] + "'"
         )

      self.__state = None
      self.__stateCallback(message['response'])

   def tryAuth(self, username, password, callback):
      self.prepareSend()
      self.__state = 'authorize'
      self.__stateCallback = callback
      self.send({
         'code'     : 'authorize',
         'username' : username,
         'password' : password
      })
      print('awaiting login response')
      
   def prepareSend(self):
      """ make sure that we're still connected and we're not waiting for a
      response from the server""" 

      if not self.__connected:
         raise Exception("Connection is closed: " + self.__closeReason)
      if self.__state:
         raise Exception("Cannot send message while " + self.__state)
