import wx

from EClass import EClass

class DrawingTools(wx.Frame):
   def __init__(self):
      super(DrawingTools, self).__init__(None, -1, 'Drawing Tools', style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

      self.SetClientSizeWH(305, 65)
      self.SetBackgroundColour('#FFFFFFF')

      self.ID_PENCIL_TOOL = wx.NewId()
      self.ID_HAND_TOOL = wx.NewId()
      self.ID_ATTACHMENT_TOOL = wx.NewId()
      self.ID_TEXT_TOOL = wx.NewId()
      self.ID_BASIC_SHAPES_TOOL = wx.NewId()
      self.ID_BASIC_SHAPES_DROPDOWN_CIRCLE = wx.NewId()
      self.ID_BASIC_SHAPES_DROPDOWN_TRIANGLE = wx.NewId()
      self.ID_BASIC_SHAPES_DROPDOWN_SQUARE = wx.NewId()

      self.selectedTool = None

      self.drawingTools = self.CreateToolBar()
      
      self.pencilTool = self.drawingTools.AddLabelTool(self.ID_PENCIL_TOOL, 'Pencil', wx.Image('view//PencilIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                       shortHelp='Pencil Tool', kind=wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.PencilToolHandler, self.pencilTool)
      self.drawingTools.ToggleTool(self.ID_PENCIL_TOOL, False)

      self.handTool = self.drawingTools.AddLabelTool(self.ID_HAND_TOOL, 'Hand', wx.Image('view//HandIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                     shortHelp='Hand Tool', kind=wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.HandToolHandler, self.handTool)
      
      self.attachmentTool = self.drawingTools.AddLabelTool(self.ID_ATTACHMENT_TOOL, 'Attachment', wx.Image('view//PaperClipIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                           shortHelp='Attachment Tool', kind=wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.AttachmentToolHandler, self.attachmentTool)

      self.textTool = self.drawingTools.AddLabelTool(self.ID_TEXT_TOOL, 'Text', wx.Image('view//TextIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                     shortHelp='Text Tool', kind=wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.TextToolHandler, self.textTool)
      
      self.basicShapesTool = self.drawingTools.AddLabelTool(self.ID_BASIC_SHAPES_TOOL, 'Basic Shapes', wx.Image('view//BasicShapesIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                            shortHelp='Basic Shapes Tool', kind=wx.ITEM_DROPDOWN)

      self.basicShapesDropdown = wx.Menu()
      self.circleShape = self.basicShapesDropdown.Append(self.ID_BASIC_SHAPES_DROPDOWN_CIRCLE, 'Circle', 'Circle Shape', wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.CircleShapeHandler, self.circleShape)

      self.squareShape = self.basicShapesDropdown.Append(self.ID_BASIC_SHAPES_DROPDOWN_SQUARE, 'Square', 'Square Shape', wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.SquareShapeHandler, self.squareShape)

      self.triangleShape = self.basicShapesDropdown.Append(self.ID_BASIC_SHAPES_DROPDOWN_TRIANGLE, 'Triangle', 'Triangle Shape', wx.ITEM_RADIO)
      self.Bind(wx.EVT_MENU, self.TriangleShapeHandler, self.triangleShape)

      self.basicShapesTool.SetDropdownMenu(self.basicShapesDropdown)

      self.drawingTools.Realize()

   def PencilToolHandler(self, e):
      self.selectedTool = 'Pencil'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))

   def HandToolHandler(self, e):
      self.selectedTool = 'Hand'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))

   def AttachmentToolHandler(self, e):
      self.selectedTool = 'Attachment'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))

   def TextToolHandler(self, e):
      self.selectedTool = 'Text'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))

   def CircleShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_BASIC_SHAPES_TOOL, True)
      self.selectedTool = 'Circle Shape'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))

   def SquareShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_BASIC_SHAPES_TOOL, True)
      self.selectedTool = 'Square Shape'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))

   def TriangleShapeHandler(self, e):
      self.drawingTools.ToggleTool(self.ID_BASIC_SHAPES_TOOL, True)
      self.selectedTool = 'Triangle Shape'
      print("Selected Tool is: {tool}".format(tool = self.selectedTool))
