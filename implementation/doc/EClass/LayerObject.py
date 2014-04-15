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

   @ivar: pencilTool: Tool that simulates drawing with a pencil on the layer
   @ivar: handTool: Tool that is used to grab, move, or manipulate LayerObjects on a layer
   @ivar: attachmentTool: Tool that allows users to upload external media such as images to a presentation
   @ivar: textTool: Tool that creates text boxes
   @ivar: basicShapesTool: Tool that allows a user to create basic shapes on the layer (circle, square, triangle)
   """