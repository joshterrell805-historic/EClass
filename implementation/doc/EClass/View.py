"""
Package View defines all views and GUIs that correspond to the EClass model.
"""

import wx

class WhiteboardNav(wx.Panel):
   """
   WhiteboardNav defines the view for the whiteboard (where slides will be displayed) as well as the navigation controls for changing the current slide.
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar presentation: A reference to the current presentation.
   @ivar whiteboard: The HTML window which displays the current slide.
   @ivar slideTextBox: A text box which can be given a slide number to navigate to.
   """

   def __init__(self, parent):
      """
      Initialize the WhiteboardNav view.

      @param parent: The current instance of the main EClass view
      """

   def MoveToPreviousSlide(self, event):
      """
      Change the current slide to the previous slide.

      @param event: The event that called this method.
      """
      pass

   def MoveToNextSlide(self, event):
      """
      Change the current slide to the next slide.

      @param event: The event that called this method.
      """
      pass

   def SyncWithPresenter(self, event):
      """
      Change the student's current slide to the presenter's current slide.

      @param event: The event that called this method.
      """
      pass

   def MoveToSlide(self, event):
      """
      Change the current slide to the specified slide (via the slide TextBox).

      @param event: The event that called this method.
      """
      pass
