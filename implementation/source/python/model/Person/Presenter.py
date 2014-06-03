from Person import Person

class Presenter(Person):

   def __init__(self, username, password):
      super(Presenter, self).__init__(username, password)
      self.hostedClass = None
