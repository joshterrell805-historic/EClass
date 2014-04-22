class Presentation:
   
   def __init__(self, path):
      path = 
      self.path = path.replace(" " "")
      self.slideNum = 1

   def MoveToNextSlide(self):
      print('From Presentation.MoveToNextSlide()')

   def MoveToPreviousSlide(self):
      print('From Presentation.MoveToPreviousSlide()')

   def MoveToSlide(self, slideNum):
      print('From Presentation.MoveToSlide()')

   def SyncWithPresenter(self):
      print('From Presentation.SyncWithPresenter')

   def SetPath(self, path):
      self.path = path

   def GetPath(self):
      print('From Presentation.GetPath(): ' + self.path)
      return self.path

   def GetSlideNum(self):
      print('From Presentation.GetSlideNum()')
      return self.slideNum

   
