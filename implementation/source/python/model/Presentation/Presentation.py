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
      self.isSynced = True # TODO doc
      self.rawHTML = None
      # Infinite recurion without using CallLater
      # EClass.GetInstance() -> Presentation() ->EClass.GetInstance() ...
      # Wait a second, then get the instance to avoid infinite recursion
      def listen():
         EClass.EClass.GetInstance().connection.registerMessageListener(
            'sync current slide', self.OnSync
         )
         EClass.EClass.GetInstance().registerOnSaveListener(
            'presentation', self.onSaveListener
         )
      wx.CallLater(1, listen)

   def onSaveListener(self, eventType, identifier):
      assert identifier == 'presentation'
      if eventType == 'save initial data for student':
         assert self.rawHTML is not None
         return {
            'slides': map(Slide.toDict, self.slides),
            'currSlide': self.currSlideNum
         }
      elif eventType == 'save to file':
         assert not len(self.slides) == 0
         return {
            'slide num' : self.currSlideNum,
            'slides' : map(Slide.toDict, self.slides)
         }

   def loadInitialData(self, data):
      # data is the object we returned to the caller of onSaveListener, above
      self.slides = map(Slide.fromDict, data['slides'])
      self.currSlideNum = data['currSlide'];

   def loadFileData(self, data):
      # data is the object we returned to the caller of onSaveListener, above
      self.slides = map(Slide.fromDict, data['slides'])
      self.currSlideNum = data['slide num']

   def MoveToNextSlide(self):
      if self.currSlideNum < len(self.slides) - 1:
         self.currSlideNum += 1
         # If user is presenter, broadcast change to all students
         if EClass.EClass.GetInstance().user.isPresenter():
            self.OnSync({'slideNum': self.currSlideNum}, None)
         else:
            self.isSynced = False
         return True
      else:
         return False

   def MoveToPreviousSlide(self):
      if self.currSlideNum != 0:
         self.currSlideNum -= 1
         # If user is presenter, broadcast change to all students
         if EClass.EClass.GetInstance().user.isPresenter():
            self.OnSync({'slideNum': self.currSlideNum}, None)
         else:
            self.isSynced = False
         return True
      else:
         return False

   def MoveToSlide(self, slideNum):
      if slideNum > 0 and slideNum <= len(self.slides):
         self.currSlideNum = slideNum - 1
         # If user is presenter, broadcast change to all students
         if EClass.EClass.GetInstance().user.isPresenter():
            self.OnSync({'slideNum': self.currSlideNum}, None)
         else:
            self.isSynced = False
         return True
      else:
         return False

   def SyncWithPresenter(self):
      if (EClass.EClass.GetInstance().user.GetPermissions().GetPresPermLevel() 
       != PermissionLevel.PermissionLevel.Lockdown):
         self.isSynced = True
         
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
      elif self.isSynced:
         self.currSlideNum = message['slideNum']
         EClass.EClass.GetInstance().RefreshSlide()
         EClass.EClass.GetInstance().Redraw()
      
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
               
