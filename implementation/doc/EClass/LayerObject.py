"""
Package LayerObject defines objects and operations within a presentation.

There are objects for both the presentation slides and the underlying markup (PresentationHTML). This can be seen in the Layer and LayerPermission objects.
"""

import sys
sys.path.insert(0, '../../source/python/model/enum')

# TODO: figure out why it's not recognizing enum then add it as base class for PermissionLevel
#from enum import Enum

class LayerObject:
   """
   A LayerObject is any editable object within a Layer.

   @author: Mike Sevilla (mjsevill@calpoly.edu)
   """


class DrawingTools:
   """
   A DrawingTools is a tool bar containing the various drawing tools a student or presenter may use during a presentation.

   @author: Mike Sevilla (mjsevill@calpoly.edu)

   @ivar pencilTool: Tool that simulates drawing with a pencil on the layer
   @ivar handTool: Tool that is used to grab, move, or manipulate LayerObjects on a layer
   @ivar attachmentTool: Tool that allows users to upload external media such as images to a presentation
   @ivar textTool: Tool that creates text boxes
   @ivar basicShapesTool: Tool that allows a user to create basic shapes on the layer (circle, square, triangle)
   @ivar basicShapesDropdown: Drop down menu for the basic shapes (circle, square, triangle)
   @ivar circleShape: Basic shape tool for a circle
   @ivar squareShape: Basic shape tool for a square
   @ivar triangleShape: Basic shape tool for a triangle
   """

   def __init__(self):
      """
      Initialize a Drawing Tools window.
      """
      pass

   def PencilToolHandler(self, event):
      """
      Handles pencil tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      pencilTool.ToggleTool() == True
      """
      pass

   def HandToolHandler(self, event):
      """
      Handles hand tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      handTool.ToggleTool() == True
      """
      pass

   def AttachmentToolHandler(self, event):
      """
      Handles attachment tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      attachmentTool.ToggleTool() == True
      """
      pass

   def TextToolHandler(self, event):
      """
      Handles text tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      textTool.ToggleTool() == True
      """
      pass

   def CircleShapeHandler(self, event):
      """
      Handles circle shape tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      circleShape.ToggleTool() == True
      """
      pass

   def SquareShapeHandler(self, event):
      """
      Handles square shape tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      squareShape.ToggleTool() == True
      """
      pass

   def TriangleShapeHandler(self, event):
      """
      Handles triangle shape tool events when this tool is selected.

      @param event: Event that called this method

      @postcondition: for (tools.ToggleTool() : DrawingTools) == False &&
      triangleShape.ToggleTool() == True
      """
      pass