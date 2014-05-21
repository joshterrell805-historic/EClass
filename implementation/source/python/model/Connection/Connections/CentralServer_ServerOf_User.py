from __init__ import BaseConnection, Client
import CentralServer_AuthPlugin_Simple as AuthPlugin
import random

# an instance of this class exists for every client
class CentralServer_ServerOf_User(BaseConnection):
   __validCodes = ['authorize', 'host', 'join', 'validateStudent']
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
      self.__hostedClass = None
      self.__joinedClass = None

   def onClose(self, reason):
      if self.__hostedClass != None:
         self.hostedClasses.remove(self.__hostedClass)
         self.__hostedClass = None

   def onMessage(self, message):
      if not self._verifyString(message, 'code'):
         return

      if message['code'] in self.__validCodes:
         print('receive ' + message['code'] + ' request')
         print(message)
         getattr(self, 'receive_' + message['code'])(message)
      else:
         self.send({'code': 'invalid code', 'request code': message['code']})

   def receive_authorize(self, message):
      if (not self._verifyString(message, 'username') or
          not self._verifyString(message, 'password')
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
      if (not self._verifyString(message, 'class') or
          not self._verifyInt(message, 'port')
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
               'reason'  : 'You are not a presenter for this class'
            }
         })
         return

      # verify that presenter isn't already hosting a class
      if self.__hostedClass != None:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : 'You are already hosting a presentation'
            }
         })
         return

      # verify presenter isn't logged in somewhere else hosting this class
      def classMatches(c):
         return (c['name'] == message['class'] and
                c['firstname'] == self.__loginSuccessResponse['firstname'] and
                c['lastname']  == self.__loginSuccessResponse['lastname'])
      hostedClasses = filter(classMatches, self.hostedClasses)
      if len(hostedClasses) != 0:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : ('You are already hosting a presentation for ' +
                  'this class (on another connection)')
            }
         })
         return

      # passed validation! add the class and send the response
      myClass = {
         'name'      : message['class'],
         'port'      : message['port'],
         'ip'        : self.getRemote().host,
         'firstname' : self.__loginSuccessResponse['firstname'],
         'lastname'  : self.__loginSuccessResponse['lastname'],
         'joining'   : {}
      }
      self.__hostedClass = myClass
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

   def receive_join(self, message):
      if (not self._verifyString(message, 'class') or
          not self._verifyString(message, 'lastname') or
          not self._verifyString(message, 'firstname')
      ):
         return

      # verify user logged in as student
      if (not self.__loginSuccessResponse or
          not self.__loginSuccessResponse['role'] == 'student'
      ):
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : ('You must be logged in as a student to join a' +
                  ' presentation')
            }
         })
         return

      # verify student may join a presentation for this class
      def classMatches(aClass):
         return (
            aClass['firstname'] == message['firstname'] and
            aClass['lastname']  == message['lastname'] and
            aClass['name']      == message['class']
         )
      classes = filter(classMatches, self.__loginSuccessResponse['classes'])
      if len(classes) != 1:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : 'You are not enrolled in this class'
            }
         })
         # we done fucked up
         if len(classes) != 0:
            raise Exception('student is enrolled in multiple classes with the' +
               ' same unique key (firstname + lastname + className)'
            )
         return

      # verify student isn't already in a presentation
      if self.__joinedClass != None:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : 'You are already in a presentation'
            }
         })

      # verify a presentation is being hosted for the class
      hostedClasses = filter(classMatches, self.hostedClasses)
      if len(hostedClasses) != 1:
         self.send({
            'code': message['code'],
            'response': {
               'success' : False,
               'reason'  : 'There is no presentation hosted for this course'
            }
         })
         # we done fucked up
         if len(hostedClasses) != 0:
            raise Exception('there are multiple hosted classes with the' +
               ' same unique key (firstname + lastname + className)'
            )
         return

      self.__joinedClass = hostedClasses[0]
      while True:
         self.__joinKey = '%064x' % random.randrange(16**64)
         if not self.__joinKey in self.__joinedClass['joining']:
            self.__joinedClass['joining'][self.__joinKey] = self
            break
      self.send({
         'code': message['code'],
         'response': {
            'success' : True,
            'port'    : self.__joinedClass['port'],
            'ip'      : self.__joinedClass['ip'],
            'key'     : self.__joinKey
         }
      })


   def receive_validateStudent(self, message):
      if not self._verifyString(message, 'key'):
         return

      # verify presenter is hosting a class
      if self.__hostedClass == None:
         self.send({
            'code' : message['code'],
            'response' : {
               'success' : False,
               'reason'  : ('You may not validate students ' +
                  'if you are not hosting a presentation.')
            }
         })
         return

      if not message['key'] in self.__hostedClass['joining']:
         self.send({
            'code' : message['code'],
            'response' : {
               'success' : False,
               'reason'  : 'The student\'s join key is invalid'
            }
         })
         return

      student = self.__hostedClass['joining'][message['key']]
      self.__hostedClass['joining'].pop(message['key'])
      self.send({
         'code' : message['code'],
         'response' : {
            'success' : True,
            'username' : student.__loginSuccessResponse['username']
         }
      })

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
