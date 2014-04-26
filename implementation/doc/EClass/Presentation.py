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

   @ivar currSlideNum: The index of the current slide.
   @ivar slides: Contains each of the slides in a presentation.
   @ivar path: Refers to the current file system path of the backing presentation file.
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

      @precondition: self.currSlideNum != len(self.slides) - 1

      @postcondition: self.currSlideNum == old(self.currSlideNum) + 1
      """
      pass

   def MoveToPreviousSlide(self):
      """
      Set the current slide to the previous slide.

      @precondition: self.currSlideNum != 0

      @postcondition: self.currSlideNum == old(self.currSlideNum) - 1
      """
      pass

   def MoveToSlide(self, slideNum):
      """
      Set the current slide to the slide at a given index.

      @param slideNum: The index (offset by 1) of the new slide to display.

      @precondition: slideNum >= 1 && slideNum <= len(self.slides)

      @postcondition: self.currSlideNum == slideNum - 1
      """
      pass

   def SyncWithPresenter(self):
      # TODO Update postcondition when we have a way to get an instance of the Presenter's EClass/presentation
      """
      Set the current slide to the slide being viewed by the presenter.

      @precondition: EClass.GetInstance().user.GetPermissions().GetPresPermLevel() != PermissionLevel.Lockdown
      
      @postcondition: self.currSlideNum == (Presenter's current slide number)
      """
      pass

   def SetPath(self, path):
      """
      Set the current path of the presentation file.

      @precondition: path != None
      @postcondition: self.path == path
      """
      pass

   def GetSlideNum(self):
      """
      Gets the current slide that the presentation is on.

      @return: The current slide number.
      """
      pass

   def GetSlide(self):
      """
      Get the current slide.

      @return: The current slide.
      """
      pass
      
   def Slidify(self):
      """
      Initialize a set of slides from the file at the presentation's path.
      
      @precondition: self.path != None
      
      @postcondition: len(self.slides) >= 1
      """
      pass


class Slide(object):
   """
   A Slide is a collection of presentation content and layers that can be edited by a presenter
   or student. A Slide contains zero or more layers that have been created specifically for its 
   presentation content. Although it is primarily a data container, a Slide also provides the 
   ability to reorder its layers.
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar content: The presentation content (HTML, CSS, etc) associated with the Slide.
   @ivar layers: Contains all of the Slide's layers.
   """
   
   def __init__(self, content, layers = []):
      """
      Initialize a Slide.

      @param content: The presentation content to assign the Slide
      @param layers: An initial set of layers for the Slide, if any
      """
      pass

   def GetContent(self):
      """
      Get the Slide's presentation content.
      
      @return: The Slide's presentation content.
      """
      pass

   def GetLayers(self):
      """
      Get the Slide's layers. An empty list is returned when there are no layers.
      
      @return: The Slide's layers.
      """
      pass
      
   def AddLayer(self, layer):
      """
      Add a Layer to the Slide's Layers.
      
      @param layer: The new Layer to add.
      
      @precondition: isinstance(layer, Layer)
      
      @postcondition: self.layers[-1] == layer
      """
      pass

   def OrderLayer(self, layer, newIndex):
      """
      Re-order the layers by moving the given layer to a different location on the layer stack.
      
      @param layer: The Layer to move.
      @param newIndex: The index to move the given Layer to.
      
      @precondition: 
         isinstance(layer, Layer) &&
         self.layers.count(layer) == 1 && 
         newIndex >= 0 &&
         newIndex < len(self.layers)
                     
      @postcondition: 
         self.layers.index(layer) == newIndex ||
         self.layers.index(layer) == newIndex - 1 (when newIndex is greater than the original index)
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
