from Slide import Slide
from Layer import Layer

class Presentation:
   
   def __init__(self, path):
      self.slides = []
      self.SetPath(path)
      self.currSlideNum = 0

   def MoveToNextSlide(self):
      if self.currSlideNum < len(self.slides) - 1:
         self.currSlideNum += 1
         return True
      else:
         return False

   def MoveToPreviousSlide(self):
      if self.currSlideNum != 0:
         self.currSlideNum -= 1
         return True
      else:
         return False

   def MoveToSlide(self, slideNum):
      if slideNum > 0 and slideNum <= len(self.slides):
         self.currSlideNum = slideNum - 1
         return True
      else:
         return False

   # TODO implement this when we have a way to check the presenter's slide from
   # the student's client
   def SyncWithPresenter(self):
      print('From Presentation.SyncWithPresenter()')

   def SetPath(self, path):
      self.path = path

   def GetPath(self):
      return self.path

   def GetSlideNum(self):
      return self.currSlideNum + 1

   def GetSlide(self):
      return self.slides[self.currSlideNum]

   def Slidify(self):
      inBody = False
      slideBase = ''
      slideEnd = '</body>\n</html>'
      slide = ''
      
      with open(self.path) as html:
         for line in html:
            if inBody:

               # Check if there is a slide break or the end of the body
               if (line.find('<br class="slide">') != -1 or
                   line.find('<br class=slide>') != -1 or
                   line.find('</body>') != -1
               ):
                  slide += slideEnd
                  self.slides.append(Slide(slide, [Layer("Background", 255, False)]))
                  slide = '' + slideBase

               else:
                  slide += line
            else:
               slideBase += line
               if line.find('<body>'):
                  inBody = True
                  slide += slideBase
               
