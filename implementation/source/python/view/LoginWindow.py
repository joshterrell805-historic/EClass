import wx
import sys

from EClassWindow import EClassWindow

sys.path.insert(0, 'model')
from EClass import EClass

class LoginWindow(wx.Frame):
   
   def __init__(self):

      no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER
         | wx.RESIZE_BOX | wx.MAXIMIZE_BOX | wx.CLOSE_BOX
      )

      super(LoginWindow, self).__init__(None, -1, 'Login', 
         style = no_resize | wx.TAB_TRAVERSAL
      )

      sizer = wx.BoxSizer(wx.VERTICAL)
      usernameHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
      passwordHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
      buttonsHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

      self.usernameTextbox = wx.TextCtrl(self)
      usernameHorizontalSizer.AddStretchSpacer(2)
      usernameHorizontalSizer.Add(wx.StaticText(self, label = 'Username: '), 2)
      usernameHorizontalSizer.Add(self.usernameTextbox, 1, wx.ALIGN_CENTER)
      usernameHorizontalSizer.AddStretchSpacer(2)

      self.passwordTextbox = wx.TextCtrl(self, style = wx.TE_PASSWORD)
      passwordHorizontalSizer.AddStretchSpacer(2)
      passwordHorizontalSizer.Add(wx.StaticText(self, label = 'Password:  '), 2)
      passwordHorizontalSizer.Add(self.passwordTextbox, 1, wx.ALIGN_CENTER)
      passwordHorizontalSizer.AddStretchSpacer(2)

      button = wx.Button(self, label = 'Login')
      button.Bind(wx.EVT_BUTTON, self.OnAttempt)
      buttonsHorizontalSizer.AddStretchSpacer(2)
      buttonsHorizontalSizer.Add(button, 1, wx.ALIGN_CENTER)

      button = wx.Button(self, label = 'Cancel')
      button.Bind(wx.EVT_BUTTON, self.OnCancel)
      buttonsHorizontalSizer.Add(button, 1, wx.ALIGN_CENTER)
      buttonsHorizontalSizer.AddStretchSpacer(2)

      sizer.AddStretchSpacer(1)
      sizer.Add(usernameHorizontalSizer)
      sizer.Add(passwordHorizontalSizer)
      sizer.AddStretchSpacer(1)
      sizer.Add(buttonsHorizontalSizer)

      sizer.SetMinSize(size = (1000,1000))
      self.SetSizer(sizer)

      self.Show()

   def GetUsername(self):
      return self.usernameTextbox.GetValue()

   def GetPassword(self):
      return self.passwordTextbox.GetValue()

   def OnAttempt(self, event):
      username = self.GetUsername()
      password = self.GetPassword()
      EClass.GetInstance().Login(username, password)

      if EClass.GetInstance().user:
         self.OnSuccess()

   def OnSuccess(self):
      self.Close()
      EClassWindow()

   def OnCancel(self, event):
      sys.exit()
