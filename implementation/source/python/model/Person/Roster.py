class Roster:
   def __init__(self):
      self.students = ["Carson Carroll", "Tim Anderson", "Ryan Ginsberg", "Mike Sevilla", "Alexa Fox", "Kelsey Hansen", "Emilio Cavazos", "Jared Osborn", "Kevin Wiebe", "Alek Squires", "John Hanna", "Haylee Springer"]
      print("Students (in class) listed before being sorted:")
      for i in range(0, len(self.students)):
         print(self.students[i])
      self.SortList(self.students)
      self.remoteList = ["Josh Terrell", "Kevin Le", "Joel Wilcox"]
      print("Students (remote access) listed before being sorted:")
      for j in range(0, len(self.remoteList)):
         print(self.remoteList[j])
      self.SortList(self.remoteList)

   def AddNewStudent(self):
      print('From Roster.AddNewStudent()')

   def RemoveStudent(self):
      print('From Roster.RemoveStudent()')

   def SortList(self, list):
      list.sort()
   
   def GetRoster(self):
      return self.students + self.remoteList
