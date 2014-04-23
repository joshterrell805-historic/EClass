class Presentation:
   
   def __init__(self, path):
      self.SetPath(path)
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
      # TODO I don't think we should allow path to be None
      # (I think it should be in our precondition that path must be a valid
      # path to an html file)
      if path != None:
         self.path = "file://" + path
      else:
         self.path = None

   def GetPath(self):
      print('From Presentation.GetPath(): ' + self.path)
      return self.path

   def GetSlideNum(self):
      print('From Presentation.GetSlideNum()')
      return self.slideNum

   
