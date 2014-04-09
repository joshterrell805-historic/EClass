"""
The Credentials module
"""

class Credentials:
   """
   Credentials is a username and password associated with a user which can be
   validated.
   """

   def __init__(self, username, password):
      """
      Create a new username-password pair.

      @type username string
      @param username the user's username

      @type password string
      @param password the user's password
      """

      self.username = username
      self.password = password

   def login(self):
      """
      Attempt to login the user.

      @rtype boolean
      @return true if the credentials are valid, otherwise false
      """

      return True
