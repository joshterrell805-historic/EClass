from datetime import datetime
import time

class Message:
   def __init__(self, name, time, text):
      self.name = name
      self.time = time #datetime object
      self.text = text

   def ToString(self):
      return self.name + " " + "[" + self.time.strftime('%m/%d/%Y %I:%M %p') + "]" + ": " + self.text

   def toDict(self):
      return {
         'name' : self.name,
         'time' : time.mktime(self.time.timetuple()), #seconds since epoch (float)
         'text' : self.text
      }

   @staticmethod
   def fromDict(d):
      print d['time']
      return Message(
         d['name'],
         datetime.fromtimestamp(d['time']),
         d['text']
      )
