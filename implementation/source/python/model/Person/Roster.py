class Roster:
   def __init__(self):
      self.students = ["Carson Carroll", "Tim Anderson", "Ryan Ginsberg", "Mike Sevilla", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
      self.SortList(self.students)
      self.remoteList = ["Josh Terrell", "Kevin Le", "Joel Wilcox"]
      self.SortList(self.remoteList)

   def AddNewStudent(self):
      print('From Roster.AddNewStudent()')

   def RemoveStudent(self):
      print('From Roster.RemoveStudent()')

   def SortList(self, list):
      list.sort()