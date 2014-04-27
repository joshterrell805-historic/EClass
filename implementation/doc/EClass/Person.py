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
   @ivar question: The student's current question (if any)
   @ivar pushedLayer: The student's current pushed layer (if any)
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

   def SetPermissions(self, permissions):
      """
      Set the student's permissions with a new StudentPermissions object.

      @param permissions: The new set of student permissions.

      @precondition: isinstance(permissions, StudentPermissions) == True

      @postcondition: self.permissions == permissions
      """
      pass
      
   def IsPresent(self):
      """
      Indicate if the student is present.
      
      @return: self.present
      """
      pass
      
   def SetPresent(self, value):
      """
      Set whether or not the student is present.
      
      @param value: A boolean value
      
      @postcondition: self.present == value
      """
      pass
      
   def IsKicked(self):
      """
      Indicate if the student has been kicked.
      
      @return: self.kicked
      """
      pass
      
   def SetKicked(self, value):
      """
      Set the student's kicked status.
      
      @param value: A boolean value
      
      @postcondition: self.kicked == value
      """
      pass
      
   def HasQuestion(self):
      """
      Indicate if the student currently has a question.
      
      @return: True when there is a question and False otherwise
      """
      pass
      
   def GetQuestion(self):
      """
      Get the student's current question.
      
      @return: self.question
      """
      pass
      
   def SetQuestion(self, question):
      """
      Set the student's current question.
      
      @param question: The new Question
      
      @precondition: isinstance(question, Question)
      
      @postcondition: self.question == question
      """
      pass
         
   def GetPushedLayer(self):
      """
      Get the student's pushed layer.
      
      @return: self.pushedLayer
      """
      pass
      
   def SetPushedLayer(self, layer):
      """
      Set the student's pushed layer.
      
      @param layer: The new Layer to push
      
      @precondition: isinstance(layer, Layer)
      
      @postcondition: self.pushedLayer == layer
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

class Roster:
   """
   A Roster contains all of the students in the class and methods to manage the students.

   @author: Carson Carroll (ccarro03@calpoly.edu)

   @ivar students: The list of students in the class.
   """

   def __init__(self, students):
      """
      Builds an instance of a roster.

      @param self: self is the instance of this object.
      @param students: A list of students in the class.
      """
      pass

   def AddNewStudent(self, student):
      """
      Takes a student and adds them to the roster.

      @param student: The student who is to be added to the roster.

      @precondition: student != None and !self.students.contains(student)

      @postcondition: students.contains(student) == true
      """
      pass

   def RemoveStudent(self, student):
      """
      Takes a student and removes them from the roster.

      @param student: The student who is to be removed from the roster.

      @precondition: student != None and self.student.contains(student)

      @postcondition: !self.students.contains(student) and self.students.contains(student) == false
      """
      pass

class RosterItem:
   """
   A RosterItem contains an individual student's first and last name as long as buttons for 
   student question asking, pushing layers, and permission setting.

   @author: Carson Carroll (ccarro03@calpoly.edu)

   @ivar student: The student the RosterItem represents.
   """

   def __init__(self, student):
      """
      Builds an instance of a RosterItem.

      @param self: self is the instance of this object.
      @param student: A student for the RosterItem to represent.
      """
      pass

   def Hand(self):
      """
      Allows a student to ask a question.
      """
      pass

   def Layers(self):
      """
      Allows a student to push private layers.
      """
      pass

 
class Question(object):
   """
   Question is a container for the text and time created of a Student's question.

   @author: Joel Wilcox (jnwilcox@calpoly.edu)

   @ivar text: The Question's text
   @ivar timeCreated: When the Question was created
   """
 
   def __init__(self, questionText, timeCreated):
      """
      Initialize a Question object.

      @param questionText: A string to initialize the question with
      @param timeCreated: The time when the Question was created (Current time if none is given)
      """
      pass

   def GetText(self):
      """
      Get the Question's text.
      
      @return: self.text
      """
      pass
      
   def GetTime(self):
      """
      Get the Question's creation time.
      
      @return: self.timeCreated
      """
      pass
      