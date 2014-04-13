import sys
sys.path.insert(0, '../Presentation')

from Presentation.PermissionLevel import PermissionLevel

class StudentPermissions(object):

   def __init__(self, presPermLevel = PermissionLevel.Normal,
      canRaiseHand = True, canPushLayer = True
   ):
      self._presPermLevel = presPermLevel
      self._canRaiseHand = canRaiseHand
      self._canPushLayer = canPushLayer

   @property
   def presPermLevel(self):
      print('From StudentPermissions.presPermLevel getter')
      return self._presPermLevel

   @presPermLevel.setter
   def presPermLevel(self, value):
      print('From StudentPermissions.presPermLevel setter')
      self._presPermLevel = value

   @property
   def canRaiseHand(self):
      print('From StudentPermissions.canRaiseHand getter')
      return self._canRaiseHand

   @canRaiseHand.setter
   def canRaiseHand(self, value):
      print('From StudentPermissions.canRaiseHand setter')
      self._canRaiseHand = value

   @property
   def canPushLayer(self):
      print('From StudentPermissions.canPushLayer getter')
      return self._canPushLayer

   @canPushLayer.setter
   def canPushLayer(self, value):
      print('From StudentPermissions.canPushLayer setter')
      self._canPushLayer = value
