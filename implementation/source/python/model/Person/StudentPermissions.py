import sys
sys.path.insert(0, '../Presentation')

from Presentation.PermissionLevel import PermissionLevel

class StudentPermissions(object):

   def __init__(self, presPermLevel = PermissionLevel.Normal,
      canRaiseHand = True, canPushLayer = True
   ):
      self.presPermLevel = presPermLevel
      self.canRaiseHand = canRaiseHand
      self.canPushLayer = canPushLayer

   def GetPresPermLevel(self):
      print('From StudentPermissions.GetPresPermLevel()')
      return self.presPermLevel

   def SetPresPermLevel(self, value):
      print('From StudentPermissions.SetPresPermLevel()')
      self.presPermLevel = value

   def CanRaiseHand(self):
      print('From StudentPermissions.CanRaiseHand()')
      return self.canRaiseHand

   def SetCanRaiseHand(self, value):
      print('From StudentPermissions.SetCanRaiseHand()')
      self.canRaiseHand = value

   def CanPushLayer(self):
      print('From StudentPermissions.CanPushLayer()')
      return self.canPushLayer

   def SetCanPushLayer(self, value):
      print('From StudentPermissions.SetCanPushLayer()')
      self.canPushLayer = value
