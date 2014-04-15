class LayerManager:
   """
   A Presentation is a collection of slides and their respective layers which is displayed at the center of the EClass.

   @author: Andrew Lisowski (alisowsk@calpoly.edu)
   """
   def __init__(self, parent):
      """
      Initialize a Layer Manager View.

      @param parent: The class that initialized this view..
      """

   def DeleteLayer(self, event):
      """
      Delete the selected slide

      @postcondition: self.layers.count() == old(self.layers.count()) - 1
      """

   def NewLayer(self, event):
      """
      Creates a New Layer for the current Slide

      @postcondition: self.layers.count() == old(self.layers.count()) + 1
      """

   def ChangeOpacity(self, event):
      """
      Changes opacity of selected layer

      @postcondition: self.layers[index].opacity != old(self.layers[index].opacity)
      """
