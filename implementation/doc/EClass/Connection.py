"""
Connection is the module (which also contains the class, Connection) which
handles communications between different users of EClass. Connection handles
the communicaiton between the student and presenter, presenter and student, and
between all users and the central server.
@author: Josh Terrell jmterrel@calpoly.edu
"""

class Connection:
   """
   Connection class is a singleton
   which represents the connection between the user and everything external. This
   is the class EClass uses to authenticate, join a presentation, ask the presenter
   a question, ...

   Note: listeners can be registered/unregistered whenever. The connection does
   not have to be made before registering a listener. It's advised to set up
   listeners before authenticating so that no messages are missed.

   Note: "simple object" below refers to an object that can be encoded and
   decoded by pickle. See pickle serialization library.

   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self):
      """
      This class is a singleton, DO NOT USE THE CONSTRUCTOR DIRECTLY.
      Instead, use the static method getInstance.
      """
      pass
   def getInstance():
      """
      @return: the single instance of Connection for this user.
      @postcondition: isinstance(@return, Connection)
      """
      pass
   def authenticate(self, username, password, callback):
      """
      Attempt to login. `callback` is called when the authentication has
      succeeded or failed.

      @param username: the user's username
      @type username: string
      @param password: the user's password
      @type password: string
      @param callback: the callback to be called when the authentication request
      succeeds or fails. This callback is passed an AuthenticationResponse
      (AuthenticationSuccess or AuthenticationFailure) as its only argument.
      @type callback: function passed one argument, AuthenticationResponse

      @precondition: hasattr(callback, '__call__')
      """
      pass
   def hostPresentation(self, className, onStudentJoin, callback):
      """
      Attempt to start hosting a presentation for a class. In order for this
      method to succeed, the user must be already authenticated as a presenter,
      he must not be hosting any other presentations, and he must be able
      to host a class for the specified class.

      @param className: the class the presenter wishes to host a
      presentationfor. This class can be any class.name returned in the
      AuthenticationSuccess object from the authenticate callback.
      @type className: string
      @param onStudentJoin: assuming hosting succeeded, this callback will be
      called whenever a student joins the presentation. This callback is called
      with the username of the student that logged in.
      @type onStudentJoin: function
      @param callback: the callback to be called when the attempt to host
      has succeeded or failed.
      @type callback: function passed one argument, HostResponse

      @precondition: hasattr(callback, '__call__') and
      hasattr(onStudentJoin, '__call__')
      """
      pass
   def joinPresentation(self, className, callback):
      """
      Attempt to join a presentation. In order for this method to succeed,
      the user must be logged in as a student and in the class that he attempts
      to join. Additionally, the class must be hosted.
      @param className: the name of the class the student wishes to join. eg
      'CPE 308' This class name can be any class.name from the classes array
      from the AuthenticationSuccess object.
      @type className: string
      @param callback: a function to be called when the attempt to join succeeds
      or fails.
      @type callback: a function with one argument, a JoinResponse

      @precondition: hasattr(callback, '__call__')
      """
      pass
   def registerStudentClassesListener(self, listener):
      """
      Register a listener to be called whenever the list of classes changes.
      A student's list of classes changes when a presenter switches a class
      from hosted to not hosted or visa versa.
      @param listener: the listener to be called whenever the classes change.
      @type listener: a function with one argument, an array of StudentClass

      @precondition: hasattr(callback, '__call__')
      """
      pass
   def unregisterStudentClassesListener(self, listener):
      """
      Unregister a previously registered listener registered with
      registerStudentClassesListener, or unregister all listeners. If listener 
      is None, this method unregisters all listeners. If listener is a funciton,
      this method unregisters the listener passed.
      
      @precondition: listener == None or hasattr(listener, '__call__')
      """
      pass
   def sendMessage(self, identifier, recipient, message):
      """
      Send a message to the person at the other side. This funciton is used for
      one-to-one and one-to-many communicaitons. EG the student sends the
      presenter a quesiton, or the a the presenter adds a layer object to the
      top layer.

      @param identifier: the identifier used for the type of this message eg
      'ask question', 'adjust permissions'. This message will only be received
      by the person at the other side if the person at the other side is
      listening for messages of type `identifier`. @see registerMessageListener
      @type identifier: string
      @param recipient: the recipient to receive this message. If this user is
      a student, this argument must be None (all sent messages go to the
      presenter only; from there the presenter may chose to broadcast the
      message to all other students) If the user is a presenter, this argument
      may be None or a string. If this parameter is None and the user is a
      presenter, the message is sent to all students. If the parameter is a
      string, it is assumed to be the username of the student to send this
      message to.
      @type recipient: string or None
      @param message: the message to send. Must be a simple python object*.

      @precondition: isinstance(identifier, string) && message
      (recipient == None or isinstance(recipient, string))
      """
      pass
   def registerMessageListener(self, identifier, listener):
      """
      Register a listener to be called whenever a message identified by
      `identifier` is received. @see sendMessage

      @param identifier: the identifier indicating the type of message received.
      This identifier must match exaclty the identifier specified in sendMessage
      @type identifier: string
      @param listener: the listener to be called whenever a message of type
      `identifier` is received. This listener is passed two arguments. In order
      they are the sender and the message. The sender is the username of the
      user who sent this message. The sender field is None if the sender is
      the presenter, otherwise the sender is the username of the student who
      sent this message to the presenter. The message is the object sent by
      the sender in sendMessage.
      @type listener: function with two arguments, sender and message

      @precondition: hasattr(listener, '__call__')
      """
      pass
   def unregisterMessageListener(self, identifier, listener):
      """
      Unregister a/some/all message listener(s) previously registered with
      registerMessageListener.

      @param identifier: the identifier of the message listener to unregister.
      @type identifier: string
      @param listener: the listener to unregister
      @type listener: function

      If identifier is None and listener is None, unregister all message
      listeners.

      If identifier is None and listener is a function, unregister all message
      listeners of any indentifier associated with the funciton.

      If identifier is a string and listener is None, unregister all message
      listeners associated with the identifier.

      If identifier is a string and listener is a funciton, unregister all
      message listeners associated with this identifier and function.

      @precondition: (listener == None or hasattr(listener, '__call__')) and
      (identifier == None or isinstance(identifier, string))
      """
      pass

class GenericResponse(object):
   """
   A generic response can either be a success or a failure. A failed generic
   response has self.success == False, and succeeded has response.success ==
   True. If the response is a success, this object is actually an instance of
   GenericSuccess. If the response is a failure, the object is actually an
   instance of GenericFailure. (both of which inherit from this class)

   @ivar success: True for successful, false for fail
   @type success: boolean (read-only)

   Note: all subclasses must invoke the super constructor.
   """
   def __init__(self):
      """
      Don't forget to call the super constructor when inheriting from this
      class!
      """
      pass

class GenericSuccess(GenericResponse):
   """
   A generic success is a GenericResponse that succeeded. A generic success
   may be subclassed to provide state to the recipient of this response.
   """
   def __init__(self):
      """
      Don't forget to call the super constructor when inheriting from this
      class!
      """
      pass

class GenericFailure(GenericResponse):
   """
   A generic failure is a GenericResponse that failed. A generic failure
   may be subclassed to provide more state to the recipient of this response.
   Generic failures have one state variable included, the reason for the
   failure.
   """
   def __init__(self, reason):
      """
      Don't forget to call the super constructor when inheriting from this
      class! (and don't forget to pass the reason (only arg)!)
      """
      super(GenericFailure, self).__init__()
      self.reason = reason

class AuthenticationResponse(GenericResponse):
   """
   This is the response received in the callback when authenticating. It is
   either an instance of AuthenticationSuccess or AuthenticationFailure.
   @ivar success: True for successful, false for fail
   @type success: boolean (read-only)
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   pass

class AuthenticationFailure(GenericFailure):
   """
   @ivar reason: the reason authentication failed (eg 'invalid credentials')
   @type reason: string
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   pass

class AuthenticationSuccess(GenericSuccess):
   """
   @ivar role: the role (student/presenter) of this logged in user
   @type role: string 'student' or 'presenter'
   @ivar classes: the classes this student is enrolled in, or this presenter may
   present for.
   @type classes: an array of StudentClass or PresenterClass
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self, role, classes):
      self.role = role
      self.classes = classes

