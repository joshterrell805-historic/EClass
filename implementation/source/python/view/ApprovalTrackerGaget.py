import wx
import sys

sys.path.insert(0, '../model')
from ApprovalTracker.ApprovalRating import ApprovalRating

class ApprovalTrackerGaget(wx.Frame):
   
   # **display** values
   minVal = 0
   maxVal = 10

   def __init__(self):
      
      super(ApprovalTrackerGaget, self).__init__(
         None, -1, "AT Gaget", size = (60, 150)
      )

      slider = wx.Slider(self,
         style = wx.SL_VERTICAL | wx.SL_LABELS | wx.SL_INVERSE
      )

      slider.SetRange(ApprovalTrackerGaget.minVal, ApprovalTrackerGaget.maxVal)

      slider.SetValue(
         (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal) / 2
      )

      self.Show()
      


# For testing.. this is only run if the file is ran directly.
if __name__ == "__main__":
   app = wx.App(False)
   ApprovalTrackerGaget()
   app.MainLoop()
