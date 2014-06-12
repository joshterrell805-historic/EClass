import unittest
import sys

sys.path.insert(0, '../../../implementation/source/python/model/Presentation')

from Slide import Slide
from LayerManagerModel import LayerManagerModel
from Layer import Layer

from Roster import Roster

class RosterItem:
   def __init__(self, student):
      self.student = student
      pass

   def Hand(self):
      print('From Roster.Hand()')

   def Layers(self):
      print('From Roster.Layers()')
