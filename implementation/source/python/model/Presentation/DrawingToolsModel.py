import sys

"""
   Class DrawingToolsModel confirms the correct selection of tools when the various tools are
   selected from the corresponding classes in the DrawingTools view.

   @author Mike Sevilla (mjsevill@calpoly.edu)
"""

class DrawingToolsModel:
   """
      The __init__ function for Class DrawingToolsModel provides the selectedTool variable that changes
      based upon which tool is selected.
   """
   def __init__(self):
      self.selectedTool = None

   """
      The PencilToolHandler function is called when the pencil tool is selected. It changes the selected
      tool to the pencil.
   """
   def PencilToolHandler(self):
      self.selectedTool = 'Pencil'
      print("From DrawingTools.PencilToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   """
      The HandToolHandler function is called when the pencil tool is selected. It changes the selected
      tool to the hand.
   """
   def HandToolHandler(self):
      self.selectedTool = 'Hand'
      print("From DrawingTools.HandToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   """
      The TextToolHandler function is called when the pencil tool is selected. It changes the selected
      tool to the text.
   """
   def TextToolHandler(self):
      self.selectedTool = 'Text'
      print("From DrawingTools.TextToolHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   """
      The CircleShapeHandler function is called when the pencil tool is selected. It changes the selected
      tool to the circle.
   """
   def CircleShapeHandler(self):
      self.selectedTool = 'Circle Shape'
      print("From DrawingTools.CircleShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   """
      The SquareShapeHandler function is called when the pencil tool is selected. It changes the selected
      tool to the square.
   """
   def SquareShapeHandler(self):
      self.selectedTool = 'Square Shape'
      print("From DrawingTools.SquareShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))

   """
      The TriangleShapeHandler function is called when the pencil tool is selected. It changes the selected
      tool to the triangle.
   """
   def TriangleShapeHandler(self):
      self.selectedTool = 'Triangle Shape'
      print("From DrawingTools.TriangleShapeHandler() - Selected Tool is: {tool}".format(tool = self.selectedTool))
