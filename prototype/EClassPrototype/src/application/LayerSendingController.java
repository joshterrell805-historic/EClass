package application;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;


public class LayerSendingController implements Initializable {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private AnchorPane anchor;

    @FXML
    private Label label;

    @FXML
    private Button noButton;

    @FXML
    private Button yesButton;


    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {

    	noButton.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	Scene scene = noButton.getScene();
    	    	if (scene != null) {
    	    		javafx.stage.Window window = scene.getWindow();
    	    		if (window != null) {
    	    			window.hide();
    	    		}
    	    	}
    	    }
    	});
    	
    	yesButton.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	Scene scene = yesButton.getScene();
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
