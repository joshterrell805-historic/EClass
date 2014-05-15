class Roster:
   def __init__(self):
      self.students = ["Carson Carroll", 
      "Tim Anderson", 
      "Ryan Ginsberg", 
      "Mike Sevilla", 
      "Alexa Fox", 
      "Kelsey Hansen", 
      "Emilio Cavazon", 
      "Jared Osborn", 
      "Kevin Wiebe", 
      "Alek Squires", 
      "John Hanna", 
      "Haylee Springer"]

   def AddNewStudent(self):
      print('From Roster.AddNewStudent()')

   def RemoveStudent(self):
      print('From Roster.RemoveStudent()')

   def SortList(self, list):
      list.sort()
   
   def GetRoster(self):
      return self.students
