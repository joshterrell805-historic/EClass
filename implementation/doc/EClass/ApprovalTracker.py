"""
Package ApprovalTracker is a collection of classes which make up a rating system
for students to rate a presentation live.

@author: Josh Terrell jmterrel@calpoly.edu
"""

class ApprovalRating:
   """
   ApprovalRating is a value which represents the approval of the presentation at
   this very instant.

   If an ApprovalRating is owned by a Student, it represents that student's
   rating.

   If an ApprovalRating is owned by a Presenter, it represents the class average.

   @author: Josh Terrell jmterrel@calpoly.edu

   @ivar __listeners: a collection of functions to be called when this
   @ivar __rating: the percentage value between [0, 1] this rating represents
   """

   def __init__(self):
      """
      Initialize an Approval Rating.
      """
      pass

   def SetValue(self, percent):
      """
      Set the the value of this approval rating to a percentage between [0, 1].

      A side effect of calling this method is that all listeners added via
      AddListener are notified that the value has changed.

      @param percent: the percentage to set this rating to

      @postcondition: self.__rating == percent
      """
      pass

   def GetValue(self):
      """
      Get the percentage value of this approval rating (value between [0, 1]).

      @return: the value this approval rating represents

      @postcondition: @return == self.__rating &&
      old(self.__rating) == self.__rating
      """
      pass

   def AddListener(self, listener):
      """
      Add a listener to be called whenever the value of this approval rating
      changes.

      @param listener: the function to be added (called with no arguments)

      @postcondition: self.__listeners.contains(listener) &&
      len(self.__listeners) == len(old(self.__listeners) + 1)
      """
      pass
