import wx
import sys
sys.path.insert(0, '../model')

from Person.Student import Student
from Presentation.PermissionLevel import PermissionLevel

class PermissionsWindow(wx.Frame):
   
   def __init__(self, student):

      super(PermissionsWindow, self).__init__(None, -1, 'Permissions: Temp Name')
      self.SetBackgroundColour('#FFFFFF')
      
      self.student = student

      self.radioUnrestricted = wx.RadioButton(self, label = 'Unrestricted',
         style = wx.RB_GROUP
      )
      self.radioNormal = wx.RadioButton(self, label = 'Normal')
      self.radioLockdown = wx.RadioButton(self, label = 'Lockdown')
      self.checkRaiseHand = wx.CheckBox(self, label = 'Raise hand/Ask question')
      self.checkPushLayer = wx.CheckBox(self,
         label = 'Push a layer to the public stack'
      )

      sizer = wx.BoxSizer(wx.VERTICAL)
      whiteboardSizer = wx.BoxSizer(wx.VERTICAL) # For whiteboard permissions
      requestsSizer = wx.BoxSizer(wx.VERTICAL)
      buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)

      whiteboardSizer.AddStretchSpacer(2)
      whiteboardSizer.Add(wx.StaticText(self, label = 'Whiteboard'), 2)
      whiteboardSizer.Add(self.radioUnrestricted, 1, wx.ALIGN_TOP)
      whiteboardSizer.Add(self.radioNormal, 1, wx.ALIGN_TOP)
      whiteboardSizer.Add(self.radioLockdown, 1, wx.ALIGN_TOP)
      whiteboardSizer.AddStretchSpacer(2)

      requestsSizer.AddStretchSpacer(2)
      requestsSizer.Add(wx.StaticText(self, label = 'Requests/Interactions'), 2)
      requestsSizer.Add(self.checkRaiseHand, 1, wx.ALIGN_TOP)
      requestsSizer.Add(self.checkPushLayer, 1, wx.ALIGN_TOP)
      requestsSizer.AddStretchSpacer(2)

      acceptButton = wx.Button(self, label = 'Accept')
      acceptButton.Bind(wx.EVT_BUTTON, self.OnAccept)
      buttonsSizer.AddStretchSpacer(2)
      buttonsSizer.Add(acceptButton, 1, wx.ALIGN_CENTER)

      cancelButton = wx.Button(self, label = 'Cancel')
      cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)
      buttonsSizer.Add(cancelButton, 1, wx.ALIGN_CENTER)
      buttonsSizer.AddStretchSpacer(2)

      sizer2 = wx.BoxSizer(wx.HORIZONTAL)
      sizer2.AddStretchSpacer(1)
      sizer2.Add(whiteboardSizer, 1, wx.ALIGN_TOP)
      sizer2.Add(requestsSizer, 1, wx.ALIGN_TOP)
      sizer2.AddStretchSpacer(1)

      sizer.AddStretchSpacer(1)
      sizer.Add(sizer2)
      sizer.Add(buttonsSizer)
      sizer.AddStretchSpacer(1)

      sizer.SetMinSize(size = (500, 300))
      self.SetSizer(sizer)
      self.Show()

   def OnAccept(self, event):
      perms = self.student.GetPermissions()
      
      if self.radioUnrestricted.GetValue() == True:
         perms.SetPresPermLevel(PermissionLevel.Unrestricted)
      elif self.radioLockdown.GetValue() == True:
         perms.SetPresPermLevel(PermissionLevel.Lockdown)
      else:
         perms.SetPresPermLevel(PermissionLevel.Normal)

      perms.SetCanRaiseHand(self.checkRaiseHand.GetValue())
      perms.SetCanPushLayer(self.checkPushLayer.GetValue())
      self.Destroy()
      
   def OnCancel(self, event):
      self.Destroy()

if __name__ == '__main__':
  
    app = wx.App()
    PermWin = PermissionsWindow(Student('blah', 'blahhh'))
    app.MainLoop()
