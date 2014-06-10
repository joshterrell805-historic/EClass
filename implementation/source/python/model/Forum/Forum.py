import wx
from Message import Message
from datetime import datetime
import EClass

class Forum:
   def __init__(self):
      self.messagesList = []
      self.view = None

      # infinite recurion without this CallLater
      # EClass.GetInstance() -> Forum() ->EClass.GetInstance() ...
      # just wait a sec, then get the instance. Does anyone have a better
      # solution?
      def listen():
         EClass.EClass.GetInstance().connection.registerMessageListener(
            'new message', self.onMessage
         )
         EClass.EClass.GetInstance().registerOnSaveListener(
            'forum', self.onSaveListener
         )
      wx.CallLater(1, listen)

   # Add message gets called by the view only when a new message is
   # created in a text control
   def AddMessage(self, message):
      message = Message(EClass.EClass.GetInstance().user.username, datetime.now(), message)
      if EClass.EClass.GetInstance().user.isPresenter():
         # if the user who typed the message is a presenter, broadcast his
         # message to all students and add his message to his forum view.
         EClass.EClass.GetInstance().connection.send('new message', message)
         self.messagesList.append(message)
         self.view and self.view.Refresh()
      else:
         # if the user who typed the message is a student, don't add the message
         # to the forum yet.. send the message to the presenter who will then
         # broadcast the message back to everyone.
         EClass.EClass.GetInstance().connection.send('new message', message)

   def onMessage(self, message, student):
      print('message received', message, student)
      if EClass.EClass.GetInstance().user.isPresenter():
         # if the presenter is receiving a message the message sender should
         # never be the presenter (send the message to himself). the message
         # sender should always be a student.
         assert(student != False)
         # don't trust what the student set as the 'name' and 'time' fields..
         message = Message(student, datetime.now(), message.text)
         # broadcast the message out to all students and add the message
         # to the presenter's view
         self.messagesList.append(message)
         self.view and self.view.Refresh()
         EClass.EClass.GetInstance().connection.send('new message', message)
      else:
         # If a student is receiving a message, the message sender should always
         # be the presenter (student messages are forwarded through the presenter)
         # student is the username of the student who sent the message,
         # or false if the presenter sent the message
         assert(student == False)
         # the message is good to go, we trust the data that the presenter sent
         # us
         self.messagesList.append(message)
         self.view and self.view.Refresh()

   def onSaveListener(self, eventType, identifier):
      assert identifier == 'forum'
      if eventType == 'save initial data for student':
         messages = map(Message.toDict, self.messagesList)
         return {'messages': messages}

   def loadInitialData(self, data):
      assert len(self.messagesList) == 0, \
      "there's a message in the forum before initial data was received"

      # data =  same object returned from onSaveListener
      messages = map(Message.fromDict, data['messages'])
      self.messagesList.extend(messages)
      self.view and self.view.Refresh()
