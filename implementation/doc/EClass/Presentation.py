"""
Package Presentation defines objects and operations related to the presentation's content and navigation.

There are objects for both the presentation slides and the underlying markup (PresentationHTML). Additionally, this package includes much of the layer functionality. This can be seen in the Layer and LayerPermission objects.
"""

import sys
sys.path.insert(0, '../../source/python/model/enum')

class Presentation:
   """
   A Presentation is a collection of slides and their respective layers which is displayed at 
   the center of the EClass. View the Slide documentation for more detailed information about them. Presentation contains a variety of methods used to navigate between slides
   and access the current slide. It handles all of the model-related syncing functionality between presenters and students as well.
   It accomplishes this by passing messages back and forth between the presenter and the student(s). On a presenter client, the current slide is broadcast
   to each student whenever the slide is changed. A student's Presentation object will listen for the message and update accordingly if it is 
   currently set to stay synced.
   
   Presentation also includes the Slidify() method which opens up the HTML file located at a Presentation's
   path and converts it to a fresh set of slides to be displayed. Any <br class="slide"> tags
   in the HTML denote the location where a new Slide should be created and Slidify() will break 
   them up at those points. However, the method ensures there will always be at least one slide if
   there are no <br class="slide"> tags.

   @author: Joel Wilcox (jnwilcox@calpoly.edu), Kevin Le (kle17@calpoly.edu)

   @ivar currSlideNum: The index of the current slide.
   @ivar slides: Contains each of the slides in a presentation.
   @ivar path: Refers to the current file system path of the backing presentation file.
   @ivar isSynced: Boolean to keep track of whether the slides should be synced with the presenter's slides.
   @ivar rawHTML: A string copy of the presentation HTML contents.
   """

   def __init__(self, path):
      """
      Initialize a Presentation.

      @param path: The path to the presentation file.
      """
      pass

   def onSaveListener(self, eventType, identifier):
      """
      Internal use only (private). This is the callback passed to
      EClass.registerOnSaveListener. The parameters are documented in the respective
      EClass method's documentation.

      This callback returns an object representing the
      state of the presentation for both the 'initial data' save functionality and
      the 'file' save functionality. Both of these save functions are explained
      in the EClass methods' documentation.
      """
      pass

   def onInitialData(self, data):
      """
      Internal use only (private). This method is called from
      EClass.loadInitalData with the object returned from
      Presentation.onSaveListener when 'save initial data for student' is the
      `eventType`. This method initializes the presentation on a student's
      EClass given the data sent by the presenter.
      """
      pass
      
   def loadFileData(self, data):
      """
      Internal use only (private). This method is called from
      EClass.loadFileData with the object returned from
      Presentation.onSaveListener when 'save to file' is the
      `eventType`. This method initializes the presentation on the presenter's
      EClass given the data saved to file by a previous `file->save` operation.
      """
      pass

   def MoveToNextSlide(self):
      """
      Set the current slide to the next consecutive slide.

      @precondition: self.currSlideNum != len(self.slides) - 1

      @postcondition: self.currSlideNum == old(self.currSlideNum) + 1
      
      @return: True if the current slide was changed successfully, False otherwise
      """
      pass

   def MoveToPreviousSlide(self):
      """
      Set the current slide to the previous slide.

      @precondition: self.currSlideNum != 0

      @postcondition: self.currSlideNum == old(self.currSlideNum) - 1
      
      @return: True if the current slide was changed successfully, False otherwise
      """
      pass

   def MoveToSlide(self, slideNum):
      """
      Set the current slide to the slide at a given index.

      @param slideNum: The index (offset by 1) of the new slide to display.

      @precondition: slideNum >= 1 && slideNum <= len(self.slides)

      @postcondition: self.currSlideNum == slideNum - 1
      
      @return: True if the current slide was changed successfully, False otherwise
      """
      pass

   def SyncWithPresenter(self, doneSyncing):
      """
      Set the current slide to the slide being viewed by the presenter.
      
      @param doneSyncing: A callback method to update the view after syncing.

      @precondition: EClass.GetInstance().user.GetPermissions().GetPresPermLevel() != PermissionLevel.Lockdown
      
      @postcondition: self.currSlideNum == Presenter's current slide number
      """
      pass
      
   def OnSync(self, message, student):
      """
      Callback used together with SyncWithPresenter to listen for sync messages
      between a Student and the Presenter. When the Presenter is receiving the 
      message, OnSync sends a message back to the Student client with the 
      Presenter's current slide number. When the Student is receiving the message,
      OnSync completes the slide change.
      
      @param message: A dictionary containing the Presenter's current slide number.
      @param student: The student sending the message (when being called on the
         Presenter's client)
         
      @precondition: student != None when being called on the Presenter's client &&
         message['slideNum'] != None when being called on the Student's client
         
      @postcondition: self.currSlideNum == Presenter's current slide number
      """
      pass

   def SetPath(self, path):
      """
      Set the current path of the presentation file.

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
   or student. The presentation content is raw HTML to be displayed by a wxPython HTMLWindow. A Slide contains zero or more layers that have been created specifically for its 
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
   A layer is a collection of layer objects. Layers are like a sheet of paper
   on an overhead projector. You can stack them on top of eachother, swap
   positions, and draw on whichever one you want. They are always drawn in
   a specified order. Layers have several different properties including:
   the visual objects each layer contains, opacity (determining
   how transparent to draw each object), visiblility (a toggle
   determining whether to draw the layer at all), and lock (a toggle determing
   whether objects may be added to or moved on the layer).
   

   Layers contain layer objects which are python dictionaries holding
   representations of visual objects. The currently implemented layer objects are:
   square, text, and pencil. Each object has a type property defining what type it is
   "square" "text" or "pencil" and then a varying set of properties determining
   how to draw the object (position, points, width, height, ...)

   @author: Andrew Lisowski (alisowsk@calpoly.edu) + Josh (class doc)

   @ivar objects: A Collection of LayerObjects that represent all graphics on a Layer
   @ivar opacity: A double representing how transparent a Layer is
   @ivar visible: Boolean value representing if a Layer can or cannot be seen
   @ivar permissions: The LayerPermissions for a given Layer
   @ivar name: Name of the given Layer
   @ivar locked: Boolean determining whether the user can edit this layer.
   """
   def __init__(self, name, opacity, lock):
      """
      Initialize a Layer.

      @param name: The name of the new layer.
      @param opacity: How visible the layer is.
      @param lock: Whether the layer is locked.
      """
      pass

   def ChangePermissions(self, newPermissions):
      """
      Set the selected layer's permissions.

      @postcondition: self.permissions == newPermissions
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
      
   def ChangeName(self, newName):
      """
      Set the name of a layer.

      @param newName: The new name of the layer.
      
      @precondition: newName != ""

      @postcondition: self.name == newName
      """
      pass
      
   def SetOpacity(self, newOpacity):
      """
      Set the opacity of a layer.

      @param newOpacity: The new opacity of the layer.
      
      @precondition: newOpacity > -1 && newOpacity < 256

      @postcondition: self.opacity == newOpacity
      """
      pass

class LayerManagerModel:
   """
   This model manages the layers attached to the current slide. The layer manager is 
   initialized with each slide. To got the layers, the application looks at 
   what layers are stored in the current slide of presentiation. It handles adding 
   and removing objects from the selected layer. It essentially is the canvas and
   has acces to all of the necassary object information.

   @author: Andrew Lisowski (alisowsk@calpoly.edu)

   @ivar layers: A Collection of Layers that represent all graphics on a Slide
   @ivar currLayer: The current Layer selected in the layer manager
   @ivar parent: A reference to the parent class
   """
   def __init__(self, parent, layers):
      """
      Initialize a LayerManagerModel.
      
      @param parent: The caller of the layer manager.
      @param layers: The layers in the current slide.
      """
      pass

   def DeleteLayer(self):
      """
      Delete the selected slide

      @postcondition: self.layers.count() == old(self.layers.count()) - 1
      """
      pass

   def NewLayer(self, layer):
      """
      Creates a New Layer for the current Slide

      @param layer: The new layer to add to the slide.
      @postcondition: self.layers.count() == old(self.layers.count()) + 1
      """
      pass
      
   def ChangeOpacity(self, index):
      """
      Changes opacity of selected layer

      @param index: index of layer to change opacity on.
      @postcondition: self.layers[index].opacity != old(self.layers[index].opacity)
      """
      pass
      
   def SetCurrentLayer(self, index):
      """
      Changes the current layer

      @param index: index of layer to change opacity on.
      @precondition: index > -1 && index < len(self.layers)
      @postcondition: self.currLayer == index
      """
      pass
   
   def AddObj(self, newObj):
      """
      Adds an object to the current layer

      @param newObj: the new object to add to the layer
      @precondition: self.layers[self.currLayer].locked == False 
                     && self.layers[self.currLayer].visible == True
      @postcondition: len(self.layers[self.currLayer].objects) == len(old(self.layers[self.currLayer].objects)) + 1
      """
      pass
      
   def RemoveObject(self, objToRemove):
      """
      Removes an object to the current layer

      @param objToRemove: the object to remove
      @precondition: self.layers[self.currLayer].locked == False 
                     && self.layers[self.currLayer].visible == True
      @postcondition: len(self.layers[self.currLayer].objects) == len(old(self.layers[self.currLayer].objects)) - 1
      """
      pass
      
   def ChangeObjPos(self, objToChange, oldPos, newPos):
      """
      Changes position of an object on the current layer

      @param objToChange: object to take the action on
      @param oldPos: objects old position
      @param newPos: objects new position
      @precondition: self.layers[self.currLayer].locked == False 
                     && self.layers[self.currLayer].visible == True
      @postcondition: object has moved x and y coordinates
      """
      pass

class QuestionList():
   def __init__(self):
      """
      Initialize a new QuestionList
      """
      pass
   
   def Append(self, question):
      """
      Add question to the QuestionList

      @param question: question to add to the QuestionList
      @precondition: question != None
      @postcondition: question in self
      """

   def Remove(self, index):
      """
      Remove the question at the specified index in the QuestionList

      @param index: index of the question to be removed
      @precondition: index < len(self) && index >= 0
      @postcondition: question not in self
      """

   def RemoveAll(self):
      """
      Remove all questions from the QuestionList
      
      @precondition: None
      @postcondition: len(self) == 0
      """

   def __getitem__(self, index):
      """
      Returns the item at the specified index. Allows QuestionList to be
      accessed as an array: i.e QuestionList[0]

      @precondition: index < len(self) && index >= 0
      @postcondition: None
      """
