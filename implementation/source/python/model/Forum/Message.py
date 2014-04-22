class Message:
   def __init__(self, name, time, text):
      self.name = name
      self.time = time
      self.text = text

   def ToString(self):
      return self.name + " " + "[" + self.time + "]" + ": " + self.text