from Person.Question import Question

class QuestionList():
   def __init__(self):
      self.questions = []
   
   def Append(self, question):
      self.questions.append(question)

   def Remove(self, index):
      self.questions.pop(index).GetText()

   def RemoveAll(self):
      self.questions[:] = []

   def __getitem__(self, index):
      return self.questions[index].GetText() 
