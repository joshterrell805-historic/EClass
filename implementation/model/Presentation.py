class Presentation:
   
   def __init__(self, path):
      self.path = path
      
   def ShowPresentation(self):
      print('From Presentation.ShowPresentation(): ' + self.path)

   def MoveToNextSlide(self):
      print('From Presentation.MoveToNextSlide()')

   def MoveToPreviousSlide(self):
      print('From Presentation.MoveToPreviousSlide()')

   def MoveToSlide(self, slideNum):
      print('From Presentation.MoveToSlide()')

   def SyncWithPresenter(self):
      print('From Presentation.SyncWithPresenter')
