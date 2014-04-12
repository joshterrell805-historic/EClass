from Person import Person

class Student(Person):

   def __init__(self, username, password):
      super(Student, self).__init__(username, password)
