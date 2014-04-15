"""
Package View defines all views and GUIs that correspond to the EClass model.
"""

__all__ = ["WhiteboardNav", "PermissionsWindow", "ImportPresentation", "InitialPrompt", "LoginWindow", "Roster", "Forum", "RosterItem"]

import wx

class WhiteboardNav(wx.Panel):
   """
   WhiteboardNav defines the view for the whiteboard (where slides will be displayed) as well as the navigation controls for changing the current slide.
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar presentation: A reference to the current presentation
   @ivar whiteboard: The HTML window which displays the current slide
   @ivar slideTextBox: A text box which can be given a slide number to navigate to
   """

   def __init__(self, parent):
      """
      Initialize the WhiteboardNav view.

      @param parent: The current instance of the main EClass view
      """

   def MoveToPreviousSlide(self, event):
      """
      Change the current slide to the previous slide.

      @param event: The event that called this method
      """
      pass

   def MoveToNextSlide(self, event):
      """
      Change the current slide to the next slide.

      @param event: The event that called this method
      """
      pass

   def SyncWithPresenter(self, event):
      """
      Change the student's current slide to the presenter's current slide.

      @param event: The event that called this method
      """
      pass

   def MoveToSlide(self, event):
      """
      Change the current slide to the specified slide (via the slide TextBox).

      @param event: The event that called this method
      """
      pass


class PermissionsWindow(wx.Frame):
   """
   PermissionsWindow defines the window used to display and access a student's permissions.
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar student: A reference to the student whose permissions are being accessed
   @ivar radioUnrestricted: A radio button for the Unrestricted permission level
   @ivar radioNormal: A radio button for the Normal permission level
   @ivar radioLockdown: A radio button for the Lockdown permission level
   @ivar checkRaiseHand: A checkbox for the "Raise a hand" permission
   @ivar checkPushLayer: A checkbox for the "Push a layer" permission
   """
   
   def __init__(self, student):
      """
      Initialize the WhiteboardNav view.

      @param student: The student whose permissions are being accessed
      """
      pass

   def OnAccept(self, event):
      """
      Update the student's permissions based on the current state of the radio buttons and checkboxes.
      Close the window.

      @param event: The event that called this method
      """
      pass
      
   def OnCancel(self, event):
      """
      Close the window without making changes to the student's permissions.

      @param event: The event that called this method
      """
      pass

class ImportPresentation(wx.Frame):
   """
   A ImportPresentation is a window that allows the importing of an already made HTMLpresentation document

   @author: Kevin Le (kle17@calpoly.edu)

   @ivar parent: The EClassWindow parent which needs the path of the HTML document
   @ivar presentationList: The directory structure which displays folders and files in the window.
   """

   def __init__(self, parent):
      """
      Creates a ImportPresentation window to select which HTMLpresentation to open.
      
      @param parent: the parant EClassWindow which import presentation needs to talk to.
      """
      pass

   def SelectPresentation(self, event):
      """
      Selects the highlighted presentation file and passes the path to EClassWindow.
      Other items such as the Whiteboard, LayerManager, Forum, and ApprovalTracker are also instantiated.
   
      @param event: The mouseclick event which calls this function.
      @postcondition: self.parant.whiteboard != None && self.parant.layerManager != None
      """
      pass

   def CancelSelectPresentation(self, event):
      """
      Cancels ImportPresentation prompt and returns to the main screen.

      @param event: The mouseclick event which calls this function.
      @postcondition: self.Show() == False
      """
      pass

   def GetPresentationPath(self):
      """
      Returns a string of the selected file path.

      @return: The string of the selected file path.
      """
      pass

