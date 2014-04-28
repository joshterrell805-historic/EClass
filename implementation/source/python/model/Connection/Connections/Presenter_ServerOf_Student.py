from __init__ import BaseConnection
from twisted.internet import reactor

# a connection to a student
class Presenter_ServerOf_Student(BaseConnection):
   def __init__(self):
      pass

   def onClose(self, reason):
      pass

   def onMessage(self, message):
      pass
