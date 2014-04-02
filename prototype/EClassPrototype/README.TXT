  ______ _____ _                    _____  ______          _____  __  __ ______ 
 |  ____/ ____| |                  |  __ \|  ____|   /\   |  __ \|  \/  |  ____|
 | |__ | |    | | __ _ ___ ___     | |__) | |__     /  \  | |  | | \  / | |__   
 |  __|| |    | |/ _` / __/ __|    |  _  /|  __|   / /\ \ | |  | | |\/| |  __|  
 | |___| |____| | (_| \__ \__ \    | | \ \| |____ / ____ \| |__| | |  | | |____ 
 |______\_____|_|\__,_|___/___/    |_|  \_\______/_/    \_\_____/|_|  |_|______|

================================================================================
================================================================================
================================================================================
================================================================================



  _______    _     _               __    _____            _             _       
 |__   __|  | |   | |             / _|  / ____|          | |           | |      
    | | __ _| |__ | | ___    ___ | |_  | |     ___  _ __ | |_ ___ _ __ | |_ ___ 
    | |/ _` | '_ \| |/ _ \  / _ \|  _| | |    / _ \| '_ \| __/ _ \ '_ \| __/ __|
    | | (_| | |_) | |  __/ | (_) | |   | |___| (_) | | | | ||  __/ | | | |_\__ \
    |_|\__,_|_.__/|_|\___|  \___/|_|    \_____\___/|_| |_|\__\___|_| |_|\__|___/


1) Instructions for getting to windows.
2) Instructions for building and running the prototype.




 __          ___           _               
 \ \        / (_)         | |              
  \ \  /\  / / _ _ __   __| | _____      __
   \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / /
    \  /\  /  | | | | | (_| | (_) \ V  V / 
     \/  \/   |_|_| |_|\__,_|\___/ \_/\_/  
             _____           _                   _   _                 
            |_   _|         | |                 | | (_)                
              | |  _ __  ___| |_ _ __ _   _  ___| |_ _  ___  _ __  ___ 
              | | | '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|
             _| |_| | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \
            |_____|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/
           

   Team Member     |          Actions to get to window
======================================================================
Mike Sevilla       |    Select 'File' in the menubar
                   |    Select 'Edit' in the menubar
                   |    Select 'View' in the menubar
                   |    Press 'Show Approval Tracker' in the View dialog
                   |    Press 'Show Drawing Tools' in the View dialog
                   |    Press 'Show Approval Tracker Analysis' in the View dialog
                   |    Press 'Show Approval Tracker Settings' in the View dialog
======================================================================
Joel Wilcox        |    Choose a lecture and press 'Select' in the
                   |       'Open Lecture' class list
                   |    Press the first 'Options' button at the top of the
                   |       'Roster' window
                   |    Press 'Change permissions...' in the 'Options' context
                   |       menu
                   |    Press 'Kick' in the 'Options' context menu
                   |    Select the 'Show Audio/Video Control' item in the
                   |       'View' Menu
                   |    Press 'On' in the 'Audio/Video Control' window
======================================================================
Carson Carroll     |    Select the 'Show Roster' item in the 'View' menu
                   |    Select the 'Show Questions' item in the 'View' menu
                   |    Select the 'Show Forum' item in the 'View' menu
                   |    Select the 'Send Layer' item in the 'File' menu
                   |    Select the 'Receive Layer' item in the 'File' menu
======================================================================
Josh Terrell       |    From the initial screen select the New Lecture button.
                   |    From the 'New Presentation' window press the textbox
                   |       button on the right sidebar, then click anywhere in
                   |       the center panel.
                   |    From the 'New Presentation' window press the list button
                   |       on the right sidebar, then click anywhere in the
                   |       center panel (that isn't on an existing element,
                   |       such as the text box inserted in the step above).
                   |    From the 'Insert List' window, press the insert or
                   |       element buttons, respectively.
                   |    From the 'New Presentation' window, press the slidify
                   |       button.
======================================================================
Kevin Le           |    The EClass.fxml view is shown after the user is logged
                   |       in. It consists of the initial whiteboard with the 
                   |       buttons "Open Lecture" and "New Lecture".
                   |    The ImportPrompt.fxml view is popped up if the user
                   |       clicks 'Open Lecture' from the initial EClass.fxml
                   |       view.
                   |    The ImportList.fxml view is popped up if the user clicks
                   |       'Yes' from the Import Lecture prompt.
                   |    The AskingQuestion.fxml view is popped up if the user
                   |       clicks on 'Ask a Question' from the 'View' tab of the
                   |       main menu bar.
                   |    The ApprovalGadget.fxml view is popped up if the user
                   |       clicks 'Show Approval Gadget' from the 'View' tab of
                   |       the main menu bar.
======================================================================
Andrew Lisowski    |    Select the 'Layer Manager' item in the 'View" menu 
                   |    Select the 'Color' item in the 'Drawing tools' menu
                   |    Click the 'Add' button in the 'Layer Manager'
                   |    Click the 'lock' button in the 'Layer Manager'
                   |    The first window launched in the EClass is the login 
                   |       window




  ____        _ _     _ _              
 |  _ \      (_) |   | (_)             
 | |_) |_   _ _| | __| |_ _ __   __ _  
 |  _ <| | | | | |/ _` | | '_ \ / _` | 
 | |_) | |_| | | | (_| | | | | | (_| | 
 |____/ \__,_|_|_|\__,_|_|_| |_|\__, | 
                                 __/ | 
                                |___/  
                        _____                   _             
           ___         |  __ \                 (_)            
          ( _ )        | |__) |   _ _ __  _ __  _ _ __   __ _ 
          / _ \/\      |  _  / | | | '_ \| '_ \| | '_ \ / _` |
         | (_>  <      | | \ \ |_| | | | | | | | | | | | (_| |
          \___/\/      |_|  \_\__,_|_| |_|_| |_|_|_| |_|\__, |
                                                         __/ |
                                                        |___/
Building:

   1. From the project root directory, navigate to prototype/EClassPrototype

      $ cd prototype/EClassPrototype

   2. Run make to build the project. This command builds all the class files
       from source.

      $ make clean && make


Running:

   1. Run the jar file as an executable jar (assumes working directory has not
       changed). The included eclass.jar file runs on Windows 7 with Java 1.7.

      $ java -jar eclass.jar

Notes about dependency on JavaFX:

   JavaFX is not supported on the csc unix lab machines. Additionally, javafx
    requires binary libraries that are architecture dependent. The supplied
    jar runs on Windows 7 with Java version 1.7.
