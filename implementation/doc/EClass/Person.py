"""
Package Person defines objects and operations related to any user of the EClass.

There are objects for both a student and a presenter. Additionally, there are objects for a student's permissions, a presenter's credentials, and the Roster.
"""

from Presentation import PermissionLevel

class Person:
   """
   Person is a class that is instantiated when someone logs into the EClass.

   @author: Kevin Le (kle17@calpoly.edu)
   """

   def __init__(self, asdf):
      """
      Build an instance of a person.

      @param self: self is the instance of this object
      @param asdf: trash for now
      """
      pass


class Student(Person):
   """
   Student contains informaton on the student. It contains things like if they are here, if their hand is raised, layers they might want to push, current approval, and their permissions/restrictions to how they use the app.
   
   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar permissions: The student's set of permissions.
   @ivar kicked: Boolean indicating if the student has been kicked.
   @ivar present: Boolean indicating if the student is present.
   """

   def __init__(self, username, password, permissions):
      """
      Initialize a Student.

      @param username: The student's username
      @param password: The student's password
      @param permissions: The student's initial set of permissions
      """
      pass

   def GetPermissions(self):
      """
      Get the Student's permissions.

      @return: self.permissions
      """
      pass

   def SetPermissions(self, value):
      """
      Set the student's permissions with a new StudentPermissions object.

      @param value: The new set of student permissions.

      @precondition: isinstance(value, StudentPermissions) == True

      @postcondition: self.permissions == value
      """
      pass


class StudentPermissions(object):
   """
   StudentPermissions has various access rights to tools that the student can use.

   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar presPermLevel: A student's PermissionLevel for presentation and layer interactions.
   @ivar canRaiseHand: Boolean indicating if a student is allowed to raise their hand and ask a question.
   @ivar canPushLayer: Boolean indicating if a student is allowed to push a layer to the presenter's stack.
   """

   def __init__(self, presPermLevel, canRaiseHand, canPushLayer):
      """
      Initialize a StudentPermissions object.

      @param presPermLevel: A presentaton PermissionLevel for a student.
      @param canRaiseHand: Boolean indicating if a student is allowed to raise their hand and ask a question.
      @param canPushLayer: Boolean indicating if a student is allowed to push a layer to the presenter's stack.
      """
      pass

   def GetPresPermLevel(self):
      """
      Get the student's current presentation PermissionLevel.

      @return: self.presPermLevel
      """
      pass

   def SetPresPermLevel(self, value):
      """
      Set the student's PermissionLevel with a new PermissionLevel.

      @param value: The new PermissionLevel

      @precondition: isinstance(value, PermissionLevel) == True

      @postcondition: self.presPermLevel == value
      """
      pass

   def CanRaiseHand(self):
      """
      Get the student's current permission for raising their hand.

      @return: self.canRaiseHand
      """
      pass

   def SetCanRaiseHand(self, value):
      """
      Set the student's ability to raise their hand.

      @param value: A boolean value

      @precondition: value == True or value == False

      @postcondition: self.canRaiseHand == value
      """
      pass

   def CanPushLayer(self):
      """
      Get the student's current permission for pushing a layer.

      @return: self.canPushLayer
      """
      pass

   def SetCanPushLayer(self, value):
      """
      Set the student's ability to push a layer to the presenter's stack.

      @param value: A boolean value

      @precondition: value == True or value == False

      @postcondition: self.canPushLayer == value
      """
      pass
