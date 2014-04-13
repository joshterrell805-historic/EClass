import sys
sys.path.insert(0, '../enum')

from enum import Enum

class PermissionLevel(Enum):
   Unrestricted = 1
   Normal = 2
   Lockdown = 3
