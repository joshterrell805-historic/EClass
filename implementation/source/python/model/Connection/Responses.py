#--- Generic
class GenericResponse(object):
   def __init__(self):
      self.__success = None

   @property
   def success(self):
      if self.__success == None:
         self.__success = isinstance(self, GenericSuccess)
      return self.__success

class GenericSuccess(GenericResponse):
   def __init__(self):
      super(GenericSuccess, self).__init__()

class GenericFailure(GenericResponse):
   def __init__(self, reason):
      super(GenericFailure, self).__init__()
      self.reason = reason


#--- Authentication
class AuthenticationResponse(GenericResponse):
   def __init__(self):
      super(AuthenticationResponse, self).__init__()

class AuthenticationFailure(GenericFailure):
   def __init__(self, reason):
      super(AuthenticationFailure, self).__init__(reason)

class AuthenticationSuccess(GenericSuccess):
   def __init__(self, role, classes):
      super(AuthenticationSuccess, self).__init__()
      self.role = role
      self.classes = classes


#--- Host
class HostResponse(GenericResponse):
   def __init__(self):
      super(HostResponse, self).__init__()

class HostFailure(GenericFailure):
   def __init__(self, reason):
      super(HostFailure, self).__init__(reason)

class HostSuccess(GenericSuccess):
   def __init__(self):
      super(HostSuccess, self).__init__()

#--- Join
class JoinResponse(GenericResponse):
   def __init__(self):
      super(JoinResponse, self).__init__()

class JoinFailure(GenericFailure):
   def __init__(self, reason):
      super(JoinFailure, self).__init__(reason)

class JoinSuccess(GenericSuccess):
   def __init__(self, initialData):
      super(JoinSuccess, self).__init__()
      self.data = initialData
