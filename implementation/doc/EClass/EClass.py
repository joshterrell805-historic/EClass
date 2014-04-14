"""
Package EClass defines objects and operations related to the core application of
model of the EClass.
"""

class EClass:
   """
   EClass is a singleton model which has a reference to other important models.
   
   @author: Kevin Le (kle17@calpoly.edu)

   @ivar presentation: Refers to the current presentation open in the EClass.
   @ivar layerManagerModel: Refers to the layerManagerModel for the current presentation.
   @ivar user: Refers to the current user profile using EClass.
   """

   def GetInstance():
      """
      Initialize an EClass. Since EClass is a singleton, GetInstance ensures only one instance will ever exist.
      """
      pass

   def __init__(self):
      """
      Initializes a presentation and user object for the model.
      """
      pass

   def Login(self, username, password):
      """
      Logs the user into the EClass application.

      @param username: The username of the user. Most likely a Cal Poly username.
      @param password: The password of the user.
      """
      pass

   def Authorize(self, username, password):
      """
      Checks if the username and password combination is valid.
   
      @param username: The username of the user. Most likely a Cal Poly username.
      @param password: The password of the user.
      @return: True or false depending if the username/pass is valid.
      """










      
