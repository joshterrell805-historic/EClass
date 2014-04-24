class Presentation:
   
   def __init__(self, path):
      self.slides = []
      self.SetPath(path)
      self.slideNum = 0

   def MoveToNextSlide(self):
      if self.slideNum < len(self.slides) - 1:
         self.slideNum += 1

   def MoveToPreviousSlide(self):
      if self.slideNum != 0:
         self.slideNum -= 1

   def MoveToSlide(self, slideNum):
      if slideNum > 0 and slideNum <= len(self.slides):
         self.slideNum = slideNum - 1

   # TODO implement this when we have a way to check the presenter's slide from
   # the student's client
   def SyncWithPresenter(self):
      print('From Presentation.SyncWithPresenter')

   def SetPath(self, path):
      # TODO I don't think we should allow path to be None
      # (I think it should be in our precondition that path must be a valid
      # path to an html file)
      # This check is redundant anyway since we set path to None when
      # we're given None
      if path != None:
         self.path = path
      else:
         self.path = None

   def GetPath(self):
      print('From Presentation.GetPath(): ' + self.path)
      return self.path

   def GetSlideNum(self):
      return self.slideNum + 1

   # TODO add documentation (Joel)
   def GetSlide(self):
      return self.slides[self.slideNum]

   # TODO add documentation (Joel)
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
                  self.slides.append(slide)
                  slide = '' + slideBase

               else:
                  slide += line
            else:
               slideBase += line
               if line.find('<body>'):
                  inBody = True
                  slide += slideBase
               
