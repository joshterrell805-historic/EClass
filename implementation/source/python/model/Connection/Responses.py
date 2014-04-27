
class AuthenticationResponse(object):
   def __init__(self):
      self.__success = None

   @property
   def success(self):
      if self.__success == None:
         self.__success = isinstance(self, AuthenticationSuccess)
      return self.__success

class AuthenticationFailure(AuthenticationResponse):
   def __init__(self, reason):
      super(AuthenticationFailure, self).__init__()
      self.reason = reason

class AuthenticationSuccess(AuthenticationResponse):
   def __init__(self, role, classes):
      super(AuthenticationSuccess, self).__init__()
      self.role = role
      self.classes = classes
