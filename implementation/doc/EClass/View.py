"""
Package View defines all views and GUIs that correspond to the EClass model.
"""

import wx

class WhiteboardNav(wx.Panel):
   """
   WhiteboardNav defines the view for the whiteboard (where slides are displayed) as well as the navigation controls for changing the current slide.
   Due to the way wxPython handles events, this class also contains much of the drawing tools functionality.
   
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu), Kevin Le (kle17@calpoly.edu)

   @ivar presentation: A reference to the current presentation
   @ivar whiteboard: The HTML window which displays the current slide
   @ivar slideTextBox: A text box which can be given a slide number to navigate to
   @ivar currSlideText: A static text display for the current slide number
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

   def RefreshSlide(self):
      """
      Refresh the whiteboard to display the presentation's current slide.
      Also refresh the slide number displayed below the whiteboard.
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
      Initialize the PermissionsWindow view.

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

class KickWindow(wx.Frame):
   """
   KickWindow defines the window used to confirm whether or not a student will be kicked.
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar student: A reference to the student who may be kicked
   """
   
   def __init__(self, student):
      """
      Initialize the KickWindow view.

      @param student: The student to be kicked
      """
      pass
      
   def OnAccept(self, event):
      """
      Update the student's 'kicked' and 'present' statuses.
      Notify the roster that the student's display in the list should be changed.
      Close the window.

      @param event: The event that called this method
      """
      pass
      
   def OnCancel(self, event):
      """
      Close the window without making changes to the student's 'kicked' or 'present' statuses.

      @param event: The event that called this method
      """
      pass
      
