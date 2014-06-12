import unittest
import sys, time, subprocess

sys.path.insert(0, '../../../implementation/source/python/model')
from Connection import Connection

import wx # needed for Conneciton.__loop, see bottom

# ConnectionTest tests the Connection model (defined in model/Connection/__init__.py)
# It implements the following test plan:
#
# Phase 1: Unit test the singleton access method, getInstance(), and by
#  inclusion, the constructor.
# Phase 2: Unit test authentication with the central server.
# Phase 3: Unit test hosting a presentation.
# Phase 4: Unit test joining a presentation.
# Phase 5: Unit test leaving a presentation.
# Phase 5: Unit test various presenter/client mid-presentation communications.
#  * initial data sent to client upon joining
#  * sync data sent to student as presenter navigates slides
#  * forum messages sent and received from and to presenter/student(s)
#  * kick presentation message and resulting closed connection
#  * layer objects synced from presenter to student as presenter draws
#  * ...much more...
#
# Note: Due to the way connections work (asynchronously), the following
#  tests are structured quite differently (as a class per test).
#  Python's unittest framework has zero support for asynchronous testing.


# Unit test getInstance()
#
# Test
# Case  Input                      Output                               Remarks
# =============================================================================
# 1     self.__instance == None    self.__instance != None    
# 2     self.__instance != None    self.__instance == old(self.__instance)
#
class GetInstanceTest(unittest.TestCase):
   @staticmethod
   def customSetup(onReady):
      onReady()
   @staticmethod
   def customTeardown():
      Connection._Connection__instance = None
      pass
   def test_getInstance(self):
      """
      Verify that the instance returned is indeed a singleton and that it is
      an instance of the Connection class.
      """
      # connection.__instance == connection._Connection__instance
      # python name mangling x.x
      # https://docs.python.org/2/reference/expressions.html#atom-identifiers
      self.assertIs(Connection._Connection__instance, None)
      instance = Connection.getInstance();
      self.assertIs(Connection._Connection__instance, instance)
      otherInstance = Connection.getInstance();
      self.assertIs(Connection._Connection__instance, instance)
      self.assertIs(instance, otherInstance);
      self.assertIsInstance(instance, Connection);

# Unit test 
#
# Test
# Case  Input                      Output                               Remarks
# =============================================================================
# 1     self.__instance == None    self.__instance != None    
# 2     self.__instance != None    self.__instance == old(self.__instance)
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
      Connection._Connection__instance = None
      c.centralProcess.kill()
      time.sleep(1)
   def test_authFail(self):
      """
      Verify that central throws error on bad username/password
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
      Connection._Connection__instance = None
      c.centralProcess.kill()
      time.sleep(1)
   def test_authSuccess(self):
      """
      Verify that central allows valid username/password
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

   def nextTest():
      if len(classes) == 0:
         #oh the hacks.. oh the horror
         Connection.getInstance().close()
         app.Exit()
      else:
         c = classes.pop(0)
         test = unittest.TestLoader().loadTestsFromTestCase(c)
         def onReady():
            unittest.TextTestRunner(verbosity=2).run(test)
            c.customTeardown()
            wx.FutureCall(1, nextTest)
         c.customSetup(onReady)

   wx.FutureCall(1, nextTest)
   app.MainLoop()
