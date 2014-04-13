"""
Package Presentation defines objects and operations related to the presentation's content and navigation.

There are objects for both the presentation slides and the underlying markup (PresentationHTML). Additionally, this package includes much of the layer functionality. This can be seen in the Layer and LayerPermission objects.
"""

import sys
sys.path.insert(0, '../../source/python/model/enum')

# TODO: figure out why it's not recognizing enum then add it as base class for PermissionLevel
#from enum import Enum

class Presentation:
   """
   A Presentation is a collection of slides and their respective layers which is displayed at the center of the EClass.

   @author: Joel Wilcox (jnwilcox@calpoly.edu), Kevin Le (kle17@calpoly.edu)

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
      pass

   def MoveToPreviousSlide(self):
      """
      Set the current slide to the previous slide.

      @precondition: self.slides.index(self.currentSlide) != 0

      @postcondition: self.slides.index(self.currentSlide) == self.slides.index(old(self.currentSlide)) - 1
      """
      pass

   def MoveToSlide(self, slideNum):
      """
      Set the current slide to the slide at a given index.

      @param slideNum: The index of the new slide to display.

      @precondition: slideNum >= 0 && slideNum < len(self.slides)

      @postcondition: self.slides.index(self.currentSlide) == slideNum
      """
      pass

   def SyncWithPresenter(self):
      """
      Set the current slide to the slide being viewed by the presenter.

      @postcondition: self.slides.index(self.currentSlide) != self.slides.index(old(self.currentSlide))
      """
      pass


class PermissionLevel():
   """
   A PermissionLevel is an Enum of the three presentation permission levels used for students.

   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar Unrestricted: The student may draw on his own layers and push layers to the public stack freely.
   @ivar Normal: The student may draw on his own layers, and may ask to add his layer to the presenter's layer stack by "push"ing that layer.
   @ivar Lockdown: The student may not draw on his own layers on his own machine and he may not push a layer.
   """
   
class Layer:
   """
   A layer is a overlay on top of slides, which the user can draw or write on.

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar objects: A Collection of LayerObjects that represent all graphics on a Layer
   @ivar opacity: A double representing how transparent a Layer is
   @ivar visible: Boolean value representing if a Layer can or cannot be seen
   @ivar permissions: The LayerPermissions for a given Layer
   @ivar name: Name of the given Layer
   @ivar locked: Boolean determining whether the user can edit this layer.
   """
   def __init__(self, name, lock):
      """
      Initialize a Layer.

      @param name: The name of the new layer.
      @param Whether the layer is locked.
      """
      pass

   def ChangePermissions(self):
      """
      Set the selected layer's permissions.

      @postcondition: self.permissions != old(self.permissions)
      """
      pass
      
   def ToggleLock(self):
      """
      Set the lock state of a layer.

      @postcondition: self.locked != old(self.locked)
      """
      pass
      
   def ToggleVisible(self):
      """
      Set the visibility of a layer.

      @postcondition: self.visible != old(self.visible)
      """
      pass

class LayerManagerModel:
   """
   Manages the layers attached to the current slide

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar layers: A Collection of Layers that represent all graphics on a Slide
   """
   def __init__(self):
      """
      Initialize a LayerManagerModel.
      """
      pass

   def DeleteLayer(self):
      """
      Delete the selected slide

      @postcondition: self.layers.count() == old(self.layers.count()) - 1
      """
      pass

   def NewLayer(self):
      """
      Creates a New Layer for the current Slide

      @postcondition: self.layers.count() == old(self.layers.count()) + 1
      """
      pass
      
   def ChangeOpacity(self, index):
      """
      Changes opacity of selected layer

      @postcondition: self.layers[index].opacity != old(self.layers[index].opacity)
      """
      pass
