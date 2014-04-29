import sys

class DrawingToolsModel:
   def __init__(self):
      self.selectedTool = None

   def PencilToolHandler(self):
      self.selectedTool = 'Pencil'
      print("From DrawingTools.PencilToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def HandToolHandler(self):
      self.selectedTool = 'Hand'
      print("From DrawingTools.HandToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def AttachmentToolHandler(self):
      self.selectedTool = 'Attachment'
      print("From DrawingTools.AttachmentToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def TextToolHandler(self):
      self.selectedTool = 'Text'
      print("From DrawingTools.TextToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def CircleShapeHandler(self):
      self.selectedTool = 'Circle Shape'
      print("From DrawingTools.CircleShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def SquareShapeHandler(self):
      self.selectedTool = 'Square Shape'
      print("From DrawingTools.SquareShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   def TriangleShapeHandler(self):
      self.selectedTool = 'Triangle Shape'
      print("From DrawingTools.TriangleShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))
