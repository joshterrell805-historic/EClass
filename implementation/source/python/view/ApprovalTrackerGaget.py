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
      
      # infinite recurion without this CallLater
      # EClass.GetInstance() -> Forum() ->EClass.GetInstance() ...
      # just wait a sec, then get the instance. Does anyone have a better
      # solution?
      def listen():
         if EClass.GetInstance().user.isPresenter():
            EClass.GetInstance().connection.registerMessageListener(
               'update approval rating', self.onUpdateRating
            )
      wx.CallLater(1, listen)

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

      else:
         slider.Enable(True)
         slider.SetValue(
            (ApprovalTrackerGaget.maxVal - ApprovalTrackerGaget.minVal) / 2
         )

         ApprovalTrackerGaget.SetApprovalRating(slider.GetValue())

         self.Bind(wx.EVT_SCROLL, self.OnSlide)
      
      self.Bind(wx.EVT_CLOSE, self.onClose)

   def OnSlide(self, event):
      rating = ApprovalTrackerGaget.SetApprovalRating(event.GetPosition())
      EClass.GetInstance().connection.send('update approval rating', rating)

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

      return valAsPercent

   def onClose(self, event):
      self.parent.showApprovalTrackerMenuItem.Check(False)
      self.Hide()

   def onUpdateRating(self, message, student):
      # this message should alaways be sent from student to presenter
      assert(student and EClass.GetInstance().user.isPresenter())
      student = EClass.GetInstance().roster.findStudentByUsername(student)

      if student != None:
         def isActive(student):
            return student.present;
         # must use object .. because python
         # count of active ratings
         a = {}
         a['c'] = 0
         def calcTotal(total, student):
            value = student.approvalRating.GetValue()
            if value is not None:
               total += value
               a['c'] += 1
            return total

         student.approvalRating.SetValue(message)
         activeStudents = filter(isActive, EClass.GetInstance().roster.students)
         mean = reduce(calcTotal, activeStudents, 0) / a['c']
         EClass.GetInstance().user.approvalRating.SetValue(mean)


# For testing.. this is only run if the file is ran directly.
if __name__ == "__main__":
   app = wx.App(False)
   EClass.GetInstance().Login('student', 'asdf')
   ApprovalTrackerGaget()
   app.MainLoop()
