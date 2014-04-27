class Presentation:
   """
   Make a series of tests that checks for individual errors in each method
   and for errors caused by sequential method calls (for the ones that operate
   on the same values)
   Testing order: 
      __init__() 
      > SetPath() 
      > Slidify() 
      > GetSlideNum(), GetSlide()
      > MoveToNextSlide(), MoveToPreviousSlide(), MoveToSlide() 
      > SyncWithPresenter()
   """

   def __init__(self, path):
      """
      Test that all ivars are set to the expected values.
      """
      pass

   def MoveToNextSlide(self):
      """
      Test outcome when slide index is 0.
      Test outcome when current slide is the last slide.
      Test outcome when slide index is somewhere in the middle of the allowed indices.
      Test the return value for the above situations.
      """
      pass

   def MoveToPreviousSlide(self):
      """
      Test outcome when slide index is 0.
      Test outcome when current slide is the last slide.
      Test outcome when slide index is somewhere in the middle of the allowed indices.
      Test the return value for the above situations.
      """
      pass

   def MoveToSlide(self, slideNum):
      """
      Test outcome when the given slideNum is < 1.
      Test outcome when the given slideNum is > the current number of slides.
      Test outcome when the given slideNum is somewhere in the middle of the allowed indices.
      Test that the final slide index is always one less than the given slideNum.
      Test the return value for the above situations.
      """
      pass

   def SyncWithPresenter(self):
      """
      Test outcome when the current slide is the same as the Presenter's current slide.
      Test outcome when the current slide is not the same as the Presenter's current slide.
      Test outcome when the Student's permission level is Lockdown.
      Test outcome when the Student's permission level is Normal.
      Test outcome when the Student's permission level is Unrestricted.
      """
      pass

   def SetPath(self, path):
      """
      Test when path is a valid path.
      Test when path is None or an empty string.
      """
      pass

   def GetSlideNum(self):
      """
      Test that the current slide index + 1 is returned for a full range of slide numbers.
      """
      pass

   def GetSlide(self):
      """
      Test that a Slide object is returned.
      Test that the returned Slide is the currently displayed Slide.
      """
      pass
      
   def Slidify(self):
      """
      Test when the path is invalid, empty, or None (null).
      Test when the path is for a file with no slide breaks.
      Test when the path is for a file with multiple slide breaks.
      Test when the HTML file has malformed slide breaks.
      Test when the HTML file contains no <body> tag.
      Test that, on success, there is always at least one slide.
      """
      pass
