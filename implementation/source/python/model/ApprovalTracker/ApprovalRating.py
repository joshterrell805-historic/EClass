class ApprovalRating:
   
   def __init__(self):
      pass

   def setValue(self, percent):
      self._rating = percent
      print "In ApprovalRating.setValue: ", percent

   def getValue(self):
      print "In ApprovalRating.getValue"

      # this can easily be changed to be something other than a percentage
      #  if we want to display between say, -10 and 10
      return self._rating
