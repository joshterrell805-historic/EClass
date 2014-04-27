from datetime import datetime

class Question(object):

   def __init__(self, questionText, timeCreated = datetime.now().time()):
      self.text = questionText
      self.timeCreated = timeCreated

   def GetText(self):
      return self.text
      
   def GetTime(self):
      return self.timeCreated