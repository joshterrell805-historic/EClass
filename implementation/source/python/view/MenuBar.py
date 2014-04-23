import wx
import sys

from RosterWindow import RosterWindow
from ForumWindow import ForumWindow
from DrawingTools import DrawingTools
from ApprovalTrackerGaget import ApprovalTrackerGaget
from LayerManager import LayerManager

class MenuBar:

   def __init__(self, parent):

      ID_FILE_NEWLECTURE = wx.NewId()
      ID_FILE_OPEN = wx.NewId()
      ID_FILE_OPENRECENT = wx.NewId()
      ID_FILE_SAVE = wx.NewId()
      ID_FILE_SAVEAS = wx.NewId()
      ID_FILE_PRINT = wx.NewId()
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
      ID_VIEW_ZOOMIN = wx.NewId()
      ID_VIEW_ZOOMOUT = wx.NewId()
      ID_VIEW_ZOOMTOFIT = wx.NewId()
      ID_VIEW_FULLSCREEN = wx.NewId()

      menuBar = wx.MenuBar()

      fileMenu = wx.Menu()
      menuBar.Append(fileMenu, 'File')
      newLectureMenuItem = fileMenu.Append(ID_FILE_NEWLECTURE, 'New Lecture\tCtrl+N', 'Opens a new lecture.')
      openMenuItem = fileMenu.Append(ID_FILE_OPEN, 'Open\tCtrl+O', 'Opens an existing lecture.')
      openRecentMenuItem = wx.Menu()
      fileMenu.AppendMenu(ID_FILE_OPENRECENT, 'Open Recent', openRecentMenuItem, 'Opens a recently open lecture.')
      fileMenu.AppendSeparator()
      saveMenuItem = fileMenu.Append(ID_FILE_SAVE, 'Save\tCtrl+S', 'Saves the existing lecture.')
      saveAsMenuItem = fileMenu.Append(ID_FILE_SAVEAS, 'Save as...\tCtrl+Shift+S', 'Saves the existing lecture as something.')
      fileMenu.AppendSeparator()
      printMenuItem = fileMenu.Append(ID_FILE_PRINT, 'Print...\tCtrl+P', 'Prints the current view.')
      fileMenu.AppendSeparator()
      quitMenuItem = fileMenu.Append(ID_FILE_QUIT, 'Quit\tCtrl+Q', 'Quits EClass program.')
      parent.Bind(wx.EVT_MENU, self.Quit, quitMenuItem)

      editMenu = wx.Menu()
      menuBar.Append(editMenu, 'Edit')
      undoMenuItem = editMenu.Append(ID_EDIT_UNDO, 'Undo\tCtrl+Z', 'Undoes the most recent edit.')
      redoMenuItem = editMenu.Append(ID_EDIT_REDO, 'Redo\tCtrl+Y', 'Redoes the most recent undo.')
      editMenu.AppendSeparator()
      cutMenuItem = editMenu.Append(ID_EDIT_CUT, 'Cut\tCtrl+X', 'Cuts the selected object(s).')
      copyMenuItem = editMenu.Append(ID_EDIT_CUT, 'Copy\tCtrl+C', 'Copies the selected object(s).')
      pasteMenuItem = editMenu.Append(ID_EDIT_PASTE, 'Paste\tCtrl+V', 'Pastes the selected object(s).')
      editMenu.AppendSeparator()
      selectAllMenuItem = editMenu.Append(ID_EDIT_SELECTALL, 'Select All\tCtrl+A', 'Selects all objects.')
      selectNoneMenuItem = editMenu.Append(ID_EDIT_SELECTNONE, 'Select None\tCtrl+Shift+A', 'Deselects all of the objects.')

      viewMenu = wx.Menu()
      menuBar.Append(viewMenu, 'View')
      self.showRosterMenuItem = viewMenu.Append(ID_VIEW_SHOWROSTER, 'Show Roster', 'Shows the roster window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleRoster, self.showRosterMenuItem)
      showDrawingToolsMenuItem = viewMenu.Append(ID_VIEW_SHOWDRAWINGTOOLS, 'Show Drawing Tools', 'Shows the drawing tools window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleDrawingTools, showDrawingToolsMenuItem)
      self.showLayerManagerMenuItem = viewMenu.Append(ID_VIEW_SHOWLAYERMANAGER, 'Show Layer Manager', 'Shows the layer manager window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleLayerManager, self.showLayerManagerMenuItem)
      showApprovalTrackerMenuItem = viewMenu.Append(ID_VIEW_SHOWAPPROVALTRACKER, 'Show Approval Tracker', 'Shows the approval tracker window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleApprovalTracker, showApprovalTrackerMenuItem)

      showForumMenuItem = viewMenu.Append(ID_VIEW_SHOWFORUM, 'Show Forum', 'Shows the forum window.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleForum, showForumMenuItem)

      viewMenu.AppendSeparator()
      zoomInMenuItem = viewMenu.Append(ID_VIEW_ZOOMIN, 'Zoom In\tCtrl+=', 'Zooms into the screen.')
      zoomOutMenuItem = viewMenu.Append(ID_VIEW_ZOOMOUT, 'Zoom Out\tCtrl+-', 'Zooms out of the screen.')
      zoomToFitMenuItem = viewMenu.Append(ID_VIEW_ZOOMTOFIT, 'Zoom to Fit\tCtrl+0', 'Zooms to the original size of the screen.')
      viewMenu.AppendSeparator()
      self.fullScreenMenuItem = viewMenu.Append(ID_VIEW_FULLSCREEN, 'Full Screen\tCtrl+F', 'Zooms to full screen.', wx.ITEM_CHECK)
      parent.Bind(wx.EVT_MENU, self.ToggleFullScreen, self.fullScreenMenuItem)

      parent.SetMenuBar(menuBar)

      self.parent = parent

   def Quit(self, e):
      self.parent.Close()

   def ToggleRoster(self, e):
      self.roster = RosterWindow()
      #self.roster.Show(not showRosterMenuItem.IsChecked())

   def ToggleDrawingTools(self, e):
      DrawingTools()
      #if self.showDrawingToolsMenuItem.IsChecked():
      #   self.showDrawingToolsMenuItem.Show()
      #else:
      #   self.showDrawingToolsMenuItem.Hide()
      # pass

   def ToggleLayerManager(self, e):
      self.layerManager = LayerManager(self.parent)
      #self.layerManager.Show(not self.showLayerManagerMenuItem.IsChecked())

   def ToggleApprovalTracker(self, e):
      # if self.showApprovalTrackerMenuItem.IsChecked():
      #    self.showApprovalTrackerMenuItem.Show()
      # else:
      #    self.showApprovalTrackerMenuItem.Hide()
      ApprovalTrackerGaget()

   def ToggleForum(self, e):
      self.forum = ForumWindow()
      #forum.Show(not showForumMenuItem.IsChecked())

   def ToggleFullScreen(self, e):
      self.parent.ShowFullScreen(
         not self.parent.IsFullScreen(), wx.FULLSCREEN_NOCAPTION
      )
