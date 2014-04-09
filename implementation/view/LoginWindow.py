import wx

class LoginWindow(wx.Frame):
   
   def __init__(self, onSuccess, onCancel):
      super(LoginWindow, self).__init__(None, -1, 'Login')

      sizer = wx.BoxSizer(wx.VERTICAL)

      usernameTextbox = wx.TextCtrl(self)
      sizer.Add(usernameTextbox)

      passwordTextbox = wx.TextCtrl(self, style = wx.TE_PASSWORD)
      sizer.Add(passwordTextbox)

      button = wx.Button(self, label = 'Login')
      button.Bind(wx.EVT_BUTTON, onSuccess)
      sizer.Add(button)

      button = wx.Button(self, label = 'Cancel')
      button.Bind(wx.EVT_BUTTON, onCancel)
      sizer.Add(button)

      self.SetSizer(sizer)
