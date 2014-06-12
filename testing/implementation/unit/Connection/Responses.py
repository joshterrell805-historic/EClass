import unittest
import sys
sys.path.insert(0, '../../../implementation/source/python/model')

from Connection.Responses import *

class ResponsesTest(unittest.TestCase):
   """
   Class ResponseTest is the companion testing class for the
   Connection/Responses module. It implements the following class test-plan:

   Phase 1: Unit Test the Failure Response class of every Response type.
   Phase 2: Unit Test the Success Response class of every Resonse type.
   """

   def test_failureResponses(self):
      """
      Unit test the failure response classes by instantiating every failure
      response class. The response must have `success == false` and `reason =
      whatever is passed to the failure response constructor`.

      Test
      Case  Input                            Output                     Remarks
      =========================================================================
      1     GenericFailure('a')              !r.success && r.reason = 'a'
      2     AuthenticationFailure('b')       !r.success && r.reason = 'b'
      3     HostFailure('c')                 !r.success && r.reason = 'c'
      4     JoinFailure('d')                 !r.success && r.reason = 'd'
      """
      r = GenericFailure('a')
      self.assertIs(r.success, False)
      self.assertEqual(r.reason, 'a')

      r = AuthenticationFailure('b')
      self.assertIs(r.success, False)
      self.assertEqual(r.reason, 'b')

      r = HostFailure('c')
      self.assertIs(r.success, False)
      self.assertEqual(r.reason, 'c')

      r = JoinFailure('d')
      self.assertIs(r.success, False)
      self.assertEqual(r.reason, 'd')

   def test_successResponses(self):
      """
      Unit test the success response classes by instantiating every success 
      response class. The response must have `success == true`. Each success
      class has differing member variables (depicted in the table below).

      Test
      Case  Input                            Output                     Remarks
      =========================================================================
      1     GenericSuccess()                 r.success
      2     AuthenticationSuccess(o, c)      r.success && r.role is o && r.classes is c
      3     HostSuccess()                    r.success
      4     JoinSuccess(d)                   r.success && r.data is d
      """
      r = GenericSuccess()
      self.assertIs(r.success, True)

      o = {'asdf': 'z'}
      c = {'mrrrp' : 'derrp'}
      r = AuthenticationSuccess(o, c)
      self.assertIs(r.success, True)
      self.assertIs(r.role, o)
      self.assertIs(r.classes, c)

      r = HostSuccess()
      self.assertIs(r.success, True)

      d = {'zaphhh' : 'zorks'}
      r = JoinSuccess(d)
      self.assertIs(r.success, True)
      self.assertIs(r.data, d)

if __name__ == "__main__":
   unittest.main()
