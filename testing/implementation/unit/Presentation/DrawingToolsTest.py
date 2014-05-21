import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Presentation')

from DrawingToolsModel import DrawingToolsModel

class DrawingToolsTest(unittest.TestCase):
   """
   Class DrawingToolsTest is the companion testing class for class DrawingTools.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the tool changing methods PecilToolHander, HandToolHander,
               AttachmentToolHandler, TextToolHandler, CircleShapeHander, SquareShapeHander,
               and TriangleShapeHandler.
   """

   def setUp(self):
      """
      Unit test the constructor by building one DrawingTools object.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Sample path             Proper init done     Only case
      """

      self.samplePath = None
      self.drawingTools = DrawingToolsModel()
      self.assertEqual(self.drawingTools.selectedTool, None)

   def test_PencilToolHandler(self):
      """
      Unit test PencilToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.PencilToolHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Pencil')


   def test_HandToolHandler(self):
      """
      Unit test HandToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.HandToolHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Hand')
      

   def test_AttachmentToolHandler(self):
      """
      Unit test AttachmentToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.AttachmentToolHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Attachment')
      

   def test_TextToolHandler(self):
      """
      Unit test TextToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.TextToolHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Text')
      

   def test_CircleShapeHandler(self):
      """
      Unit test CircleShapeToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.CircleShapeHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Circle Shape')

   def test_SquareShapeHandler(self):
      """
      Unit test SquareShapeToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.SquareShapeHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Square Shape')

   def test_TriangleShapeHandler(self):
      """
      Unit test TriangleShapeToolHandler.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        null                    null                 All other tools are deselected
      """
      
      self.drawingTools.TriangleShapeHandler()
      self.assertEqual(self.drawingTools.selectedTool, 'Triangle Shape')

if __name__ == "__main__":
   unittest.main()