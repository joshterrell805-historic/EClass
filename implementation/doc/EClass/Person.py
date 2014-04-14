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

   @ivar _permissions: The student's set of permissions.
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

   @property
   def permissions(self):
      """
      Get the Student's permissions.
      """
      pass

   @permissions.setter
   def permissions(self, value):
      """
      Set the student's permissions with a new StudentPermissions object.

      @param value: The new set of student permissions.

      @precondition: isinstance(value, StudentPermissions) == True

      @postcondition: self._permissions == value
      """
      pass


class StudentPermissions(object):
   """
   StudentPermissions has various access rights to tools that the student can use.

   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar _presPermLevel: A student's PermissionLevel for presentation and layer interactions.
   @ivar _canRaiseHand: Boolean indicating if a student is allowed to raise their hand and ask a question.
   @ivar _canPushLayer: Boolean indicating if a student is allowed to push a layer to the presenter's stack.
   """

   def __init__(self, presPermLevel, canRaiseHand, canPushLayer):
      """
      Initialize a StudentPermissions object.

      @param presPermLevel: A presentaton PermissionLevel for a student.
      @param canRaiseHand: Boolean indicating if a student is allowed to raise their hand and ask a question.
      @param canPushLayer: Boolean indicating if a student is allowed to push a layer to the presenter's stack.
      """
      pass

   @property
   def presPermLevel(self):
      """
      Get the student's current presentation PermissionLevel.
      """
      pass

   @presPermLevel.setter
   def presPermLevel(self, value):
      """
      Set the student's PermissionLevel with a new PermissionLevel.

      @param value: The new PermissionLevel

      @precondition: isinstance(value, PermissionLevel) == True

      @postcondition: self._presPermLevel == value
      """
      pass

   @property
   def canRaiseHand(self):
      """
      Get the student's current permission for raising their hand.
      """
      pass

   @canRaiseHand.setter
   def canRaiseHand(self, value):
      """
      Set the student's ability to raise their hand.

      @param value: A boolean value

      @precondition: value == True or value == False

      @postcondition: self._canRaiseHand == value
      """
      pass

   @property
   def canPushLayer(self):
      """
      Get the student's current permission for pushing a layer.
      """
      pass

   @canPushLayer.setter
   def canPushLayer(self, value):
      """
      Set the student's ability to push a layer to the presenter's stack.

      @param value: A boolean value

      @precondition: value == True or value == False

      @postcondition: self._canPushLayer == value
      """
      pass
