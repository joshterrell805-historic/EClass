from Message import Message

class Forum:
   def __init__(self):
      self.messagesStack = []

   def AddMessage(self, name, time, message):
      message = Message(name, time, message)
      self.messagesStack.append(message)

   def Refresh(self):
      print('From Forum.Refresh()')