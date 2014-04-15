"""
Package Forum defines objects and operations related to the Forum.

There are objects for both a forum and a message.
"""

class ForumModel:
   """
   A Forum contains all of the messages from user to user and methods to manage the forum.

   @author: Carson Carroll (ccarro03@calpoly.edu)

   @ivar messages: The list of messages in the forum.
   """

   def __init__(self, messages):
      """
      Build an instance of the forum.

      @param self: self is the instance of this object.
      @param messages: A list of messages in the forum.
      """
      pass

   def SendMessage(self, message):
      """
      Puts a new Message into the list of current messages.

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