class Class(object):
   """
   @ivar name: the name of this class (eg 'CPE 308')
   @type name: string
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self, name):
      self.name = name

class StudentClass(Class):
   """
   The type of class in the classes array if the logged in user is a student.
   @ivar presenterFirstName: the first name of the presenter for this class.
   @type presenterFirstName: string
   @ivar presenterLastName: the last name of the presenter for this class.
   @type presenterLastName: string
   @ivar hosted: true if the class is currently being hosted, false if it
   is unavailable to join. To get updates this list of classes, see
   Connection.registerStudentClassesListener.
   @type hosted: boolean (read-only)
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self, name, presenterFirstName, presenterLastName, hosted):
      super(StudentClass, self).__init__(name)
      self.presenterFirstName = presenterFirstName
      self.presenterLastName = presenterLastName
      self.hosted = hosted

class PresenterClass(Class):
   """
   The type of class in the classes array if the logged in user is a presenter.
   @ivar students: an array of students in the class
   @type students: array of Student
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self, name, students):
      super(PresenterClass, self).__init__(name)
      self.students = students

class Student(object):
   """
   @ivar username: username of the student
   @type username: string
   @ivar firstName: first name of the student
   @type firstName: string
   @ivar lastName: last name of the student
   @type lastName: string
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self, username, firstName, lastName):
      self.username = username
      self.firstName = firstName
      self.lastName = lastName

class HostResponse(GenericResponse):
   """
   Response passed to the callback when attempting to host. It is either an
   instance of HostSuccess or HostFailure
   @ivar success: True for successful, false for fail
   @type success: boolean (read-only)
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   pass

class HostSuccess(GenericSuccess): 
   """
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   pass

class HostFailure(GenericFailure):
   """
   @ivar reason: the reason hosting failed (eg 'not a presenter for this class')
   @type reason: string
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   pass

class JoinResponse(object):
   """
   Response passed to the callback when attempting to join. It is either an
   instance of JoinSuccess or JoinFailure
   @ivar success: True for successful, false for fail
   @type success: boolean (read-only)
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   @property
   def success(self):
      if self.__success == None:
         self.__success = isinstance(self, JoinSuccess)
      return self.__success

class JoinSuccess(JoinResponse): 
   """
   @author: Josh Terrell jmterrel@calpoly.edu
   @ivar data: the initial data sent by the presenter to the student upon
   successful join. This dictionary holds thing such as the presentation HTML,
   initial slide number, initial forum messages, etc. 
   @type data: dictionary 
   """
   def __init__(self, initialData):
      pass

class JoinFailure(JoinResponse):
   """
   @ivar reason: the reason joining failed (eg 'not a student of this class')
   @type reason: string
   @author: Josh Terrell jmterrel@calpoly.edu
   """
   def __init__(self, reason):
      self.reason = reason
