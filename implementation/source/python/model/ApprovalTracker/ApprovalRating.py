class ApprovalRating:
   
   def __init__(self):
      self.listeners = []

   def SetValue(self, percent):
      self._rating = percent
      print "In ApprovalRating.SetValue: ", percent

      # post an event to listeners, if there are any
      for listener in self.listeners:
         listener()

   def GetValue(self):
      print "In ApprovalRating.GetValue", self._rating

      # this can easily be changed to be something other than a percentage
      # if we want to display between say, min and max
      #  self._rating * (max - min) + min

      return self._rating

   def AddListener(self, listener):
      self.listeners.append(listener)
