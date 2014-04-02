package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.control.RadioMenuItem;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.control.TitledPane;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class EClass implements Initializable {
    @FXML
    public static Button prevButton;
    @FXML
    public static Button nextButton;
    @FXML
    public static TextField slideNumTextField;
    @FXML
    public static TextArea whiteboardTextArea;
    @FXML
    public static TextArea slideNumTextArea;
    @FXML
    public static Button openLectureButton;
    @FXML
    public static Button newLectureButton;
    @FXML //  fx:id="closeLectureButton"
    public static Button closeLectureButton; //Value injected by FXMLLoader
    @FXML //  fx:id="lecturePane"
    public static Pane lecturePane; //Value injected by FXMLLoader
    @FXML
    public static Rectangle rectangle1;
    @FXML
    public static Rectangle rectangle2;
    @FXML
    public static Rectangle rectangle3;
	@FXML
	private MenuBar MenuBar;
	@FXML
	private Menu View;
	@FXML
	private Menu File;
	@FXML
	private MenuItem sendLayerItem;
	@FXML
	private MenuItem receiveLayerItem;
	@FXML
	private RadioMenuItem MBShowApprovalTracker;
	@FXML
	private RadioMenuItem MBShowApprovalGadget;
	@FXML
	private RadioMenuItem MBShowApprovalTrackerAnalysis;
	@FXML
	private RadioMenuItem MBShowApprovalTrackerSettings;
	@FXML
	private RadioMenuItem MBShowDrawingTools;
	@FXML
	private RadioMenuItem MBShowForum;
	@FXML
	private RadioMenuItem MBShowLayerManager;
	@FXML
	private RadioMenuItem MBAskQuestion;
	@FXML
	private RadioMenuItem MBShowRoster;
	@FXML
	private RadioMenuItem MBShowQuestions;
	@FXML
	private RadioMenuItem MBShowAVControl;
	@FXML
	private TitledPane approvalTracker;
	@FXML
	private Button setApprovalButton;

    
    public static final String slideContent1 = "I. This week's material:\n"
    		+ "\tA. Milestone 2 writeup and example.\n\n"
    		+ "\tB. Requirements document HTML standards\n\n"
    		+ "\tC. Conventions for standardized GUIs\n\n"
    		+ "\tD. These lecture notes\n\n"
    		+ "\tE. Week 3 lab notes, with more on SVN";
    
    public static final String slideContent2 = "II. Some paper UI sketches and other paper notes are OK for Milestone 2, as long as the overall document structure is online in HTML format.\n"
    		+ "\tA. Clearly label all paper materials so they can be referenced from the online requirements document.\n\n"
    		+ "\t\t1. Figure number and caption for screen pictures.\n\n"
    		+ "\t\t2. Title for other notes.\n\n"
    		+ "\tB. Make copies if you want to keep the originals.\n\n"
    		+ "\tC. Deliver to lab or Fisher's office by 5 PM Friday.";
    
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	setNavigationVisible(false);
    	prevButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	moveToSlide(1);
            }		
    	});
    	
    	nextButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	moveToSlide(2);
            }		
    	});
    	
    	slideNumTextField.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	moveToSlide(slideNumTextField.getText().equals("1") ? 1 : 2);
            }		
    	});
    	
    	openLectureButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("ImportPrompt.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root, 250, 170.5));
                stage.show();
            }		
    	});
    	
    	newLectureButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("inserting-elements.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root, 600, 400));
                stage.setTitle("New Lecture");
                stage.show();
            }		
    	});	
    	
    	sendLayerItem.setOnAction(new EventHandler<ActionEvent>() {
			@Override
            public void handle(ActionEvent event) {
            	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("LayerSending.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root, 341, 321));
                stage.show();
            }		
		
		});
    	
    	receiveLayerItem.setOnAction(new EventHandler<ActionEvent>() {
			@Override
            public void handle(ActionEvent event) {
            	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("LayerAccepting.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root, 341, 321));
                stage.show();
            }		
		
		});
    	
		MBShowApprovalTracker.setOnAction(new EventHandler<ActionEvent>() {
			@Override
            public void handle(ActionEvent event) {
            	Parent root = null;
            	try {
					root = FXMLLoader.load(getClass().getResource("ApprovalTracker.fxml"));
				} catch (IOException e) {
					e.printStackTrace();
				}
                Stage stage = new Stage();
                stage.setScene(new Scene(root, 527, 159));
                stage.show();
            }		
		
		});
		
		MBShowRoster.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("Roster.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 307, 586));
	            stage.show();
			}
		
		});
		
		MBShowForum.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("Forum.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 226, 558));
	            stage.show();
			}
		
		});
		
		MBShowQuestions.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("QuestionAsking.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 216, 287));
	            stage.show();
			}
		
		});
		
		MBShowAVControl.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("AudioVideo.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root));
	            stage.show();
			}
		
		});
		
		MBShowLayerManager.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("LayerManager.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 258, 206));
	            stage.setTitle("Layer Manager");
	            stage.show();
			}
		
		});
		
		MBShowDrawingTools.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("DrawingTools.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 170, 450));
	            stage.show();
			}
		});
		
		MBAskQuestion.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("AskingQuestion.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 387, 209));
	            stage.show();
			}
		});
		
		MBShowApprovalGadget.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("ApprovalGadget.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
	            Stage stage = new Stage();
	            stage.setScene(new Scene(root, 142, 308));
	            stage.show();
			}
		});
		
		MBShowApprovalTrackerAnalysis.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				// TODO Auto-generated method stub
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("ApprovalTrackerAnalysis.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
				Stage stage = new Stage();
				stage.setScene(new Scene(root, 788, 300));
				stage.show();
			}
			
		});
		
		MBShowApprovalTrackerSettings.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				// TODO Auto-generated method stub
				Parent root = null;
				try {
					root = FXMLLoader.load(getClass().getResource("ApprovalTrackerSettings.fxml"));
				}
				catch (IOException e) {
					e.printStackTrace();
				}
				Stage stage = new Stage();
				stage.setScene(new Scene(root, 537, 201));
				stage.show();
			}
		});
    }
    
    private void moveToSlide(int slideNum) {
    	if (slideNum == 1) {
	    	whiteboardTextArea.setText(slideContent1);
	    	slideNumTextArea.setText("1");
    	}
    	else { // Anything past the last slide number goes to the last slide
    		whiteboardTextArea.setText(slideContent2);
    		slideNumTextArea.setText("2");
    	}
    }
    
    public static void setNavigationVisible(boolean bool) {
    	if (bool) {
    		rectangle1.setVisible(true);
    		rectangle2.setVisible(true);
    		rectangle3.setVisible(true);
    		prevButton.setVisible(true);
    		nextButton.setVisible(true);
    		slideNumTextField.setVisible(true);
    		slideNumTextArea.setVisible(true);
    	}
    	else {
    		rectangle1.setVisible(false);
    		rectangle2.setVisible(false);
    		rectangle3.setVisible(false);
    		prevButton.setVisible(false);
    		nextButton.setVisible(false);
    		slideNumTextField.setVisible(false);
    		slideNumTextArea.setVisible(false);
    	}
    }
}
