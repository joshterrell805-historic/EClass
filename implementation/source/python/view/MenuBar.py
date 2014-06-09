import wx
import sys

from EClass import EClass
from RosterWindow import RosterWindow
from ForumWindow import ForumWindow
from DrawingTools import DrawingTools
from ApprovalTrackerGaget import ApprovalTrackerGaget
from LayerManager import LayerManager
from InitialPrompt import InitialPrompt
from AskQuestion import AskQuestion

class MenuBar:
   def __init__(self, parent):

      self.IDs = self.InitLocalVars()
      self.__rosterWindow = RosterWindow(self)
      self.__drawingTools = DrawingTools(self)
      self.layerManager = LayerManager(self)
      self.__approvalTracker = ApprovalTrackerGaget(self)
      self.__forum = ForumWindow(self)
      self.__askQuestion = AskQuestion(self)

      menuBar = wx.MenuBar()
      fileMenu = wx.Menu()
      menuBar.Append(fileMenu, 'File')
      openMenuItem = fileMenu.Append(self.IDs[0], 'Open\tCtrl+O',
                                     'Opens an existing presentation.')
      parent.Bind(wx.EVT_MENU, self.OpenPresentation, openMenuItem)

      fileMenu.AppendSeparator()
      saveMenuItem = fileMenu.Append(self.IDs[1], 'Save\tCtrl+S',
                                     'Saves the existing presentation.')
      parent.Bind(wx.EVT_MENU, self.SavePresenatation, saveMenuItem)
      fileMenu.AppendSeparator()
      quitMenuItem = fileMenu.Append(self.IDs[2], 'Quit\tCtrl+Q',
                                     'Quits EClass program.')
      parent.Bind(wx.EVT_MENU, self.Quit, quitMenuItem)

      editMenu = wx.Menu()
      menuBar.Append(editMenu, 'Edit')
      undoMenuItem = editMenu.Append(self.IDs[3], 'Undo\tCtrl+Z',
                                     'Undoes the most recent edit.')
      redoMenuItem = editMenu.Append(self.IDs[4], 'Redo\tCtrl+Y',
                                     'Redoes the most recent undo.')
      editMenu.AppendSeparator()
      cutMenuItem = editMenu.Append(self.IDs[5], 'Cut\tCtrl+X',
                                    'Cuts the selected object(s).')
      copyMenuItem = editMenu.Append(self.IDs[6], 'Copy\tCtrl+C',
                                     'Copies the selected object(s).')
      pasteMenuItem = editMenu.Append(self.IDs[7], 'Paste\tCtrl+V',
                                      'Pastes the selected object(s).')
      editMenu.AppendSeparator()
      selectAllMenuItem = editMenu.Append(self.IDs[8],
                                          'Select All\tCtrl+A', 'Selects all objects.')
      selectNoneMenuItem = editMenu.Append(self.IDs[9],
                                           'Select None\tCtrl+Shift+A', 'Deselects all selected objects.')

      viewMenu = wx.Menu()
      menuBar.Append(viewMenu, 'View')
      self.showRosterMenuItem = viewMenu.Append(self.IDs[10], 'Show Roster',
                                                'Shows the roster window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleRoster, self.showRosterMenuItem)

      self.showDrawingToolsMenuItem = viewMenu.Append(self.IDs[11], 'Show Drawing Tools',
                                                      'Shows the drawing tools window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleDrawingTools, self.showDrawingToolsMenuItem)

      self.showLayerManagerMenuItem = viewMenu.Append(self.IDs[12], 'Show Layer Manager',
                                                      'Shows the layer manager window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleLayerManager, self.showLayerManagerMenuItem)

      self.showApprovalTrackerMenuItem = viewMenu.Append(self.IDs[13], 'Show Approval Tracker',
                                                         'Shows the approval tracker window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleApprovalTracker, self.showApprovalTrackerMenuItem)

      self.showForumMenuItem = viewMenu.Append(self.IDs[14], 'Show Forum',
                                               'Shows the forum window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleForum, self.showForumMenuItem)

      self.showAskQuestionMenuItem = viewMenu.Append(self.IDs[15], 'Show Questions',
                                                     'Shows the questions window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleAskQuestion, self.showAskQuestionMenuItem)

      viewMenu.AppendSeparator()
      self.fullScreenMenuItem = viewMenu.Append(self.IDs[16], 'Full Screen\tCtrl+F',
                                                'Zooms to full screen.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleFullScreen, self.fullScreenMenuItem)

      parent.SetMenuBar(menuBar)
      self.parent = parent

   def InitLocalVars(self):
      localVars = []
      
      ID_FILE_OPEN = wx.NewId()
      ID_FILE_SAVE = wx.NewId()
      ID_FILE_QUIT = wx.NewId()
      ID_EDIT_UNDO = wx.NewId()
      ID_EDIT_REDO = wx.NewId()
      ID_EDIT_CUT = wx.NewId()
      ID_EDIT_COPY = wx.NewId()
      ID_EDIT_PASTE = wx.NewId()
      ID_EDIT_SELECTALL = wx.NewId()
      ID_EDIT_SELECTNONE = wx.NewId()
      ID_VIEW_SHOWROSTER = wx.NewId()
      ID_VIEW_SHOWDRAWINGTOOLS = wx.NewId()
      ID_VIEW_SHOWLAYERMANAGER = wx.NewId()
      ID_VIEW_SHOWAPPROVALTRACKER = wx.NewId()
      ID_VIEW_SHOWFORUM = wx.NewId()
      ID_VIEW_SHOWASKQUESTION = wx.NewId()
      ID_VIEW_FULLSCREEN = wx.NewId()

      localVars.append(ID_FILE_OPEN)
      localVars.append(ID_FILE_SAVE)
      localVars.append(ID_FILE_QUIT)
      localVars.append(ID_EDIT_UNDO)
      localVars.append(ID_EDIT_REDO)
      localVars.append(ID_EDIT_CUT)
      localVars.append(ID_EDIT_COPY)
      localVars.append(ID_EDIT_PASTE)
      localVars.append(ID_EDIT_SELECTALL)
      localVars.append(ID_EDIT_SELECTNONE)
      localVars.append(ID_VIEW_SHOWROSTER)
      localVars.append(ID_VIEW_SHOWDRAWINGTOOLS)
      localVars.append(ID_VIEW_SHOWLAYERMANAGER)
      localVars.append(ID_VIEW_SHOWAPPROVALTRACKER)
      localVars.append(ID_VIEW_SHOWFORUM)
      localVars.append(ID_VIEW_SHOWASKQUESTION)
      localVars.append(ID_VIEW_FULLSCREEN)
      return localVars

   def OpenPresentation(self, e):
      self.parent.importPresentation.Show()

   def SavePresenatation(self, e):
      saveFileDialog = wx.FileDialog(self, "Save As", "", "", "HTML files (*.html)|*.html",
                                     wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

      # user decided not to save presentation
      if saveFileDialog.ShowModal() == wx.ID_CANCEL:
         return

      # save the current contents in the file
      outputStream = wx.FileOutputStream(saveFileDialog.GetPath())

      # file could not be saved successfully
      if not outputStream.IsOk():
         wx.LogError("Cannot save current contents in file '%s'.."%saveFileDialog.GetPath())
         return


   def ToggleRoster(self, e):
      rosterCourseName = EClass.GetInstance().user.hostedClass['name']
      if not self.showRosterMenuItem.IsChecked():
         self.__rosterWindow.Hide()
      else:
         self.__rosterWindow.classText.SetValue(rosterCourseName)
         self.__rosterWindow.Show()

   def ToggleDrawingTools(self, e):
      if not self.showDrawingToolsMenuItem.IsChecked():
         self.__drawingTools.Hide()
      else:
         self.__drawingTools.Show()

   def ToggleLayerManager(self, e):
      if not self.showLayerManagerMenuItem.IsChecked():
         self.layerManager.Hide()
      else:
         self.layerManager.Show()

   def ToggleApprovalTracker(self, e):
      if not self.showApprovalTrackerMenuItem.IsChecked():
         self.__approvalTracker.Hide()
      else:
         self.__approvalTracker.Show()

   def ToggleForum(self, e):
      if not self.showForumMenuItem.IsChecked():
         self.__forum.Hide()
      else:
         self.__forum.Show()

   def ToggleAskQuestion(self, e):
      if not self.showAskQuestionMenuItem.IsChecked():
         self.__askQuestion.Hide()
      else:
         self.__askQuestion.Show()

   def ToggleFullScreen(self, e):
      self.parent.ShowFullScreen(
         not self.parent.IsFullScreen(), wx.FULLSCREEN_NOBORDER
      )

   def Quit(self, e):
      self.parent.Close()
