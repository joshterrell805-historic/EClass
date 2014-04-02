package application;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import com.sun.glass.ui.Window;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Accordion;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ListView;
import javafx.scene.control.TitledPane;
import javafx.stage.Stage;

public class NewLayerController implements Initializable {
	@FXML //  fx:id="perms"
    private ChoiceBox<String> perms;
	@FXML //  fx:id="selectButton"
	private Button selectButton;
	@FXML //  fx:id="cancelButton"
	private Button cancelButton;
    
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	perms = new ChoiceBox<String>(FXCollections.observableArrayList("Everyone", "Sam", "Trent", "..."));
    	
    	selectButton.setOnAction(new EventHandler<ActionEvent>() {
			@SuppressWarnings("unchecked")
			public void handle(ActionEvent event) {
				  Scene scene = selectButton.getScene();
				  if (scene != null) {
				    javafx.stage.Window window = scene.getWindow();
				    if (window != null) {
				      window.hide();
				    }
				  }
            }		
    	});
    	
    	cancelButton.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
            	Scene scene = selectButton.getScene();
				  if (scene != null) {
				    javafx.stage.Window window = scene.getWindow();
				    if (window != null) {
				      window.hide();
				    }
				  }
            }		
    	});
    }

}
