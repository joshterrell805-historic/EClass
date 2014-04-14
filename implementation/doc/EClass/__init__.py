"""
EClass is a presentation tool which allows students to interactively follow
a presentation by taking notes on the presentation itself, ask the presenter
questions, rate how well they understand the presentation at any given moment,
and converse in a forum with other students.

@author: Josh Terrell jmterrel@calpoly.edu
"""

__all__ = ["Person", "Presentation"]

class EClass():
   """
   EClass is a colleciton of all the highest level models in the EClass program
   including (but not limited to) the presentation, layer manager, and logged in
   user.

   @ivar presentation: the Presentation model
   @ivar user: the logged in user (None for no logged in user)
   @ivar layerManagerModel: the model for the Layer Manager

   @author: Josh Terrell jmterrel@calpoly.edu, Kevin Le kle17@calpoly.edu
   """

   def __init__(self):
      """
      Private! see EClass.GetInstance()
      """
      pass

   @staticmethod
   def GetInstance():
      """
      Get an instance of this singleton which holds a reference to important
      top-level models.

      @return: the EClass instance

      @postcondition: isinstance(@return, EClass)
      """
      pass

   def Login(self, username, password):
      """
      Attempt to login the user.

      On success, self.user is set to a Presenter or Student depending on the
      credentials of the user.

      On failure, self.user remains None.

      @param username: the username of the user 
      @param password: the password of the user

      @precondition: self.user == None
      """
      pass

   def Authorize(self, username, password):
      """
      Try to authorize the user using the username/password combination.

      @param username: the username of the user 
      @param password: the password of the user
      @return: True or false depending if possible to authorize.
      """

   def SetUpLayerManager(self):
      """
      Initialize the Layer Manager's model.

      @postcondition: isinstance(self.layerManagerModel, LayerManagerModel)
      """
      pass
