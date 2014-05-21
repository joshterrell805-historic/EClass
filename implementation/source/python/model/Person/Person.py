from ApprovalTracker.ApprovalRating import ApprovalRating

class Person(object):

   def __init__(self, username, password):
      self.username = username
      self.password = password
      self.approvalRating = ApprovalRating()

   def isPresenter(self):
      return isinstance(self, Presenter)

# bottom because of circular dependency.
from Presenter import Presenter
