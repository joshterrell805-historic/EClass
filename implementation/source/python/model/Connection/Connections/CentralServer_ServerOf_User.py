from __init__ import BaseConnection, Client
import CentralServer_AuthPlugin_Simple as AuthPlugin

# an instance of this class exists for every client
class CentralServer_ServerOf_User(BaseConnection):
   __validCodes = ['authorize']

   def __init__(self):
      self.__loginSuccessResponse = None

   def onMessage(self, message):
      if not self.__verifyString(message, 'code'):
         return

      if message['code'] in self.__validCodes:
         print('receive ' + message['code'] + ' request')
         print(message)
         getattr(self, 'receive_' + message['code'])(message)
      else:
         self.send({'code': 'invalid code', 'request code': message['code']})

   def receive_authorize(self, message):
      if (not self.__verifyString(message, 'username') or
          not self.__verifyString(message, 'password')
      ):
         return

      if self.__loginSuccessResponse:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'   : 'You are already logged in'
            }
         })
         return

      def loginResponse(response):
         if response['success']:
            self.__loginSuccessResponse = response
            self.send({
               'code'    : message['code'],
               'response': {
                  'success' : response['success'],
                  'role'    : response['role'],
                  'classes' : response['classes']
               }
            })
         else:
            self.send({
               'code'    : message['code'],
               'response': {
                  'success' : response['success'],
                  'reason'  : response['reason']
               }
            })

      AuthPlugin.login(
         message['username'], message['password'], loginResponse
      )

   def __verifyString(self, message, key):
      return self.__verifyType(message, key, basestring, 'string')
   def __verifyInt(self, message, key):
      return self.__verifyType(message, key, int, 'int')
   def __verifyDict(self, message, key):
      return self.__verifyType(message, key, dict, 'dict')
   def __verifyType(self, message, key, valueType, valueTypeName):
      try:
         keys = key.split('.')
         value = message
         for k in keys:
            value = value[k]

         if not isinstance(value, valueType):
            raise Exception()
      except:
         self.send({
            'code'   : 'malformed message',
            'reason' : 'missing field or incorrect type',
            'field'  : key,
            'type'   : valueTypeName
         })
         return False

      return True
