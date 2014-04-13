class ApprovalRating:
   
   def __init__(self):
      self.listeners = []

   def setValue(self, percent):
      self._rating = percent
      print "In ApprovalRating.setValue: ", percent

      # post an event to listeners, if there are any
      for listener in self.listeners:
         listener()

   def getValue(self):
      print "In ApprovalRating.getValue", self._rating

      # this can easily be changed to be something other than a percentage
      # if we want to display between say, min and max
      #  self._rating * (max - min) + min

      return self._rating

   def addSetValueListener(self, listener):
      self.listeners.append(listener)
