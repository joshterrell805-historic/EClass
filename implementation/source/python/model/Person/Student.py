from Person import Person

from ApprovalTracker.ApprovalRating import ApprovalRating

class Student(Person):

   def __init__(self, username, password):
      super(Student, self).__init__(username, password)

      self.approvalRating = ApprovalRating()
