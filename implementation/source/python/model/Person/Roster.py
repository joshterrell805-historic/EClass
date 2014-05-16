class Roster:
   def __init__(self):
      self.students = ["Carson Carroll", 
      "Tim Anderson", 
      "Ryan Ginsberg", 
      "Mike Sevilla", 
      "Alexa Fox", 
      "Kelsey Hansen", 
      "Emilio Cavazos", 
      "Jared Osborn", 
      "Kevin Wiebe", 
      "Alek Squires", 
      "John Hanna", 
      "Haylee Springer"]
      self.SortList(self.students)
      """
      self.sObjs = [Student("Alek Squires", "")],
      Student("Alexa Fox", ""),
      Student("Carson Carroll", ""),
      Student("Emilio Cavazos", ""),
      Student("Haylee Springer", ""),
      Student("Jared Osborn", ""),
      Student("John Hanna", ""),
      Student("Kelsey Hansen", ""),
      Student("Kevin Wiebe", ""),
      Student("Mike Sevilla", ""),
      Student("Ryan Ginsberg", ""),
      Student("Tim Anderson", "")]"""

   def AddNewStudent(self):
      print('From Roster.AddNewStudent()')

   def RemoveStudent(self):
      print('From Roster.RemoveStudent()')

   def SortList(self, list):
      list.sort()
   
   def GetRoster(self):
      return self.students
