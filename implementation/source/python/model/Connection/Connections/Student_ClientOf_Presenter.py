from __init__ import BaseConnection

# a connection from a student to a presenter
class Student_ClientOf_Presenter(BaseConnection):
   def __init__(self):
      pass

   def onClose(self, reason):
      pass

   def onMessage(self, message):
      pass

   def tryJoin(self, key, callback):
      # TODO next, try to join the presentation
      pass
