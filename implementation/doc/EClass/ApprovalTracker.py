"""
Package ApprovalTracker is a collection of classes which make up a rating system
for students to rate a presentation live.

@author: Josh Terrell
"""

class ApprovalRating:
   """
   ApprovalRating is a value which represents the approval of the presentation at
   this very instant.

   If an ApprovalRating is owned by a Student, it represents that student's
   rating.

   If an ApprovalRating is owned by a Presenter, it represents the class average.

   @author: Josh Terrell

   @ivar listeners: (private) a collection of functions to be called when this
   model has been updated
   """

   def __init__(self):
      """
      Initialize an Approval Rating.
      """
      pass

   def SetValue(self, percent):
      """
      Set the the value of this approval rating to a percentage between [0, 1].

      @param percent: the percentage to set this rating to
      """
      pass

   def GetValue(self):
      """
      Get the percentage value of this approval rating (value between [0, 1]).

      @return: the value this approval rating represents
      """
      pass

   def AddListener(self, listener):
      """
      Add a listener to be called whenever the value of this approval rating
      changes.

      @param listener: the function to be added (called with no arguments)
      """
      pass
