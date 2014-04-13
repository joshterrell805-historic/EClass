from ApprovalTracker.ApprovalRating import ApprovalRating

class Person(object):

   def __init__(self, username, password):
      self.username = username
      self.password = password
      self.approvalRating = ApprovalRating()
