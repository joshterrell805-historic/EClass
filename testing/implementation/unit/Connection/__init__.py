import unittest
import sys, time, subprocess

sys.path.insert(0, '../../../implementation/source/python/model')
from Connection import Connection

import wx # needed for Conneciton.__loop, see bottom

class GetInstanceTest(unittest.TestCase):
   @staticmethod
   def customSetup(onReady):
      onReady()
   @staticmethod
   def customTeardown():
      pass
   def test_getInstance(self):
      """
      Verify that the instance returned is indeed a singleton and that it is
      an instance of the Connection class.
      """
      instance = Connection.getInstance();
      otherInstance = Connection.getInstance();
      self.assertIs(instance, otherInstance);
      self.assertIsInstance(instance, Connection);

class AuthFailTest(unittest.TestCase):
   @staticmethod
   def customSetup(onReady):
      c = AuthFailTest
      c.centralProcess = subprocess.Popen(['python', 'Connection/launchCC.py'])

      time.sleep(1)
      def onResponse(response):
         c.response = response;
         onReady()

      c.con = Connection.getInstance()
      c.con.authenticate('invalid username', 'asdf', onResponse)
      
   @staticmethod
   def customTeardown():
      c = AuthFailTest
      Connection.__instance = None
      c.centralProcess.kill()
      time.sleep(1)
   def test_authFail(self):
      """
      Verify that the cc throws error on bad username/password
      """
      c = AuthFailTest
      self.assertFalse(c.response.success)

class AuthSuccessTest(unittest.TestCase):
   @staticmethod
   def customSetup(onReady):
      c = AuthSuccessTest
      c.centralProcess = subprocess.Popen(['python', 'Connection/launchCC.py'])

      time.sleep(1)
      def onResponse(response):
         c.response = response;
         onReady()

      c.con = Connection.getInstance()
      c.con.authenticate('student', 'asdf', onResponse)
      
   @staticmethod
   def customTeardown():
      c = AuthSuccessTest
      Connection.__instance = None
      c.centralProcess.kill()
      time.sleep(1)
   def test_authSuccess(self):
      """
      Verify that the cc allows valid username/password
      """
      c = AuthSuccessTest
      self.assertTrue(c.response.success)

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

   classes = []
   classes.append(GetInstanceTest)
   classes.append(AuthFailTest)
   classes.append(AuthSuccessTest)

   frame = wx.Frame(None)
   frame.SetLabel('Temporary but needed window for connection tests.')
   # tests don't work on mac without.. for wx.FutureCall to work, a window
   # must be active (mac only)
   frame.visible = True
   frame.firstTime = True

   def hideWindow(evt):
      if frame.visible:
         frame.visible = False
         frame.Hide()
   def startTests(evt):
      if frame.firstTime:
         nextTest()
         frame.firstTime = False
   def nextTest():
      if len(classes) == 0:
         #oh the hacks.. oh the horror
         Connection.getInstance().close()
         app.Exit()
      else:
         c = classes.pop()
         test = unittest.TestLoader().loadTestsFromTestCase(c)
         def onReady():
            unittest.TextTestRunner(verbosity=2).run(test)
            c.customTeardown()
            wx.FutureCall(0.01, nextTest)
         c.customSetup(onReady)
   app.Bind(wx.EVT_ACTIVATE_APP, startTests);
   app.Bind(wx.EVT_SHOW, hideWindow);

   frame.Show()
   app.MainLoop()