class ImportPresentation(wx.Frame):
   """
   A ImportPresentation is a window that allows the importing of an already made HTMLpresentation document

   @author: Kevin Le (kle17@calpoly.edu), Joel Wilcox (jnwilcox@calpoly.edu)

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

class RosterWindow(wx.Frame):
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

   def Redraw(self, event):
      """
      Updates the two lists of students to show which students are present and which ones are absent
      as students login and logout.
      """
      pass

   def OnClose(self, event):
      """
      Hides the roster window and unchecks the "Show Roster" menu item in the "View" menu.
      """
      pass

   def ShowStudentPanel(self, event):
      """
      Shows the student panel that is associated with the selected student that is present.
      """
      pass

class ForumWindow(wx.Frame):
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

   def onClose(self, event):
      """
      Hides the forum window and unchecks the "Show Forum" menu item in the "View" menu.
      """
      pass

class RosterItemPanel(wx.Panel):
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
      
   def OpenKickWindow(self, event):
      """
      Opens the 'Kick Confirmation' window where the presenter confirms or cancels kicking
      a student.
      """
      pass

class RosterStaticPanel(wx.Panel):
   """
   The static panel is the panel that is the parent panel to each RosterItemPanel that displays when a student is
   selected.

   @author: Carson Carroll (ccarro03@calpoly.edu)
   """

   def __init__(self, parent):
      """
      Initializes the panel's sizer as well as its initial background color.
      """
      pass

class LayerManager:
   """
   Renders the view of the LayerManagerModel

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar parent: A reference to the parent class
   """
   def __init__(self, parent):
      """
      Initialize a LayerManager view.
      
      @param parent: A reference to the EClass window.
      """
      pass

   def DeleteLayer(self, event):
      """
      Sends a delete action to the LayerManagerModel

      @param event: the user action that promted this callback.
      
      @postcondition: len(EClass.GetInstance().layerManagerModel.layers) 
                      == old(len(EClass.GetInstance().layerManagerModel.layers)) - 1
      """
      pass

   def NewLayer(self, event):
      """
      Show the NewLayerView

      @param event: the user action that promted this callback.

      @postcondition: self.layers.count() == old(self.layers.count()) + 1
      """
      pass

   def ChangeOpacity(self, event):
      """
      Sends a changeOpactiy call to a layer in the layer manager

      @param event: the user action that promted this callback.

      @postcondition: self.layers[index].opacity != old(self.layers[index].opacity)
      """
      pass
      
   def UpdateLayers(self):
      """
      Update the layers present in the LayerManager. 
      Gets layers of current slide and displays them.
      """
      pass
      
   def onClose(self, event):
      """
      Uncheck the menu item, and close the LayerManagerPanel

      @postcondition: self.parent.showLayerManagerMenuItem != old(self.parent.showLayerManagerMenuItem)
      """
      pass
      
class LayerView:
   """
   Renders a Layer inside the LayerManager.

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar parent: A reference to the parent class
   @ivar index: Position in Layer manager
   @ivar layer: The layer this class is displaying
   """
   def LayerListObject(self, parent, index, checked):
      """
      Gets the layer represented as a sizer.

      @param parent: A reference to the EClass window.
      @param index: Index in the layer manager.
      @param checked: Whether the layer is Selected
      
      @precondition: index > -1 && index < len(self.parent.layers)
      
      @postcondition: self.index == index
      """
      pass

   def __init__(self, parent, layer):
      """
      Initialize a NewLayerWindow view.

      @param parent: A reference to the LayerManager window.
      @param layer: the layer we are displaying.
      """
      pass
      
   def ChangePermissions(self, event):
      """
      Bring the ChangePermWindow up.

      @param event: the user action that promted this callback.

      @postcondition: self.permissions != old(self.permissions)
      """
      pass
      
   def ToggleVisible(self, event):
      """
      Sets the visibility of the layer

      @param event: the user action that promted this callback.

      @postcondition: self.visible != old(self.visible)
      """
      pass

   def ToggleLock(self, event):
      """
      Locks and unlocks the layer

      @param event: the user action that promted this callback.

      @postcondition: self.locked != old(self.locked)
      """
      pass
      
class NewLayerWindow:
   """
   Renders the dialog for a New Layer.

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar parent: A reference to the parent class
   @ivar layer: A reference to the new layer
   @ivar newName: A reference to the new name box
   @ivar slider: A reference to the slider
   """
   
   def __init__(self, parent):
      """
      Initialize a NewLayerWindow view.
      
      @param parent: A reference to the EClass window.
      """
      pass
      
   def MakeNewLayer(self, event):
      """
      Attached to the Ok button. Gets data from form, sends it to the LayerManagerModel

      @param event: the user action that promted this callback.
      
      @postcondition: len(EClass.GetInstance().layerManagerModel.layers) 
                      == old(len(EClass.GetInstance().layerManagerModel.layers)) + 1
      """
      pass
      
   def ChangePermissions(self, event):
      """
      Bring the ChangePermWindow up.

      @param event: the user action that promted this callback.
      """
      pass
      
class ChangePermWindow(wx.Frame):
   """
   Shows the Dialog to change the permissions on a layer.

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar parent: A reference to the parent class
   @ivar layer: A reference to the layer we are changing
   @ivar listBox1: Selection for permissions
   """
   def __init__(self, parent, layer):
      """
      Initialize a ChangePermWindow view.
      
      @param parent: A reference to the parent class
      @param layer: A reference to the layer we are changing
      """

   def ChangeLayerPerm(self, event):
      """
      Sets the permissions on a layer, then closes the Change Permissions dialog.
      
      @param event: the user action that promted this callback.
      """

class EClassWindow:
   """
   EClassWindow is the main window for the EClass program. It contains the
   menubar,the whiteboard, and the navigation panel.

   @author: Josh Terrell jmterrel@calpoly.edu
   """

class MenuBar:
   """
   MenuBar is a collection of all menu operations including 
   file operations and view operations that hide/show various windows.

   @ivar IDs: List holding all the IDs for each Menu and Menu Item
   @ivar fileMenu: Sub-menu for all file operations
   @ivar viewMenu: Sub-menu for all view operations
   @ivar openMenuItem: Menu item to open a presentation
   @ivar saveMenuItem: Menu item to save a presentation
   @ivar quitMenuItem: Menu item to quit the EClass program
   @ivar showRosterMenuItem: Menu item to show the Roster
   @ivar showDrawingToolsMenuItem: Menu item to show the Drawing Tools
   @ivar showLayerManagerMenuItem: Menu item to show the Layer Manager
   @ivar showApprovalTrackerMenuItem: Menu item to show the Approval Tracker
   @ivar showForumMenuItem: Menu item to show the Forum
   @ivar showAskQuestionMenuItem: Menu item to show the Ask Question window
   @ivar fullScreenMenuItem: Menu item to toggle full screen on the EClass program

   @author: Mike Sevilla (mjsevill@calpoly.edu)
   """

   def InitLocalVars(self, event):
      """
      Creates and returns a list of all IDs for each menu and menu item.

      On success, the function returns a list of all IDs

      On failure, the function does not return a list of all IDs

      @param event: Event that calls this method.
      """
      pass

   def OpenPresentation(self, event):
      """
      Opens the window allowing the user to open a pre-made presentation into
      the EClass program.

      On success, the EClass program opens the .html file.

      On failure, the EClass program does not open the selected .html file.

      @param event: Event that calls this method
      """
      pass

   def SavePresentation(self, event):
      """
      Opens the window allowing the user to save the current presentation as either a
      new presentation or overwrite the existing presentation.

      On success, the EClass program saves the .creampie file.

      On failure, the EClass program does not save the selected .creampie file.

      @param event: Event that calls this method
      """
      pass

   def ToggleRoster(self, event):
      """
      Shows/Hides the roster.

      @param event: Event that calls this method.

      @postcondition: rosterWindow.Toggle() == !rosterWindow.Toggle()
      """
      pass

   def ToggleDrawingTools(self, event):
      """
      Shows/Hides the drawing tools.

      @param event: Event that calls this method.

      @postcondition: drawingTools.Toggle() == !drawingTools.Toggle()
      """
      pass

   def ToggleLayerManager(self, event):
      """
      Shows/Hides the layer manager.
      
      @param event: Event that calls this method.

      @postcondition: layerManager.Toggle() == !layerManager.Toggle()
      """
      pass

   def ToggleApprovalTracker(self, event):
      """
      Shows/Hides the approval tracker.

      @param event: Event that calls this method.

      @postcondition: approvalTracker.Toggle() == !approvalTracker.Toggle()
      """
      pass

   def ToggleForum(self, event):
      """
      Shows/Hides the forum.

      @param event: Event that calls this method.

      @postcondition: forum.Toggle() == !forum.Toggle()
      """
      pass

   def ToggleAskQuestion(self, event):
      """
      Shows/Hides the Ask Question window.

      @param event: Event that calls this method.

      @postcondition: askQuestion.Toggle() == !askQuestion.Toggle()
      """
      pass

   def ToggleFullScreen(self, event):
      """
      Sets the EClass window to full screen or original size.

      @param event: Event that calls this method.

      @postcondition: parent.IsFullScreen() = !parent.IsFullScreen()
      """
      pass

   def Quit(self, event):
      """
      Quits the EClass program.

      On success, the EClass program quits.

      On failure, the EClass program is still running.

      @param event: Event that calls this method.
      """
      pass
