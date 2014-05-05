from Message import Message

class Forum:
   def __init__(self):
      self.messagesList = []

   def AddMessage(self, name, time, message):
      message = Message(name, time, message)
      self.messagesList.append(message)

   def Refresh(self):
      print('From Forum.Refresh()')