class InitialPrompt(wx.Panel):
   """
   InitialPrompt represents the panel that the user first sees to either create or open a new presentation.

   @author: Kevin Le (kle17@calpoly.edu)
   
   @ivar parant: The parant EClassWindow which talks to the panel.
   """

   def __init__(self, parant):
      """
      Puts the panal on to the parant EClassWindow.

      @param parant: The parant EClassWindow to set self.parant to.
      @precondition: parant != None
      """
      pass

   def CreatePresentation(self, event):
      """
      Function whichs chooses to bring up the create a presentation prompt.
      InitialPrompt is hidden if called.

      @param event: Mouseclick event which calls this function.
      @postcondition: self.Shown() == False
      """
      pass

   def UsePresentation(self, event):
      """
      Function which chooses to bring up the open a presentation prompt.
      Initial prompt is hidden if called.

      @param event: Mouseclick event which calls this function.
      @postcondition: self.Shown() == False && self.parant.importPresentation.Shown == True
      """
      pass

class LoginWindow(wx.Frame):
   """
   LoginWindow is the window that is shown when the application is first launched.
   The user is prompted for a username and password. If the username and password are
   valid, the user can then launch the main EClassWindow.

   @author: Kevin Le (kle17@calpoly.edu)
   """

   def __init__(self):
      """
      Initialized all buttons on the window and the appropriate sizers. Textboxes are also
      made for the user to enter their credentials.
      """
      pass

   def GetUsername(self):
      """
      This function returns the text entered into the username textbox.

      @return: The username string.
      """
      pass

   def GetPassword(self):
      """
      This function returns the text entered into the password textbox.
      
      @return: The password string.
      """
      pass

   def OnAttempt(self, event):
      """
      Attempts to log the user into the EClass using the credentials.

      @postcondition: User is either logged in or not
      """
      pass

   def OnSuccess(self):
      """
      The user has successfully logged in and the EClassWindow is to be launched.
      
      @precondition: User successfully logged in
      @postcondition: EClassWindow != None
      """
      pass

   def OnCancel(self, event):
      """
      The entire program exits if cancel is clicked.
      """
      pass

class Roster(wx.Frame):
   """
   Roster is the window that is shown when the user presses the 'Show Roster' menu
   item from the 'View' menu. The roster is populated with the student's names in
   the class.

   @author: Carson Carroll (ccarro03@calpoly.edu)
   """

   def __init__(self):
      """
      Initializes all buttons on the window and the appropriate sizers. RosterItem's
      populate the appropriate panel to display the students in the roster.
      """
      pass

   def AddStudent(self, event):
      """
      Adds a student to the roster.
      """
      pass

   def Remove(self, event):
      """
      Removes a student from the roster.
      """
      pass

class Forum(wx.Frame):
   """
   Forum is the window that is shown when the user presses the 'Show Forum' menu
   item from the 'View' menu. The forum contains messages that users have sent 
   to each other as well as a field for user to enter text for a new message.

   @author: Carson Carroll (ccarro03@calpoly.edu)
   """

   def __init__(self):
      """
      Initializes all buttons on the window and the appropriate sizers. Two TextCtrl's
      are initialized with one being READONLY and one supporting MULTILINE input.
      """
      pass

   def SendMessage(self, event):
      """
      Appends the newly created message to the end of the messages list which is then
      displayed in the READONLY TextCtrl.
      """
      pass

   def CloseForum(self, event):
      """
      Closes the forum window.
      """
      pass

   def Refresh(self):
      """
      Refreshes the messages list.
      """
      pass

class RosterItem(wx.Panel):
   """
   RosterItem is the panel that displays a student's first and last name along with three
   buttons for question asking, pushing layers, and student permissions.  A RosterItem is what
   populates the roster.

   @author: Carson Carroll (ccarro03@calpoly.edu)
   """

   def __init__(self, parent):
      """
      Initializes all buttons on the panel and the appropriate sizers. The first name and last
      name are set as well.
      """
      pass

   def HandButton(self, event):
      """
      Shows whether a student has a question or not.
      """
      pass

   def LayersButton(self, event):
      """
      Shows whether a student has pushed a layer or not.
      """
      pass

   def OpenPermissions(self, event):
      """
      Opens the StudentPermissions window where the student's permissions can be set.
      """
      pass