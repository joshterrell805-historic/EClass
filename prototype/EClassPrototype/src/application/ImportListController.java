package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.control.Accordion;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TitledPane;

public class ImportListController implements Initializable {
	@FXML //  fx:id="accordion"
	private Accordion accordion;
	@FXML //  fx:id="firstListView"
    private ListView<String> firstListView;
	@FXML //  fx:id="secondListView"
    private ListView<String> secondListView;
	@FXML //  fx:id="thirdListView"
    private ListView<String> thirdListView;
	@FXML //  fx:id="forthListView"
    private ListView<String> forthListView;
	@FXML //  fx:id="fifthListView"
    private ListView<String> fifthListView;
	@FXML //  fx:id="selectButton"
	private Button selectButton;
	@FXML //  fx:id="cancelButton"
	private Button cancelButton;
    
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	ObservableList<String> items = FXCollections.observableArrayList (
    		    "Week 1 Lecture", "Week 2 Lecture", "Week 3 Lecture", "Week 4 Lecture",
    		    "Week 5 Lecture", "Week 6 Lecture", "Week 7 Lecture", "Week 8 Lecture",
    		    "Week 9 Lecture", "Week 10 Lecture");
    	firstListView.setItems(items);
    	secondListView.setItems(items);
    	thirdListView.setItems(items);
    	forthListView.setItems(items);
    	fifthListView.setItems(items);
    	
    	selectButton.setOnAction(new EventHandler<ActionEvent>() {
			@SuppressWarnings("unchecked")
			Parent root = null;
			public void handle(ActionEvent event) {
            	((Node)(event.getSource())).getScene().getWindow().hide();
            	TitledPane currPane = (TitledPane) accordion.getExpandedPane();
            	ListView<String> currList = (ListView<String>) currPane.getContent();
            	System.out.println("Lecture selected is: " + currPane.getText() + ", "
            			+ currList.getSelectionModel().getSelectedItem());
            	EClass.lecturePane.getChildren().clear();
            	EClass.lecturePane.setVisible(false);
            	EClass.whiteboardTextArea.setText(EClass.slideContent1);
            	EClass.slideNumTextArea.setText("1");
            	EClass.setNavigationVisible(true);
            }		
    	});
    	
    	cancelButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	((Node)(event.getSource())).getScene().getWindow().hide();
            }		
    	});
    }

}
