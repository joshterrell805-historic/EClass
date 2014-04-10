class Person:

   def __init__(self, username, password):
      self.username = username
      self.password = password

   def Login(self):
      print('From Person.Login(): ' + self.username + ' ' + self.password)
