import wx
import sys

sys.path.insert(0, 'model')

from ApprovalTracker.ApprovalRating import ApprovalRating
from EClass import EClass

class ApprovalTrackerGaget(wx.Frame):
   
   # **display** values
   minVal = 0
   maxVal = 10

   def __init__(self):
      
      super(ApprovalTrackerGaget, self).__init__(
         None, -1, "A.T.G.", size = (60, 150)
      )

      slider = wx.Slider(self,
         style = wx.SL_VERTICAL | wx.SL_LABELS | wx.SL_INVERSE
      )

      slider.SetRange(ApprovalTrackerGaget.minVal, ApprovalTrackerGaget.maxVal)

      slider.SetValue(
         (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal) / 2
      )

      ApprovalTrackerGaget.SetApprovalRating(slider.GetValue())

      self.Bind(wx.EVT_SCROLL_CHANGED, self.OnSlide)

      self.Show()

   def OnSlide(self, event):
      ApprovalTrackerGaget.SetApprovalRating(event.GetPosition())

   @staticmethod
   def SetApprovalRating(rating):
      # pre -- rating is between minVal and maxVal

      valAsPercent = (
         (float)(rating - ApprovalTrackerGaget.minVal)
            /
         (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal)
      )

      user = EClass.getInstance().user
      user.approvalRating.setValue(valAsPercent)


# For testing.. this is only run if the file is ran directly.
if __name__ == "__main__":
   app = wx.App(False)
   EClass.getInstance().Login('student', 'asdf')
   ApprovalTrackerGaget()
   app.MainLoop()
