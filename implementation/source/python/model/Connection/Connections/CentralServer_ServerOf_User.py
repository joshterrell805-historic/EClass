from __init__ import BaseConnection, Client
import CentralServer_AuthPlugin_Simple as AuthPlugin

# an instance of this class exists for every client
class CentralServer_ServerOf_User(BaseConnection):
   __validCodes = ['authorize', 'host']
   __hostedClasses = []

   @property
   def hostedClasses(self):
      # returns an array shared by all connections of the hosted classes
      # contains name(class),
      # first and  lastname(presenter),
      # port
      # students(username)
      return CentralServer_ServerOf_User.__hostedClasses

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
               'success'  : False,
               'reason'   : 'You are already logged in'
            }
         })
         return

      def loginResponse(response):
         if response['success']:
            self.__loginSuccessResponse = response
            if response['role'] == 'student':
               self.__updateMyClasses()
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

   def receive_host(self, message):
      if (not self.__verifyString(message, 'class') or
          not self.__verifyInt(message, 'port')
      ):
         return

      # verify user logged in as presenter
      if (not self.__loginSuccessResponse or
          not self.__loginSuccessResponse['role'] == 'presenter'
      ):
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : ('You must be logged in as a presenter to host a' +
                  ' presentation')
            }
         })
         return

      # verify presenter may host a presentation for this class
      def getClassName(aClass):
         return aClass['name']
      if (not message['class'] in
            map(getClassName, self.__loginSuccessResponse['classes'])
      ):
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : 'You may not host a presentation for this class'
            }
         })
         return

      def isMyClass(aClass):
         return (
            self.__loginSuccessResponse['firstname'] == aClass['firstname'] and
            self.__loginSuccessResponse['lastname'] == aClass['lastname']
         )
      myClasses = filter(isMyClass, self.hostedClasses)

      # verify that presenter isn't already hosting a class
      if len(myClasses) != 0:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : 'You are already hosting a presentation'
            }
         })
         # we done fucked up
         if len(myClasses) != 1:
            raise Exception('presenter is hosting more than one class')

      # passed validation! add the class and send the response
      myClass = {
         'name' : message['class'],
         'port' : message['port'],
         'firstname' : self.__loginSuccessResponse['firstname'],
         'lastname'  : self.__loginSuccessResponse['lastname'],
         'students'  : []
      }
      self.hostedClasses.append(myClass)
      self.send({
         'code' : message['code'],
         'response': {
            'success': True
         }
      })
      print(myClass['firstname'] + ' ' + myClass['lastname'] + ' is hosting ' +
         myClass['name'])


      # TODO notify students that the hosted classes have changed

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

   def __updateMyClasses(self):
      # update this student's list of classes so with hosted information

      def isHosted(myClass):
         def classesEquivalent(hostedClass):
            return (
               myClass['firstname'] == hostedClass['firstname'] and
               myClass['lastname'] == hostedClass['lastname'] and
               myClass['name'] == hostedClass['name']
            )
         # if myclass has the same name, firstname, and lastname as a class
         # in hostedClasses, then my class is hosted
         return len(filter(classesEquivalent, self.hostedClasses)) != 0

      for myClass in self.__loginSuccessResponse['classes']:
         if isHosted(myClass):
            myClass['hosted'] = True
         else:
            myClass['hosted'] = False
