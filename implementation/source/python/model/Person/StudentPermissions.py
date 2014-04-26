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
      return self.presPermLevel

   def SetPresPermLevel(self, value):
      self.presPermLevel = value

   def CanRaiseHand(self):
      return self.canRaiseHand

   def SetCanRaiseHand(self, value):
      self.canRaiseHand = value

   def CanPushLayer(self):
      return self.canPushLayer

   def SetCanPushLayer(self, value):
      self.canPushLayer = value
