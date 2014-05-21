import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Presentation')

from Presentation import Presentation
from Slide import Slide

class PresentationTest(unittest.TestCase):
   """
   Class PresentationTest is the companion testing class for class Presentation.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the path access methods SetPath and GetPath.
      Phase 3: Unit test the Slidify method.
      Phase 4: Unit test the slide changing methods MoveToNextSlide,
               MoveToPreviousSlide, MoveToSlide, and SyncWithPresenter.
      Phase 5: Unit test the getter methods GetSlideNum and GetSlide.
   """

   def setUp(self):
      """
      Unit test the constructor by building one Presentation object.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Sample path             Proper init done     Only case
      """
      self.samplePath = './PresentationTestSample.html'
      self.sampleSlideCount = 300
      self.presentation = Presentation(self.samplePath)
      self.assertEqual(len(self.presentation.slides), 0)
      self.assertEqual(self.presentation.path, self.samplePath)
      self.assertEqual(self.presentation.currSlideNum, 0)
      self.presentation.Slidify()
      self.assertEqual(len(self.presentation.slides), self.sampleSlideCount)

   def test_SetPath(self):
      """
      Unit test SetPath by sending it valid and invalid paths.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        Sample path             path = Sample path   Valid
      2        None                    path = None          Valid for now
      3        ''                      path = ''            Valid for now
      """
      self.presentation.SetPath(self.samplePath)
      self.assertEqual(self.presentation.path, self.samplePath)
      self.presentation.SetPath(None)
      self.assertEqual(self.presentation.path, None)
      self.presentation.SetPath('')
      self.assertEqual(self.presentation.path, '')

   def test_GetPath(self):
      """
      Unit test GetPath.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        path = self.samplePath  self.samplePath      Only case
      """
      self.assertEqual(self.presentation.GetPath(), self.samplePath)
      
   def test_Slidify(self):
      """
      Unit test Slidify using a variety of paths and presentation content.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        path = None             No slides created    
      2        path = ''               No slides created
      3        file with no slide      1 slide created
               breaks
      4        path = self.samplePath  300 slides created
      5        file with malformed     No slides created
               slide breaks
      6        file with no <body>     No slides created
               tag
      """
      
   def test_MoveToNextSlide(self):
      """
      Unit test MoveToNextSlide.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        currSlideNum = 0        currSlideNum = 299   Advance through all slides
      2        currSlideNum = 299      False returned       Top of range
      """
      self.assertEqual(self.presentation.currSlideNum, 0)
      for i in range(len(self.presentation.slides) - 1):
         self.assertEqual(self.presentation.currSlideNum, i)
         self.assertTrue(self.presentation.MoveToNextSlide())
      
      self.assertFalse(self.presentation.MoveToNextSlide())
      self.assertEqual(self.presentation.currSlideNum, self.sampleSlideCount - 1)

   def test_MoveToPreviousSlide(self):
      """
      Unit test MoveToPreviousSlide.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        currSlideNum = 299      currSlideNum = 0     Advance through all slides in reverse
      2        currSlideNum = 0        False returned       Bottom of range
      """
      self.presentation.currSlideNum = self.sampleSlideCount - 1
      for i in range(len(self.presentation.slides) - 1):
         self.assertEqual(self.presentation.currSlideNum, self.sampleSlideCount - 1 - i)
         self.assertTrue(self.presentation.MoveToPreviousSlide())
      
      self.assertFalse(self.presentation.MoveToPreviousSlide())
      self.assertEqual(self.presentation.currSlideNum, 0)

   def test_MoveToSlide(self):
      """
      Unit test MoveToSlide by passing a wide range of slide numbers.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        slideNum = 0            False returned       Just below bottom
      2        slideNum = -100         False returned       Well below bottom
      3        slideNum = 301          False returned       Just above top
      4        slideNum = 401          False returned       Well above top
      5        slideNum = 1            currSlideNum = 0     Bottom of range
      6        slideNum = 150          currSlideNum = 149   Middle of range
      7        slideNum = 300          currSlideNum = 299   Top of range
      """
      self.assertEqual(self.presentation.currSlideNum, 0)
      self.assertFalse(self.presentation.MoveToSlide(0))
      self.assertFalse(self.presentation.MoveToSlide(-100))
      self.assertFalse(self.presentation.MoveToSlide(301))
      self.assertFalse(self.presentation.MoveToSlide(401))
      
      self.assertTrue(self.presentation.MoveToSlide(1))
      self.assertEqual(self.presentation.currSlideNum, 0)
      self.assertTrue(self.presentation.MoveToSlide(150))
      self.assertEqual(self.presentation.currSlideNum, 149)
      self.assertTrue(self.presentation.MoveToSlide(self.sampleSlideCount))
      self.assertEqual(self.presentation.currSlideNum, self.sampleSlideCount - 1)

   def test_SyncWithPresenter(self):
      """
      Unit test SyncWithPresenter.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        currSlideNum =          No slide change
               presenter currSlideNum
      2        currSlideNum !=         currSlideNum =
               presenter currSlideNum  presenter currSlideNum    
      """
      

   def test_GetSlideNum(self):
      """
      Unit test GetSlideNum with a wide range of current slide numbers.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        currSlideNum = 0        1                    Bottom of range
      2        currSlideNum = 149      150                  Middle of range
      3        currSlideNum = 299      300                  Top of range
      """
      self.assertEqual(self.presentation.GetSlideNum(), 1)
      self.presentation.MoveToSlide(150)
      self.assertEqual(self.presentation.GetSlideNum(), 150)
      self.presentation.MoveToSlide(300)
      self.assertEqual(self.presentation.GetSlideNum(), 300)

   def test_GetSlide(self):
      """
      Unit test GetSlide.

      Test
      Case     Input                   Output               Remarks
      =========================================================================
      1        none                    Slide returned       Only case
      """
      self.assertTrue(isinstance(self.presentation.GetSlide(), Slide))
      
      
if __name__ == "__main__":
   unittest.main()
