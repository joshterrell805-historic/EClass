import wx

from EClass import EClass

class DrawingTools(wx.Frame):
   def __init__(self):
      super(DrawingTools, self).__init__(None, -1, 'Drawing Tools')

      self.SetClientSizeWH(275, 65)
      self.SetBackgroundColour('#FFFFFFF')

      ID_PENCIL_TOOL = wx.NewId()
      ID_HAND_TOOL = wx.NewId()
      ID_ATTACHMENT_TOOL = wx.NewId()
      ID_TEXT_TOOL = wx.NewId()
      ID_BASIC_SHAPES_TOOL = wx.NewId()

      drawingTools = self.CreateToolBar()
      pencilTool = drawingTools.AddLabelTool(ID_PENCIL_TOOL, 'Pencil', wx.Image('view//PencilIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                             shortHelp='Pencil Tool')
      handTool = drawingTools.AddLabelTool(ID_HAND_TOOL, 'Hand', wx.Image('view//HandIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                           shortHelp='Hand Tool')
      attachmentTool = drawingTools.AddLabelTool(ID_ATTACHMENT_TOOL, 'Attachment', wx.Image('view//PaperClipIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                 shortHelp='Attachment Tool')
      textTool = drawingTools.AddLabelTool(ID_TEXT_TOOL, 'Text', wx.Image('view//TextIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                           shortHelp='Text Tool')
      basicShapesTool = drawingTools.AddLabelTool(ID_BASIC_SHAPES_TOOL, 'Basic Shapes', wx.Image('view//BasicShapesIcon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(),
                                                  shortHelp='Basic Shapes Tool')

      drawingTools.Realize()

      self.Show()