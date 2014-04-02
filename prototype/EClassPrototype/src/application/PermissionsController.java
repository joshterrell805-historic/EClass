package application;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;

public class PermissionsController implements Initializable {
	@FXML
    private Button permAcceptButton;
	@FXML
    private Button permCancelButton;
	@FXML
	private RadioButton unrestrictedRadioButton;
	@FXML
	private RadioButton normalRadioButton;
	@FXML
    private RadioButton lockdownRadioButton;
	@FXML
	private ToggleGroup permGroup;
    
    @Override
    public void initialize(URL fxmlFileLocation, final ResourceBundle resources) {
    	permGroup = new ToggleGroup();
    	normalRadioButton.setSelected(true);
    	
    	permAcceptButton.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	Scene scene = permCancelButton.getScene();
    	    	if (scene != null) {
    	    		javafx.stage.Window window = scene.getWindow();
    	    		if (window != null) {
    	    			window.hide();
    	    		}
    	    	}
    	    }
    	});
    	
    	permCancelButton.setOnAction(new EventHandler<ActionEvent>() {
    	    public void handle(ActionEvent e) {
    	    	((Node)(e.getSource())).getScene().getWindow().hide();
    	    }
    	});
    }
}
