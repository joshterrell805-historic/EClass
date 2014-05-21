import unittest
from datetime import datetime
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Forum')

from Forum import Forum
from Message import Message

class ForumTest(unittest.TestCase):

   def setUp(self):
      self.forum = Forum()
      self.assertEqual(0, len(self.forum.messagesList))

   def test_AddMessage(self):
      time = datetime.now()
      self.forum.AddMessage('carson', time, 'asdf')

      self.assertEqual(1, len(self.forum.messagesList))

      message = self.forum.messagesList[0]

      self.assertEqual('carson', message.name)
      self.assertEqual(time, message.time)
      self.assertEqual('asdf', message.text)

   def test_AddMessageStress(self):
      time = None
      message = None
      for i in range(0, 10000):
         time = datetime.now()
         self.forum.AddMessage('carson' + str(i), time, 'Hello' + str(i))
         message = self.forum.messagesList[i]
         self.assertEqual('carson' + str(i), message.name)
         self.assertEqual(time, message.time)
         self.assertEqual('Hello' + str(i), message.text)

      self.assertEqual(10000, len(self.forum.messagesList))

   def test_ToStringMessage(self):
      time = datetime.now()
      message = Message('carson', time.strftime('%m/%d/%Y %I:%M %p'), "this is a test")
      messageString = message.ToString()
      self.assertEqual("carson [" + time.strftime('%m/%d/%Y %I:%M %p') + "]: this is a test", messageString)


if __name__ == '__main__':
    unittest.main()
