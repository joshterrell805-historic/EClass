import sys
sys.path.insert(0, '../../source/python/model/enum')

# TODO: figure out why it's not recognizing enum then add it as base class for PermissionLevel
#from enum import Enum

"""
Module Presentation defines objects and operations related to the presentation's content.

There are objects for both the presentation slides and the underlying markup (PresentationHTML). Additionally, this package includes much of the layer functionality. This can be seen in the Layer and LayerPermission objects.
"""

class Presentation:
   """
   A Presentation is a collection of slides and their respective layers which is displayed at the center of the EClass.

   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar currentSlide: Refers to the current slide being displayed.
   @ivar slides: Contains each of the slides in a presentation.
   """

   def __init__(self, path):
      """
      Initialize a Presentation.

      @param path: The path to the presentation file.
      """
      pass

   def MoveToNextSlide(self):
      """
      Set the current slide to the next consecutive slide.

      @precondition: self.slides.index(self.currentSlide) != len(self.slides) - 1

      @postcondition: self.slides.index(self.currentSlide) == self.slides.index(old(self.currentSlide)) + 1
      """
      print('From Presentation.MoveToNextSlide()')

   def MoveToPreviousSlide(self):
      """
      Set the current slide to the previous slide.

      @precondition: self.slides.index(self.currentSlide) != 0

      @postcondition: self.slides.index(self.currentSlide) == self.slides.index(old(self.currentSlide)) - 1
      """
      print('From Presentation.MoveToPreviousSlide()')

   def MoveToSlide(self, slideNum):
      """
      Set the current slide to the slide at a given index.

      @param slideNum: The index of the new slide to display.

      @precondition: slideNum >= 0 && slideNum < len(self.slides)

      @postcondition: self.slides.index(self.currentSlide) == slideNum
      """
      print('From Presentation.MoveToSlide()')

   def SyncWithPresenter(self):
      """
      Set the current slide to the slide being viewed by the presenter.

      @postcondition: self.slides.index(self.currentSlide) != self.slides.index(old(self.currentSlide))
      """
      print('From Presentation.SyncWithPresenter')


class PermissionLevel():
   """
   A PermissionLevel is an Enum of the three presentation permission levels used for students.

   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar Unrestricted: The student may draw on his own layers and push layers to the public stack freely.
   @ivar Normal: The student may draw on his own layers, and may ask to add his layer to the presenter's layer stack by "push"ing that layer.
   @ivar Lockdown: The student may not draw on his own layers on his own machine and he may not push a layer.
   """
