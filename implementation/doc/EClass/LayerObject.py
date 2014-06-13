"""
Package LayerObject defines objects and operations within a presentation.

There are objects for both the presentation slides and the underlying markup (PresentationHTML).
This can be seen in the Layer and LayerPermission objects.
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

class DrawingToolsModel:
   """
   A DrawingToolsModel holds the functionality of selecting any of the drawing tools from the DrawingTools
   tool bar. In our implementation, drawing is done on a frame known as a layer. Each user has a series of layers 
   to draw on. See the Layer class under Presentation.py for more information.

   @author: Mike Sevilla (mjsevill@calpoly.edu)

   @ivar selectedTool: Represents the currently selected tool
   """

   def __init__(self):
      """
      Initialize the selectedTool to 'None'
      """
      pass

   def PencilToolHandler(self, event):
      """
      Change the selected tool to the 'Pencil'

      @param event: Event that called this method

      @postcondition: selectedTool == 'Pencil'
      """
      pass

   def HandToolHandler(self, event):
      """
      Change the selected tool to the 'Hand'

      @param event: Event that called this method

      @postcondition: selectedTool == 'Hand'
      """
      pass

   def TextToolHandler(self, event):
      """
      Change the selected tool to the 'Text'

      @param event: Event that called this method

      @postcondition: selectedTool == 'Text'
      """
      pass

   def CircleShapeHandler(self, event):
      """
      Change the selected tool to the 'Circle Shape'

      @param event: Event that called this method

      @postcondition: selectedTool == 'Circle Shape'
      """
      pass

   def SquareShapeHandler(self, event):
      """
      Change the selected tool to the 'Square Shape'

      @param event: Event that called this method

      @postcondition: selectedTool == 'Square Shape'
      """
      pass

   def TriangleShapeHandler(self, event):
      """
      Change the selected tool to the 'Triangle Shape'

      @param event: Event that called this method

      @postcondition: selectedTool == 'Triangle Shape'
      """
      pass

class DrawingTools:
   """
   A DrawingTools is a tool bar containing the various drawing tools a student or presenter may use during a presentation.
   In our implementation, drawing is done on a frame known as a layer. Each user has a series of layers 
   to draw on. See the Layer class under Presentation.py for more information.

   @author: Mike Sevilla (mjsevill@calpoly.edu)

   @ivar pencilTool: Tool that simulates drawing with a pencil on the layer
   @ivar handTool: Tool that is used to grab, move, or manipulate LayerObjects on a layer
   @ivar textTool: Tool that creates text boxes
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

   def OnClose (self, event):
      """
      Handles closing the DrawingTools tool bar.

      @precondition: showDrawingToolsMenuItem.IsChecked() == True

      @postcondition: showDrawingToolsMenuItem.IsChecked() == False
      """
      pass