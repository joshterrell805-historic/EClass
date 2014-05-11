import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Person')
sys.path.insert(0, '../../../../implementation/source/python/model/Presentation')

from StudentPermissions import StudentPermissions
from Presentation.PermissionLevel import PermissionLevel

class StudentPermissionsTest(unittest.TestCase):
   """
   Class QuestionTest is the companion testing class for class Question.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the Permission Level access methods GetPresPermLevel
               and SetPresPermLevel.
      Phase 3: Unit test the hand raise access methods CanRaiseHand and
               SetCanRaiseHand.
      Phase 4: Unit test the layer pushing access methods CanPushLayer and
               SetCanPushLayer.
   """
