import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Presentation')

from Slide import Slide

class SlideTest(unittest.TestCase):
   """
   Class SlideTest is the companion testing class for class Slide.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the HTML/CSS content access method GetContent.
      Phase 3: Unit test layer access methods AddLayer and GetLayers.
      Phase 4: Unit test the layer ordering method OrderLayer.
   """