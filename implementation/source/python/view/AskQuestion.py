import wx, sys
sys.path.insert(0, 'model')
from Person.Question import Question
from Presentation.QuestionList import QuestionList

class AskQuestion(wx.Frame):

   def __init__(self, parent):
      wx.Frame.__init__(self, None, wx.ID_ANY, size = (800, 300))
      self.SetLabel('Ask a Question')
      self.panel = wx.Panel(self)
      self.parent = parent
      self.questionList = QuestionList()

      self.listView = wx.ListView(self.panel, style = 
         wx.LC_REPORT|wx.BORDER_SUNKEN, name = 'Questions'
      )
      self.listView.InsertColumn(0, 'Questions')
      columnSize = self.listView.GetSize()[0]
      self.listView.SetColumnWidth(0, columnSize)

      self.questionEntry = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE)
      self.submitButton = wx.Button(self.panel, label = 'Submit')
      self.deleteButton = wx.Button(self.panel, label = 'Delete')
      self.deleteAllButton = wx.Button(self.panel, label = 'Delete All')

      self.fullQuestion = wx.TextCtrl(self.panel, style = wx.TE_READONLY | 
         wx.TE_MULTILINE
      )
      
      leftVertSizer = wx.BoxSizer(wx.VERTICAL)
      midVertSizer = wx.BoxSizer(wx.VERTICAL)
      midButtonHoriSizer = wx.BoxSizer(wx.HORIZONTAL)
      mainHoriSizer = wx.BoxSizer(wx.HORIZONTAL)

      leftVertSizer.Add(self.questionEntry, 5, wx.ALL|wx.EXPAND)
      leftVertSizer.Add(self.submitButton, 1, wx.EXPAND)

      midButtonHoriSizer.Add(self.deleteButton, 1, wx.EXPAND)
      midButtonHoriSizer.Add(self.deleteAllButton, 1, wx.EXPAND)

      midVertSizer.Add(self.listView, 5, wx.ALL|wx.EXPAND)
      midVertSizer.Add(midButtonHoriSizer, 1, wx.ALL|wx.EXPAND)
   
      mainHoriSizer.Add(leftVertSizer, 3, wx.ALL|wx.EXPAND)
      mainHoriSizer.Add(midVertSizer, 3, wx.ALL|wx.EXPAND)
      mainHoriSizer.Add(self.fullQuestion, 3, wx.ALL|wx.EXPAND)

      self.panel.SetSizer(mainHoriSizer)

      self.Bind(wx.EVT_CLOSE, self.onClose)
      self.submitButton.Bind(wx.EVT_BUTTON, self.Ask)
      self.deleteButton.Bind(wx.EVT_BUTTON, self.Delete)
      self.deleteAllButton.Bind(wx.EVT_BUTTON, self.DeleteAll)
      self.listView.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OpenQuestion)
      self.listView.Bind(wx.EVT_LIST_DELETE_ALL_ITEMS, self.ClearOpenQuestion)
      self.Refresh()

   def Ask(self, event):
      questionText = self.questionEntry.GetValue()
      self.questionEntry.Clear()

      if questionText:
         q = Question(questionText)
         self.questionList.Append(q)
         self.listView.Append((q.GetText(),))

   def Delete(self, event):
      self.questionList.Remove(self.listView.GetFocusedItem())
      self.listView.DeleteItem(self.listView.GetFocusedItem())

   def DeleteAll(self, event):
      self.questionList.RemoveAll()
      self.listView.ClearAll()

   def OpenQuestion(self, event):
      self.fullQuestion.SetValue(self.questionList[self.listView.GetFocusedItem()])

   def ClearOpenQuestion(self, event):
      self.fullQuestion.Clear()

   def onClose(self, event):
      self.parent.showAskQuestionMenuItem.Check(False)
      self.Hide()
