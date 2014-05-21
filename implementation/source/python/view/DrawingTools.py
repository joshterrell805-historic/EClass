import wx
import sys
sys.path.insert(0, 'model/Presentation')

from EClass import EClass
from DrawingToolsModel import DrawingToolsModel

class DrawingTools(wx.Frame):
   def __init__(self, parent):
      super(DrawingTools, self).__init__(None, -1, 'Drawing Tools', style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

      self.SetClientSizeWH(305, 65)
      self.SetBackgroundColour('#FFFFFFF')
      self.parent = parent
      self.drawingToolsModel = DrawingToolsModel()

      self.ID_PENCIL_TOOL = wx.NewId()
      self.ID_HAND_TOOL = wx.NewId()
      self.ID_ATTACHMENT_TOOL = wx.NewId()
      self.ID_TEXT_TOOL = wx.NewId()
      self.ID_BASIC_SHAPES_TOOL = wx.NewId()
      self.ID_BASIC_SHAPES_CIRCLE = wx.NewId()
      self.ID_BASIC_SHAPES_TRIANGLE = wx.NewId()
      self.ID_BASIC_SHAPES_SQUARE = wx.NewId()

      self.drawingTools = self.CreateToolBar()
      
      self.pencilTool = self.drawingTools.AddLabelTool(self.ID_PENCIL_TOOL, 'Pencil', wx.Image('view//PencilIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                       shortHelp='Pencil Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.PencilToolHandler, self.pencilTool)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)

      self.handTool = self.drawingTools.AddLabelTool(self.ID_HAND_TOOL, 'Hand', wx.Image('view//HandIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                     shortHelp='Hand Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.HandToolHandler, self.handTool)
      
      self.attachmentTool = self.drawingTools.AddLabelTool(self.ID_ATTACHMENT_TOOL, 'Attachment', wx.Image('view//PaperClipIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                           shortHelp='Attachment Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.AttachmentToolHandler, self.attachmentTool)

      self.textTool = self.drawingTools.AddLabelTool(self.ID_TEXT_TOOL, 'Text', wx.Image('view//TextIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                     shortHelp='Text Tool', kind=wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.TextToolHandler, self.textTool)
      
      self.basicShapesTool = self.drawingTools.AddLabelTool(self.ID_BASIC_SHAPES_TOOL, 'Basic Shapes', wx.Image('view//BasicShapesIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                            shortHelp='Basic Shapes Tool', kind=wx.ITEM_DROPDOWN)

      self.basicShapesDropdown = wx.Menu()
      self.circleShape = self.basicShapesDropdown.Append(self.ID_BASIC_SHAPES_CIRCLE, 'Circle', 'Circle Shape', wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.CircleShapeHandler, self.circleShape)

      self.squareShape = self.basicShapesDropdown.Append(self.ID_BASIC_SHAPES_SQUARE, 'Square', 'Square Shape', wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.SquareShapeHandler, self.squareShape)

      self.triangleShape = self.basicShapesDropdown.Append(self.ID_BASIC_SHAPES_TRIANGLE, 'Triangle', 'Triangle Shape', wx.ITEM_CHECK)
      self.Bind(wx.EVT_MENU, self.TriangleShapeHandler, self.triangleShape)

      self.basicShapesTool.SetDropdownMenu(self.basicShapesDropdown)

      self.drawingTools.Realize()
      
      self.Bind(wx.EVT_CLOSE, self.onClose)

   def PencilToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_ATTACHMENT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_CIRCLE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_SQUARE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_TRIANGLE, False)
      self.drawingToolsModel.PencilToolHandler()


   def HandToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_ATTACHMENT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_CIRCLE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_SQUARE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_TRIANGLE, False)
      self.drawingToolsModel.HandToolHandler()

   def AttachmentToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_CIRCLE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_SQUARE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_TRIANGLE, False)
      self.drawingToolsModel.AttachmentToolHandler()

   def TextToolHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_ATTACHMENT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_CIRCLE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_SQUARE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_TRIANGLE, False)
      self.drawingToolsModel.TextToolHandler()

   def CircleShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_ATTACHMENT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_SQUARE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_TRIANGLE, False)
      self.drawingTools.ToggleTool(self.ID_BASIC_SHAPES_TOOL, True)
      self.drawingToolsModel.CircleShapeHandler()

   def SquareShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_ATTACHMENT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_CIRCLE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_TRIANGLE, False)
      self.drawingToolsModel.SquareShapeHandler()

   def TriangleShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_HAND_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_ATTACHMENT_TOOL, False)
      self.drawingTools.ToggleTool(self.ID_TEXT_TOOL, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_CIRCLE, False)
      self.basicShapesDropdown.Check(self.ID_BASIC_SHAPES_SQUARE, False)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)
      self.drawingToolsModel.TriangleShapeHandler()

   def onClose(self, event):
      self.parent.showDrawingToolsMenuItem.Check(False)
      self.Hide()
