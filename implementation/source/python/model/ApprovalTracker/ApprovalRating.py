class ApprovalRating:
   
   def __init__(self):
      self.__listeners = []

   def SetValue(self, percent):
      self.__rating = percent
      print "In ApprovalRating.SetValue: ", percent

      # post an event to listeners, if there are any
      for listener in self.__listeners:
         listener()

   def GetValue(self):
      print "In ApprovalRating.GetValue", self.__rating

      # this can easily be changed to be something other than a percentage
      # if we want to display between say, min and max
      #  self._rating * (max - min) + min

      return self.__rating

   def AddListener(self, listener):
      self.__listeners.append(listener)
