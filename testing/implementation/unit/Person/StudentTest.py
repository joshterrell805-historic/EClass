import unittest
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Person')

from Student import Student

class StudentTest(unittest.TestCase):
   """
   Class StudentTest is the companion testing class for class Student.
   It implements the following class test plan:

      Phase 1: Unit test the constructor.
      Phase 2: Unit test the permissions access methods SetPermissions and 
               GetPermissions.
      Phase 3: Unit test the status access methods SetPresent, IsPresent,
               SetKicked, and IsKicked.
      Phase 4: Unit test the question methods HasQuestion, SetQuestion,
               and GetQuestion.
      Phase 5: Unit test the layer methods SetPushedLayer and GetPushedLayer.
   """

   def __init__(self, username, password, permissions):
      """
      Test that all ivars are initialized correctly.
      Test when no initial permissions are given.
      Test when initial permissions are given.
      """
      pass

   def GetPermissions(self):
      """
      Test that a StudentPermissions object is returned.
      """
      pass

   def SetPermissions(self, permissions):
      """
      Test when permissions is None/null.
      Test when permissions is not an instance of StudentPermissions.
      Test when permissions is a valid StudentPermissions.
      """
      pass
      
   def IsPresent(self):
      """
      Test that True is returned when the student is present.
      Test that False is returned when the student is not present.
      """
      pass
      
   def SetPresent(self, value):
      """
      Test when value is not True or False.
      Test when value is True.
      Test when value is False.
      """
      pass
      
   def IsKicked(self):
      """
      Test that True is returned when the student has been kicked.
      Test that False is returned when the student has not been kicked.
      """
      pass
      
   def SetKicked(self, value):
      """
      Test when value is not True or False.
      Test when value is True.
      Test when value is False.
      """
      pass
      
   def HasQuestion(self):
      """
      Test that True is returned when the student has a question.
      Test that False is returned when the student does not have a question.
      """
      pass
      
   def GetQuestion(self):
      """
      Test when the student has a Question.
      Test when the student does not have a Question.
      Test that return value is always a Question or None.
      """
      pass
      
   def SetQuestion(self, question):
      """
      Test when question is an instance of Question.
      Test when question is not an instance of Question.
      """
      pass
         
   def GetPushedLayer(self):
      """
      Test when the student has a layer to push.
      Test when the student does not have a layer to push.
      Test that return value is always a Layer or None.
      """
      pass
      
   def SetPushedLayer(self, layer):
      """
      Test when layer is an instance of Layer.
      Test when layer is not an instance of Layer.
      """
      pass
      