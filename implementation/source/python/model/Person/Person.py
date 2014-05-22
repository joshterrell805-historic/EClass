import sys
sys.path.insert(0, '..')
from ApprovalTracker.ApprovalRating import ApprovalRating

class Person(object):

   def __init__(self, username, firstName = 'first', lastName = 'last'):
      self.username = username
      self.firstName = firstName
      self.lastName = lastName
      self.approvalRating = ApprovalRating()

   def isPresenter(self):
      return isinstance(self, Presenter)

# bottom because of circular dependency.
from Presenter import Presenter
