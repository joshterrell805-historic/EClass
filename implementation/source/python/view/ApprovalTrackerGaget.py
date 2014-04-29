import wx
import sys

sys.path.insert(0, 'model')

from ApprovalTracker.ApprovalRating import ApprovalRating
from EClass import EClass
from Person.Presenter import Presenter

class ApprovalTrackerGaget(wx.Frame):
   
   # **display** values
   minVal = 0
   maxVal = 10

   def __init__(self, parent):
      
      super(ApprovalTrackerGaget, self).__init__(
         None, -1, "A.T.G.", size = (60, 150)
      )

      self.parent = parent

      slider = wx.Slider(self,
         minValue = ApprovalTrackerGaget.minVal,
         maxValue = ApprovalTrackerGaget.maxVal,
         style = wx.SL_VERTICAL | wx.SL_INVERSE
      )
      self.slider = slider

      if isinstance(EClass.GetInstance().user, Presenter):
         slider.Enable(False)

         EClass.GetInstance().user.approvalRating.AddListener(
            self.OnValueChanged
         )

         # TODO remove this.. this is just so we can see the event in action
         EClass.GetInstance().user.approvalRating.SetValue(0.8)

      else:
         slider.Enable(True)
         slider.SetValue(
            (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal) / 2
         )

         ApprovalTrackerGaget.SetApprovalRating(slider.GetValue())

         self.Bind(wx.EVT_SCROLL, self.OnSlide)
      
      self.Bind(wx.EVT_CLOSE, self.onClose)

   def OnSlide(self, event):
      ApprovalTrackerGaget.SetApprovalRating(event.GetPosition())

   def OnValueChanged(self):
      percent = EClass.GetInstance().user.approvalRating.GetValue()

      self.slider.SetValue(
         ApprovalTrackerGaget.minVal +
         percent * (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal)
      )


   @staticmethod
   def SetApprovalRating(rating):
      # pre -- rating is between minVal and maxVal

      valAsPercent = (
         (float)(rating - ApprovalTrackerGaget.minVal)
            /
         (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal)
      )

      user = EClass.GetInstance().user
      user.approvalRating.SetValue(valAsPercent)

   def onClose(self, event):
      self.parent.showApprovalTrackerMenuItem.Check(False)
      self.Hide()


# For testing.. this is only run if the file is ran directly.
if __name__ == "__main__":
   app = wx.App(False)
   EClass.GetInstance().Login('student', 'asdf')
   ApprovalTrackerGaget()
   app.MainLoop()
