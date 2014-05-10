import unittest
import sys

sys.path.insert(0, '../../../../implementation/source/python/model')
from Connection import Connection

import wx # needed for Conneciton.__loop, see bottom

class ConnectionTest(unittest.TestCase):

   def test_getInstance(self):
      """
      Verify that the instance returned is indeed a singleton and that it is
      an instance of the Connection class.
      """
      instance = Connection.getInstance();
      otherInstance = Connection.getInstance();
      self.assertIs(instance, otherInstance);
      self.assertIsInstance(instance, Connection);

   @staticmethod
   def tearDownClass():
      app.Exit()

if __name__ == '__main__':
   # Due to not figuring out a better solution, we actually need wx python here
   # in the model. We don't want every view to be responsible for using
   # wx.FutureCall, so we assume that every caller of Connection is from the wx
   # thread. This problem originated from having two event queues, one for wx
   # python and one for twisted. Each event queue is blocking so it needs its
   # own thread. We could also solve this by launching two separate applications
   # (two processes) and use pipes to communicate between the processes.. I
   # actually think that might be the better solution for industry but for
   # this project we just want something that works, and this works.
   app = wx.App(False)
   f = wx.Frame(None)
   wx.FutureCall(1, unittest.main)
   app.MainLoop()
