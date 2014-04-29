"""
EClass is a presentation tool which allows students to interactively follow
a presentation by taking notes on the presentation itself, ask the presenter
questions, rate how well they understand the presentation at any given moment,
and converse in a forum with other students.

There are three types of applications that interact in EClass: EClass
(presenter logged in), EClass (student logged in), and the central server.
Documentation about how these applications interact behind the scenes is
described in the U{networking documentation <THIS_WILL_BE_REMOVED_TO_CREATE_A_RELATIVE_LINK../documentation/design/networking.html>}. Also, see EClass.Connection below to see
the model of the EClass side of the connection.

@author: Josh Terrell jmterrel@calpoly.edu
"""

__all__ = ["Person", "Presentation", "Connection"]

class EClass():
   """
   EClass is a collection of all the highest level models in the EClass program
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

   def Login(self, username, password, onSuccess, onFailure):
      """
      Attempt to login the user.

      If the login succeeds, self.user is set to an instance of Presenter or
      Student depending on the credentials of the user, and the onSuccess
      callback is called.

      If the login fails, self.user remains None and onFailure is called.

      @param username: the username of the user 
      @param password: the password of the user
      @param onSuccess: the callback to be called if the authorizaiton request
      succeeds (passed 0 arguments)
      @param onFailure: the callback called if the authorization request fails
      passed one argument, a string stating the reason that the requst failed.

      @precondition: self.user == None
      """
      pass

   def SetUpLayerManager(self):
      """
      Initialize the Layer Manager's model.

      @postcondition: isinstance(self.layerManagerModel, LayerManagerModel)
      """
      pass

   def exit(self):
      """
      Close the EClass model cleaning up any resources that need to be cleaned
      (mainly networking connections). 

      NOTE: this may pre-maturely close the program with a SIGKILL if twisted
      can't be shut down. This is a issue we're working on, but for now all
      other cleanup should be called before calling this method.
      """
      pass
