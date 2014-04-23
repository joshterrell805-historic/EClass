"""
Package Forum defines objects and operations related to the Forum.

There are objects for both a forum and a message.
"""

class Forum:
   """
   A Forum contains all of the messages from user to user and methods to manage the forum.

   @author: Carson Carroll (ccarro03@calpoly.edu)

   @ivar messagesStack: A list that is represented like a stack that holds all of the forum's messages.
   """

   def __init__(self):
      """
      Build an instance of the forum.

      @param self: self is the instance of this object.
      """
      pass

   def AddMessage(self, name, time, message):
      """
      Puts a new Message into the list of current messages.

      @param name: The username of the user that is to be displayed along with the text of the message.
      @param time: The current date and time of when the message was sent.
      @param message: The message that is to be added to the end of the list of messages.

      @precondition: self.messages != None and message != None and !message.text.IsEmpty()

      @postcondition: messages.size() == old(messages.size()) + 1
      """
      pass

   def Refresh(self):
      """
      Refreshes the list of messages to the most up to date version.
      """
      pass

class Message:
   """
   A Message contains all of the information for a message including the user's name, the datetime that a message was sent, and the text of the message.

   @author: Carson Carroll (ccarro03@calpoly.edu)

   @ivar name: The username of the user.
   @ivar time: The datetime of when the message was sent.
   @ivar text: The text of the message.
   """

   def __init__(self, name, time, text):
      """
      Builds an instance of a Message.

      @param self: self is the instance of this object.
      @param name: The username of the user.
      @param time: The datetime of when the message was sent.
      @param text: The text of the message.
      """
      pass

   def ToString(self):
      """
      Takes the contents of the message: name, datetime, text and formats them all together into a string.

      @precondition: self.text != None

      @postcondition: return self.name + " " + "[" + self.time + "]" + ": " + self.text
      """
      pass