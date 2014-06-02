import wx
import sys
sys.path.insert(0, 'model/Presentation')

from EClass import EClass
from DrawingToolsModel import DrawingToolsModel

"""
   Class DrawingTools provides the functionality for all DrawingToolsModel-related actions. Class DrawingTools
   provides methods to toggle the various drawing tools such as the hand tool to move objects and the pencil tool
   to draw on the presentation.

   @author Mike Sevilla (mjsevill@calpoly.edu)
"""

class DrawingTools(wx.Frame):
   """
      The __init__ function for Class DrawingTools provides all the set up for the drawing tools tool bar. Set up
      includes creating the tool bar, setting the size, and setting up the tool buttons.
   """
   def __init__(self, parent):
      """
         Local variables include object IDs for each tool as well as communication between the view and model.
      """
      super(DrawingTools, self).__init__(None, -1, 'Drawing Tools', style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

      self.SetClientSizeWH(235, 45)
      self.SetBackgroundColour('#FFFFFFF')
      self.parent = parent
      self.drawingToolsModel = DrawingToolsModel()

      self.ID_PENCIL_TOOL = wx.NewId()
      self.ID_HAND_TOOL = wx.NewId()
      self.ID_TEXT_TOOL = wx.NewId()
      self.ID_CIRCLE_SHAPE = wx.NewId()
      self.ID_TRIANGLE_SHAPE = wx.NewId()
      self.ID_SQUARE_SHAPE = wx.NewId()

      self.drawingTools = self.CreateToolBar()

      """
         Initialization of each tool and action handlers for when they are pressed.
      """
      self.pencilTool = self.drawingTools.AddLabelTool(self.ID_PENCIL_TOOL, 'Pencil', wx.Image('view//PencilIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                       shortHelp='Pencil Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.PencilToolHandler, self.pencilTool)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)

      self.handTool = self.drawingTools.AddLabelTool(self.ID_HAND_TOOL, 'Hand', wx.Image('view//HandIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                     shortHelp='Hand Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.HandToolHandler, self.handTool)

      self.textTool = self.drawingTools.AddLabelTool(self.ID_TEXT_TOOL, 'Text', wx.Image('view//TextIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                     shortHelp='Text Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.TextToolHandler, self.textTool)

      self.circleTool = self.drawingTools.AddLabelTool(self.ID_CIRCLE_SHAPE, 'Circle Shape', wx.Image('view//CircleIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                       shortHelp='Circle Shape', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.CircleShapeHandler, self.circleTool)

      self.squareTool = self.drawingTools.AddLabelTool(self.ID_SQUARE_SHAPE, 'Square Shape', wx.Image('view//SquareIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                       shortHelp='Square Shape', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.SquareShapeHandler, self.squareTool)

      self.triangleTool = self.drawingTools.AddLabelTool(self.ID_TRIANGLE_SHAPE, 'Triangle Shape', wx.Image('view//TriangleIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                       shortHelp='Triangle Shape', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.TriangleShapeHandler, self.triangleTool)

      self.drawingTools.Realize()
      self.Bind(wx.EVT_CLOSE, self.onClose)

   """
      The PencilToolHandler function is called when the pencil tool is selected. It deselects all other tools.
   """
   def PencilToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_SQUARE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_CIRCLE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_TRIANGLE_SHAPE, False)
      self.drawingToolsModel.PencilToolHandler()


   """
      The HandToolHandler function is called when the hand tool is selected. It deselects all other tools.
   """
   def HandToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_SQUARE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_CIRCLE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_TRIANGLE_SHAPE, False)
      self.drawingToolsModel.HandToolHandler()

   """
      The TextToolHandler function is called when the text tool is selected. It deselects all other tools.
   """
   def TextToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_SQUARE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_CIRCLE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_TRIANGLE_SHAPE, False)
      self.drawingToolsModel.TextToolHandler()

   """
      The CircleShapeHandler function is called when the circle tool is selected. It deselects all other tools.
   """
   def CircleShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_SQUARE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_TRIANGLE_SHAPE, False)
      self.drawingToolsModel.CircleShapeHandler()

   """
      The SquareShapeHandler function is called when the square tool is selected. It deselects all other tools.
   """
   def SquareShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_CIRCLE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_TRIANGLE_SHAPE, False)
      self.drawingToolsModel.SquareShapeHandler()

   """
      The TriangleShapeHandler function is called when the triangle tool is selected. It deselects all other tools.
   """
   def TriangleShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_SQUARE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_CIRCLE_SHAPE, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingToolsModel.TriangleShapeHandler()

   """
      The onClose fuction hides the drawing tools when the option is selected from the menu bar or the 'x'.
   """
   def onClose(self, event):
      self.parent.showDrawingToolsMenuItem.Check(False)
      self.Hide()
