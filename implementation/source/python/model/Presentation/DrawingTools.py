from DrawingTools import DrawingTools

class DrawingToolsModel:
   def __init__(self):
      self.selectedTool = None

   def PencilToolHandler(self, e):
      self.selectedTool = 'Pencil'
      print("From DrawingTools.PencilToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def HandToolHandler(self, e):
      self.selectedTool = 'Hand'
      print("From DrawingTools.HandToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def AttachmentToolHandler(self, e):
      self.selectedTool = 'Attachment'
      print("From DrawingTools.AttachmentToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def TextToolHandler(self, e):
      self.selectedTool = 'Text'
      print("From DrawingTools.TextToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def CircleShapeHandler(self, e):
      self.selectedTool = 'Circle Shape'
      print("From DrawingTools.CircleShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def SquareShapeHandler(self, e):
      self.selectedTool = 'Square Shape'
      print("From DrawingTools.SquareShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def TriangleShapeHandler(self, e):
      self.selectedTool = 'Triangle Shape'
      print("From DrawingTools.TriangleShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))
