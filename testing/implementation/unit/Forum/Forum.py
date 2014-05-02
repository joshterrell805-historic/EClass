import unittest
from datetime import datetime
import sys
sys.path.insert(0, '../../../../implementation/source/python/model/Forum')

from Forum import Forum

class ForumTest(unittest.TestCase):

   def setUp(self):
      self.forum = Forum()
      self.assertEqual(0, len(self.forum.messagesStack))

   def test_AddMessage(self):
      time = datetime.now()
      self.forum.AddMessage('carson', time, 'asdfz')

      self.assertEqual(1, len(self.forum.messagesStack))

      message = self.forum.messagesStack[0]

      self.assertEqual('carson', message.name)
      self.assertEqual(time, message.time)
      self.assertEqual('asdf', message.text)


if __name__ == '__main__':
    unittest.main()
