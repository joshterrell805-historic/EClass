import wx
from Slide import Slide
from Layer import Layer
import EClass
import PermissionLevel

class Presentation:
   
   def __init__(self, path):
      self.slides = []
      self.SetPath(path)
      self.currSlideNum = 0
      # infinite recurion without this CallLater
      # EClass.GetInstance() -> Presentation() ->EClass.GetInstance() ...
      # just wait a sec, then get the instance. Does anyone have a better
      # solution?
      def listen():
         EClass.EClass.GetInstance().connection.registerMessageListener(
            'sync current slide', self.OnSync
         )
      wx.CallLater(1, listen)

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

   def SyncWithPresenter(self, doneSyncing):
      if (EClass.EClass.GetInstance().user.GetPermissions().GetPresPermLevel() 
       != PermissionLevel.PermissionLevel.Lockdown):
         self.__doneSyncing = doneSyncing
         
         # The message only contains a slide number if it's coming from the Presenter
         message = {'slideNum': None}
         EClass.EClass.GetInstance().connection.send('sync current slide', message)
   
   def OnSync(self, message, student):
      if EClass.EClass.GetInstance().user.isPresenter():
         # Send the Presenter's current slide number back to a student
         message['slideNum'] = self.currSlideNum
         EClass.EClass.GetInstance().connection.send(
            'sync current slide', message, student
         )
      else:
         self.currSlideNum = message['slideNum']
         self.__doneSyncing()
      
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
      slideBase = ''                # HTML that comes before the body (same for all slides)
      slideEnd = '</body>\n</html>' # HTML to end a slide
      slide = ''                    # All HTML content when being added to |slides|
      
      self.rawHTML = ''
      with open(self.path) as html:
         for line in html:
            self.rawHTML += line
            if inBody:
               # Check if there is a slide break or the end of the body
               if (line.find('<br class="slide">') != -1 or
                   line.find('<br class=slide>') != -1 or
                   line.find('</body>') != -1
               ):
                  slide += slideEnd
                  self.slides.append(Slide(slide, [Layer("Background", 255, False)]))
                  # Prepare for the next slide by getting rid of the body HTML
                  slide = '' + slideBase

               else:
                  slide += line
            else:
               slideBase += line
               if line.find('<body>'):
                  inBody = True
                  slide += slideBase
               
