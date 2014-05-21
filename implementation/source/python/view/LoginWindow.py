import wx
import sys

sys.path.insert(0, 'model')
from EClass import EClass

from JoinPresentation import JoinPresentation
from HostPresentation import HostPresentation

class LoginWindow(wx.Frame):
   
   def __init__(self):
      no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER
         | wx.RESIZE_BOX | wx.MAXIMIZE_BOX | wx.CLOSE_BOX
      )

      super(LoginWindow, self).__init__(None, -1, 'Login', 
         style = no_resize | wx.TAB_TRAVERSAL
      )

      self.SetBackgroundColour('#FFEDDB')

      sizer = wx.BoxSizer(wx.VERTICAL)
      titleHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
      usernameHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
      passwordHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)
      buttonsHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

      self.reasonText = wx.StaticText(self, -1)
      self.reasonText.SetForegroundColour((255, 0, 0))

      self.title = wx.StaticText(self, -1, label = '    EClass' + '\n' + 
      'By CREAMS'
      )
      font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
      self.title.SetFont(font)
      titleHorizontalSizer.AddStretchSpacer(2)
      titleHorizontalSizer.Add(self.title, 2)
      titleHorizontalSizer.AddStretchSpacer(2)

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

      sizer.AddStretchSpacer(5)
      sizer.Add(titleHorizontalSizer, 5)
      sizer.AddStretchSpacer(5)
      sizer.Add(usernameHorizontalSizer, 5)
      sizer.AddStretchSpacer(1)
      sizer.Add(passwordHorizontalSizer, 5)
      sizer.AddStretchSpacer(1)
      sizer.Add(buttonsHorizontalSizer)
      sizer.AddStretchSpacer(5)

      self.SetSizer(sizer)

      self.Centre()
      self.Show()

      self.Bind(wx.EVT_CLOSE, self.OnCancel)

   def GetUsername(self):
      return self.usernameTextbox.GetValue()

   def GetPassword(self):
      return self.passwordTextbox.GetValue()

   def OnAttempt(self, event):
      username = self.GetUsername()
      password = self.GetPassword()

      def onSuccess():
         self.OnSuccess()
      def onFailure(reason):
         self.reasonText.SetLabel(reason)
         print(reason)

      EClass.GetInstance().Login(username, password, onSuccess, onFailure)

   def OnSuccess(self):
      self.Hide()

      if EClass.GetInstance().user.isPresenter():
         HostPresentation(self).Show()
      else:
         JoinPresentation(self).Show()

   def OnCancel(self, event):
      EClass.GetInstance().exit()
